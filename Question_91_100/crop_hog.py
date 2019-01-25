import cv2
import numpy as np

np.random.seed(0)

# read image
img = cv2.imread("imori_1.jpg")
H, W, C = img.shape

# Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

gt = np.array((47, 41, 129, 103), dtype=np.float32)

#gt = np.array((41, 3, 83, 32), dtype=np.float32)
#gt2 = np.array((123, 41, 161, 74), dtype=np.float32)
#gt3 = np.array((97, 83, 137, 113), dtype=np.float32)
cv2.rectangle(img, (gt[0], gt[1]), (gt[2], gt[3]), (0,255,255), 1)
#cv2.rectangle(img, (gt2[0], gt2[1]), (gt2[2], gt2[3]), (0,255,255), 1)
#cv2.rectangle(img, (gt3[0], gt3[1]), (gt3[2], gt3[3]), (0,255,255), 1)

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


# crop and create database

Crop_num = 300
L = 60

H_size = 32
F_n = ((H_size // 8) ** 2) * 9

db = np.zeros((Crop_num, F_n + 1))

for i in range(Crop_num):
    x1 = np.random.randint(W-L)
    y1 = np.random.randint(H-L)
    x2 = x1 + L
    y2 = y1 + L
    crop = np.array((x1, y1, x2, y2))

    _iou = np.zeros((3,))
    _iou[0] = iou(gt, crop)
    #_iou[1] = iou(gt2, crop)
    #_iou[2] = iou(gt3, crop)

    if _iou.max() >= 0.5:
        cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,255), 1)
        label = 0
    else:
        cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 1)
        label = 1

    crop_area = gray[y1:y2, x1:x2]
    crop_area = resize(crop_area, H_size, H_size)
    _hog = hog(crop_area)
    
    db[i, :F_n] = _hog.ravel()
    db[i, -1] = label

    #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0,0), 1)
    
cv2.imshow("re", img)
cv2.waitKey(0)

from sklearn import svm
clf = svm.SVC(kernel='linear')
clf.fit(X=db[..., :F_n], y=db[..., -1])


# read detect target image
img2 = cv2.imread("imori_many.jpg")
H2, W2, C2 = img2.shape

# Grayscale
gray2 = 0.2126 * img2[..., 2] + 0.7152 * img2[..., 1] + 0.0722 * img2[..., 0]

# [h, w]
recs = np.array(((42, 42), (56, 56), (70, 70)), dtype=np.float32)

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
            r_hog = hog(region).ravel()

            f_dif = np.sum(np.abs(db[:, :F_n] - r_hog) ** 2)
            min_arg = np.argsort(f_dif)[:5]
            pred = db[min_arg, -1]

            #if len(np.where(pred==0)[0]) > 0:
            #    cv2.rectangle(img2, (x1, y1), (x2, y2), (0,0,255), 1)
            
            pred = clf.predict(r_hog[None, ...])[0]
            if pred == 0:
                cv2.rectangle(img2, (x1, y1), (x2, y2), (0,0,255), 1)
    print(y, x)

                
#print(db)
cv2.imshow("", img2)
cv2.waitKey(0)
