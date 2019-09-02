import cv2
import numpy as np

np.random.seed(0)

# get HOG
def HOG(img):
    # Grayscale
    def BGR2GRAY(img):
        gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
        return gray

    # Magnitude and gradient
    def get_gradXY(gray):
        H, W = gray.shape

        # padding before grad
        gray = np.pad(gray, (1, 1), 'edge')

        # get grad x
        gx = gray[1:H+1, 2:] - gray[1:H+1, :W]
        # get grad y
        gy = gray[2:, 1:W+1] - gray[:H, 1:W+1]
        # replace 0 with 
        gx[gx == 0] = 1e-6

        return gx, gy

    # get magnitude and gradient
    def get_MagGrad(gx, gy):
        # get gradient maginitude
        magnitude = np.sqrt(gx ** 2 + gy ** 2)

        # get gradient angle
        gradient = np.arctan(gy / gx)

        gradient[gradient < 0] = np.pi / 2 + gradient[gradient < 0] + np.pi / 2

        return magnitude, gradient

    # Gradient histogram
    def quantization(gradient):
        # prepare quantization table
        gradient_quantized = np.zeros_like(gradient, dtype=np.int)

        # quantization base
        d = np.pi / 9

        # quantization
        for i in range(9):
            gradient_quantized[np.where((gradient >= d * i) & (gradient <= d * (i + 1)))] = i

        return gradient_quantized


    # get gradient histogram
    def gradient_histogram(gradient_quantized, magnitude, N=8):
        # get shape
        H, W = magnitude.shape

        # get cell num
        cell_N_H = H // N
        cell_N_W = W // N
        histogram = np.zeros((cell_N_H, cell_N_W, 9), dtype=np.float32)

        # each pixel
        for y in range(cell_N_H):
            for x in range(cell_N_W):
                for j in range(N):
                    for i in range(N):
                        histogram[y, x, gradient_quantized[y * 4 + j, x * 4 + i]] += magnitude[y * 4 + j, x * 4 + i]

        return histogram

		# histogram normalization
    def normalization(histogram, C=3, epsilon=1):
        cell_N_H, cell_N_W, _ = histogram.shape
        ## each histogram
        for y in range(cell_N_H):
    	    for x in range(cell_N_W):
       	    #for i in range(9):
                histogram[y, x] /= np.sqrt(np.sum(histogram[max(y - 1, 0) : min(y + 2, cell_N_H),
                                                            max(x - 1, 0) : min(x + 2, cell_N_W)] ** 2) + epsilon)

        return histogram

    # 1. BGR -> Gray
    gray = BGR2GRAY(img)

    # 1. Gray -> Gradient x and y
    gx, gy = get_gradXY(gray)

    # 2. get gradient magnitude and angle
    magnitude, gradient = get_MagGrad(gx, gy)

    # 3. Quantization
    gradient_quantized = quantization(gradient)

    # 4. Gradient histogram
    histogram = gradient_histogram(gradient_quantized, magnitude)
    
    # 5. Histogram normalization
    histogram = normalization(histogram)

    return histogram


# get IoU overlap ratio
def iou(a, b):
	# get area of a
    area_a = (a[2] - a[0]) * (a[3] - a[1])
	# get area of b
    area_b = (b[2] - b[0]) * (b[3] - b[1])

	# get left top x of IoU
    iou_x1 = np.maximum(a[0], b[0])
	# get left top y of IoU
    iou_y1 = np.maximum(a[1], b[1])
	# get right bottom of IoU
    iou_x2 = np.minimum(a[2], b[2])
	# get right bottom of IoU
    iou_y2 = np.minimum(a[3], b[3])

	# get width of IoU
    iou_w = iou_x2 - iou_x1
	# get height of IoU
    iou_h = iou_y2 - iou_y1

	# get area of IoU
    area_iou = iou_w * iou_h
	# get overlap ratio between IoU and all area
    iou = area_iou / (area_a + area_b - area_iou)

    return iou

# resize using bi-linear
def resize(img, h, w):
    # get shape
    _h, _w, _c  = img.shape

    # get resize ratio
    ah = 1. * h / _h
    aw = 1. * w / _w

    # get index of each y
    y = np.arange(h).repeat(w).reshape(w, -1)
    # get index of each x
    x = np.tile(np.arange(w), (h, 1))

    # get coordinate toward x and y of resized image
    y = (y / ah)
    x = (x / aw)

    # transfer to int
    ix = np.floor(x).astype(np.int32)
    iy = np.floor(y).astype(np.int32)

    # clip index
    ix = np.minimum(ix, _w-2)
    iy = np.minimum(iy, _h-2)

    # get distance between original image index and resized image index
    dx = x - ix
    dy = y - iy

    dx = np.tile(dx, [_c, 1, 1]).transpose(1, 2, 0)
    dy = np.tile(dy, [_c, 1, 1]).transpose(1, 2, 0)
    
    # resize
    out = (1 - dx) * (1 - dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix + 1] + (1 - dx) * dy * img[iy + 1, ix] + dx * dy * img[iy + 1, ix + 1]
    out[out > 255] = 255

    return out


