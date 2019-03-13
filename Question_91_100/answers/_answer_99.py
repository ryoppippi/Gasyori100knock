import cv2
import numpy as np

np.random.seed(0)

# read image
img = cv2.imread("imori_1.jpg")
H, W, C = img.shape

# Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

gt = np.array((47, 41, 129, 103), dtype=np.float32)

cv2.rectangle(img, (gt[0], gt[1]), (gt[2], gt[3]), (0,255,255), 1)

def iou(a, b):
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    iou_x1 = np.maximum(a[0], b[0])
    iou_y1 = np.maximum(a[1], b[1])
    iou_x2 = np.minimum(a[2], b[2])
    iou_y2 = np.minimum(a[3], b[3])
    iou_w = max(iou_x2 - iou_x1, 0)
    iou_h = max(iou_y2 - iou_y1, 0)
    area_iou = iou_w * iou_h
    iou = area_iou / (area_a + area_b - area_iou)
    return iou


def hog(gray):
    h, w = gray.shape
    # Magnitude and gradient
    gray = np.pad(gray, (1, 1), 'edge')

    gx = gray[1:h+1, 2:] - gray[1:h+1, :w]
    gy = gray[2:, 1:w+1] - gray[:h, 1:w+1]
    gx[gx == 0] = 0.000001

    mag = np.sqrt(gx ** 2 + gy ** 2)
    gra = np.arctan(gy / gx)
    gra[gra<0] = np.pi / 2 + gra[gra < 0] + np.pi / 2

    # Gradient histogram
    gra_n = np.zeros_like(gra, dtype=np.int)

    d = np.pi / 9
    for i in range(9):
        gra_n[np.where((gra >= d * i) & (gra <= d * (i+1)))] = i

    N = 8
    HH = h // N
    HW = w // N
    Hist = np.zeros((HH, HW, 9), dtype=np.float32)
    for y in range(HH):
        for x in range(HW):
            for j in range(N):
                for i in range(N):
                    Hist[y, x, gra_n[y*4+j, x*4+i]] += mag[y*4+j, x*4+i]
                
    ## Normalization
    C = 3
    eps = 1
    for y in range(HH):
        for x in range(HW):
            #for i in range(9):
            Hist[y, x] /= np.sqrt(np.sum(Hist[max(y-1,0):min(y+2, HH), max(x-1,0):min(x+2, HW)] ** 2) + eps)

    return Hist

def resize(img, h, w):
    _h, _w  = img.shape
    ah = 1. * h / _h
    aw = 1. * w / _w
    y = np.arange(h).repeat(w).reshape(w, -1)
    x = np.tile(np.arange(w), (h, 1))
    y = (y / ah)
    x = (x / aw)

    ix = np.floor(x).astype(np.int32)
    iy = np.floor(y).astype(np.int32)
    ix = np.minimum(ix, _w-2)
    iy = np.minimum(iy, _h-2)

    dx = x - ix
    dy = y - iy
    
    out = (1-dx) * (1-dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix+1] + (1 - dx) * dy * img[iy+1, ix] + dx * dy * img[iy+1, ix+1]
    out[out>255] = 255

    return out


class NN:
    def __init__(self, ind=2, w=64, w2=64, outd=1, lr=0.1):
        self.w2 = np.random.randn(ind, w)
        self.b2 = np.random.randn(w)
        self.w3 = np.random.randn(w, w2)
        self.b3 = np.random.randn(w2)
        self.wout = np.random.randn(w2, outd)
        self.bout = np.random.randn(outd)
        self.lr = lr

    def forward(self, x):
        self.z1 = x
        self.z2 = self.sigmoid(np.dot(self.z1, self.w2) + self.b2)
        self.z3 = self.sigmoid(np.dot(self.z2, self.w3) + self.b3)
        self.out = self.sigmoid(np.dot(self.z3, self.wout) + self.bout)
        return self.out

    def train(self, x, t):
        # backpropagation output layer
        out_d = 2*(self.out - t) * self.out * (1 - self.out)
        out_dW = np.dot(self.z3.T, out_d)
        out_dB = np.dot(np.ones([1, out_d.shape[0]]), out_d)
        self.wout -= self.lr * out_dW
        self.bout -= self.lr * out_dB[0]

        w3_d = np.dot(out_d, self.wout.T) * self.z3 * (1 - self.z3)
        w3_dW = np.dot(self.z2.T, w3_d)
        w3_dB = np.dot(np.ones([1, w3_d.shape[0]]), w3_d)
        self.w3 -= self.lr * w3_dW
        self.b3 -= self.lr * w3_dB[0]
        
        # backpropagation inter layer
        w2_d = np.dot(w3_d, self.w3.T) * self.z2 * (1 - self.z2)
        w2_dW = np.dot(self.z1.T, w2_d)
        w2_dB = np.dot(np.ones([1, w2_d.shape[0]]), w2_d)
        self.w2 -= self.lr * w2_dW
        self.b2 -= self.lr * w2_dB[0]

    def sigmoid(self, x):
        return 1. / (1. + np.exp(-x))

# crop and create database

Crop_num = 200
L = 60
H_size = 32
F_n = ((H_size // 8) ** 2) * 9

db = np.zeros((Crop_num, F_n+1))

for i in range(Crop_num):
    x1 = np.random.randint(W-L)
    y1 = np.random.randint(H-L)
    x2 = x1 + L
    y2 = y1 + L
    crop = np.array((x1, y1, x2, y2))

    _iou = iou(gt, crop)

    if _iou >= 0.5:
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 1)
        label = 1
    else:
        cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 1)
        label = 0

    crop_area = gray[y1:y2, x1:x2]
    crop_area = resize(crop_area, H_size, H_size)
    _hog = hog(crop_area)
    
    db[i, :F_n] = _hog.ravel()
    db[i, -1] = label


