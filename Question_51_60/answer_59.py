import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("seg.png").astype(np.float32)
H, W, C = img.shape

label = np.zeros((H, W), dtype=np.int)
label[img[..., 0]>0] = 1

LUT = [0 for _ in range(H*W)]

n = 1

for y in range(H):
    for x in range(W):
        if label[y, x] == 0:
            continue
        c2 = label[max(y-1,0), min(x+1, W-1)]
        c3 = label[max(y-1,0), x]
        c4 = label[max(y-1,0), max(x-1,0)]
        c5 = label[y, max(x-1,0)]
        if c3 < 2 and c5 < 2 and c2 < 2 and c4 < 2:
            n += 1
            label[y, x] = n
        else:
            _vs = [c3, c5, c2, c4]
            vs = [a for a in _vs if a > 1]
            v = min(vs)
            label[y, x] = v

            minv = v
            for _v in vs:
                if LUT[_v] != 0:
                    minv = min(minv, LUT[_v])
            for _v in vs:
                LUT[_v] = minv
                
count = 1

for l in range(2, n+1):
    flag = True
    for i in range(n+1):
        if LUT[i] == l:
            if flag:
                count += 1
                flag = False
            LUT[i] = count

COLORS = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 0]]
out = np.zeros((H, W, C), dtype=np.uint8)

for i, lut in enumerate(LUT[2:]):
    out[label == (i+2)] = COLORS[lut-2]
    
# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