# neural network
class NN:
    def __init__(self, ind=2, w=64, w2=64, outd=1, lr=0.1):
        # layer 1 weight
        self.w1 = np.random.normal(0, 1, [ind, w])
        # layer 1 bias
        self.b1 = np.random.normal(0, 1, [w])
        # layer 2 weight
        self.w2 = np.random.normal(0, 1, [w, w2])
        # layer 2 bias
        self.b2 = np.random.normal(0, 1, [w2])
        # output layer weight
        self.wout = np.random.normal(0, 1, [w2, outd])
        # output layer bias
        self.bout = np.random.normal(0, 1, [outd])
        # learning rate
        self.lr = lr

    def forward(self, x):
        # input tensor
        self.z1 = x
        # layer 1 output tensor
        self.z2 = sigmoid(np.dot(self.z1, self.w1) + self.b1)
        # layer 2 output tensor
        self.z3 = sigmoid(np.dot(self.z2, self.w2) + self.b2)
        # output layer tensor
        self.out = sigmoid(np.dot(self.z3, self.wout) + self.bout)
        return self.out

    def train(self, x, t):
        # backpropagation output layer
        #En = t * np.log(self.out) + (1-t) * np.log(1-self.out)
        En = (self.out - t) * self.out * (1 - self.out)
        # get gradients for weight and bias
        grad_wout = np.dot(self.z3.T, En)
        grad_bout = np.dot(np.ones([En.shape[0]]), En)
        # update weight and bias
        self.wout -= self.lr * grad_wout
        self.bout -= self.lr * grad_bout

        # backpropagation inter layer
        # get gradients for weight and bias
        grad_u2 = np.dot(En, self.wout.T) * self.z3 * (1 - self.z3)
        grad_w2 = np.dot(self.z2.T, grad_u2)
        grad_b2 = np.dot(np.ones([grad_u2.shape[0]]), grad_u2)
        # update weight and bias
        self.w2 -= self.lr * grad_w2
        self.b2 -= self.lr * grad_b2
        
        # get gradients for weight and bias
        grad_u1 = np.dot(grad_u2, self.w2.T) * self.z2 * (1 - self.z2)
        grad_w1 = np.dot(self.z1.T, grad_u1)
        grad_b1 = np.dot(np.ones([grad_u1.shape[0]]), grad_u1)
        # update weight and bias
        self.w1 -= self.lr * grad_w1
        self.b1 -= self.lr * grad_b1

# sigmoid
def sigmoid(x):
    return 1. / (1. + np.exp(-x))

# train
def train_nn(nn, train_x, train_t, iteration_N=10000):
    # each iteration
    for i in range(iteration_N):
        # feed-forward data
        nn.forward(train_x)
        # update parameter
        nn.train(train_x, train_t)

    return nn


# crop bounding box and make dataset
def make_dataset(img, gt, Crop_N=200, L=60, th=0.5, H_size=32):
    # get shape
    H, W, _ = img.shape

    # get HOG feature dimension
    HOG_feature_N = ((H_size // 8) ** 2) * 9

    # prepare database
    db = np.zeros([Crop_N, HOG_feature_N + 1])

    # each crop
    for i in range(Crop_N):
        # get left top x of crop bounding box
        x1 = np.random.randint(W - L)
        # get left top y of crop bounding box
        y1 = np.random.randint(H - L)
        # get right bottom x of crop bounding box
        x2 = x1 + L
        # get right bottom y of crop bounding box
        y2 = y1 + L

        # get bounding box
        crop = np.array((x1, y1, x2, y2))

        _iou = np.zeros((3,))
        _iou[0] = iou(gt, crop)
        #_iou[1] = iou(gt2, crop)
        #_iou[2] = iou(gt3, crop)

        # get label
        if _iou.max() >= th:
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 1)
            label = 1
        else:
            cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 1)
            label = 0

        # crop area
        crop_area = img[y1:y2, x1:x2]

        # resize crop area
        crop_area = resize(crop_area, H_size, H_size)

        # get HOG feature
        _hog = HOG(crop_area)
        
        # store HOG feature and label
        db[i, :HOG_feature_N] = _hog.ravel()
        db[i, -1] = label

    return db


# sliding window
def sliding_window(img, nn, H_size=32, prob_th=0.7):
    # get shape
    H, W, _ = img.shape

    # base rectangle [h, w]
    recs = np.array(((42, 42), (56, 56), (70, 70)), dtype=np.float32)

    # detected region
    detects = np.ndarray((0, 5), dtype=np.float32)

    # sliding window
    for y in range(0, H, 4):
        for x in range(0, W, 4):
            for rec in recs:
                # get half size of ractangle
                dh = int(rec[0] // 2)
                dw = int(rec[1] // 2)

                # get left top x
                x1 = max(x - dw, 0)
                # get left top y
                x2 = min(x + dw, W)
                # get right bottom x
                y1 = max(y - dh, 0)
                # get right bottom y
                y2 = min(y + dh, H)

                # crop region
                region = img[max(y - dh, 0) : min(y + dh, H), max(x - dw, 0) : min(x + dw, W)]

                # resize crop region
                region = resize(region, H_size, H_size)

                # get HOG feature
                region_hog = HOG(region).ravel()

                # predict score using neural network
                score = nn.forward(region_hog)

                if score >= prob_th:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 1)
                    detects = np.vstack((detects, np.array((x1, y1, x2, y2, score))))

    print(detects)

    return img


# Read image
img = cv2.imread("imori_1.jpg").astype(np.float32)

# prepare gt bounding box
gt = np.array((47, 41, 129, 103), dtype=np.float32)

# get database
db = make_dataset(img, gt)


# train neural network
# get input feature dimension
input_dim = db.shape[1] - 1
# prepare train data X
train_x = db[:, :input_dim]
# prepare train data t
train_t = db[:, -1][..., None]

# prepare neural network
nn = NN(ind=input_dim, w=64, w2=64, lr=0.01)
# training
nn = train_nn(nn, train_x, train_t, iteration_N=10000)


# read detect target image
img2 = cv2.imread("imori_many.jpg")

# detection
out = sliding_window(img2, nn)


cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