## training neural network
nn = NN(ind=F_n, lr=0.01)
for i in range(10000):
    nn.forward(db[:, :F_n])
    nn.train(db[:, :F_n], db[:, -1][..., None])


# read detect target image
img2 = cv2.imread("imori_many.jpg")
H2, W2, C2 = img2.shape

# Grayscale
gray2 = 0.2126 * img2[..., 2] + 0.7152 * img2[..., 1] + 0.0722 * img2[..., 0]

# [h, w]
recs = np.array(((42, 42), (56, 56), (70, 70)), dtype=np.float32)

detects = np.ndarray((0, 5), dtype=np.float32)

# sliding window
for y in range(0, H2, 4):
    for x in range(0, W2, 4):
        for rec in recs:
            dh = int(rec[0] // 2)
            dw = int(rec[1] // 2)
            x1 = max(x-dw, 0)
            x2 = min(x+dw, W2)
            y1 = max(y-dh, 0)
            y2 = min(y+dh, H2)
            region = gray2[max(y-dh,0):min(y+dh,H2), max(x-dw,0):min(x+dw,W2)]
            region = resize(region, H_size, H_size)
            region_hog = hog(region).ravel()

            score = nn.forward(region_hog)
            if score >= 0.7:
                #cv2.rectangle(img2, (x1, y1), (x2, y2), (0,0,255), 1)
                detects = np.vstack((detects, np.array((x1, y1, x2, y2, score))))


# Non-maximum suppression
def nms(_bboxes, iou_th=0.5, select_num=None, prob_th=None):
    #
    # Non Maximum Suppression
    #
    # Argument
    #  bboxes(Nx5) ... [bbox-num, 5(leftTopX,leftTopY,w,h, score)]
    #  iou_th([float]) ... threshold for iou between bboxes.
    #  select_num([int]) ... max number for choice bboxes. If None, this is unvalid.
    #  prob_th([float]) ... probability threshold to choice. If None, this is unvalid.
    # Return
    #  inds ... choced indices for bboxes
    #

    bboxes = _bboxes.copy()
    
    bboxes[:, 2] = bboxes[:, 2] - bboxes[:, 0]
    bboxes[:, 3] = bboxes[:, 3] - bboxes[:, 1]
    
    # Sort by bbox's score. High -> Low
    sort_inds = np.argsort(bboxes[:, -1])[::-1]

    processed_bbox_ind = []
    return_inds = []

    unselected_inds = sort_inds.copy()
    
    while len(unselected_inds) > 0:
        process_bboxes = bboxes[unselected_inds]
        argmax_score_ind = np.argmax(process_bboxes[::, -1])
        max_score_ind = unselected_inds[argmax_score_ind]
        return_inds += [max_score_ind]
        unselected_inds = np.delete(unselected_inds, argmax_score_ind)

        base_bbox = bboxes[max_score_ind]
        compare_bboxes = bboxes[unselected_inds]
        
        base_x1 = base_bbox[0]
        base_y1 = base_bbox[1]
        base_x2 = base_bbox[2] + base_x1
        base_y2 = base_bbox[3] + base_y1
        base_w = np.maximum(base_bbox[2], 0)
        base_h = np.maximum(base_bbox[3], 0)
        base_area = base_w * base_h

        # compute iou-area between base bbox and other bboxes
        iou_x1 = np.maximum(base_x1, compare_bboxes[:, 0])
        iou_y1 = np.maximum(base_y1, compare_bboxes[:, 1])
        iou_x2 = np.minimum(base_x2, compare_bboxes[:, 2] + compare_bboxes[:, 0])
        iou_y2 = np.minimum(base_y2, compare_bboxes[:, 3] + compare_bboxes[:, 1])
        iou_w = np.maximum(iou_x2 - iou_x1, 0)
        iou_h = np.maximum(iou_y2 - iou_y1, 0)
        iou_area = iou_w * iou_h

        compare_w = np.maximum(compare_bboxes[:, 2], 0)
        compare_h = np.maximum(compare_bboxes[:, 3], 0)
        compare_area = compare_w * compare_h

        # bbox's index which iou ratio over threshold is excluded
        all_area = compare_area + base_area - iou_area
        iou_ratio = np.zeros((len(unselected_inds)))
        iou_ratio[all_area < 0.9] = 0.
        _ind = all_area >= 0.9
        iou_ratio[_ind] = iou_area[_ind] / all_area[_ind]
        
        unselected_inds = np.delete(unselected_inds, np.where(iou_ratio >= iou_th)[0])

    if prob_th is not None:
        preds = bboxes[return_inds][:, -1]
        return_inds = np.array(return_inds)[np.where(preds >= prob_th)[0]].tolist()
        
    # pick bbox's index by defined number with higher score
    if select_num is not None:
        return_inds = return_inds[:select_num]

    return return_inds


detects = detects[nms(detects, iou_th=0.25)]

for d in detects:
    v = list(map(int, d[:4]))
    cv2.rectangle(img2, (v[0], v[1]), (v[2], v[3]), (0,0,255), 1)
    cv2.putText(img2, "{:.2f}".format(d[-1]), (v[0], v[1]+9),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,0,255), 1)

cv2.imwrite("out.jpg", img2)
cv2.imshow("result", img2)
cv2.waitKey(0)
