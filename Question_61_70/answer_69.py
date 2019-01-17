import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

# Magnitude and gradient
gray = np.pad(gray, (1, 1), 'edge')

gx = gray[1:H+1, 2:] - gray[1:H+1, :W]
gy = gray[2:, 1:W+1] - gray[:H, 1:W+1]
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
HH = H // N
HW = W // N
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
        
## Draw
out = gray[1:H+1, 1:W+1].copy().astype(np.uint8)

for y in range(HH):
    for x in range(HW):
        cx = x * N + N // 2
        cy = y * N + N // 2
        x1 = cx + N // 2 - 1
        y1 = cy
        x2 = cx - N // 2 + 1
        y2 = cy

        h = Hist[y, x] / np.sum(Hist[y, x])
        h /= h.max()
        
        for c in range(9):
            #angle = (20 * c + 10 - 90) / 180. * np.pi
            angle = (20 * c + 10) / 180. * np.pi
            rx = int(np.sin(angle) * (x1 - cx) + np.cos(angle) * (y1 - cy) + cx)
            ry = int(np.cos(angle) * (x1 - cx) - np.cos(angle) * (y1 - cy) + cy)
            lx = int(np.sin(angle) * (x2 - cx) + np.cos(angle) * (y2 - cy) + cx)
            ly = int(np.cos(angle) * (x2 - cx) - np.cos(angle) * (y2 - cy) + cy)
        
            c = int(255. * h[c])
            cv2.line(out, (lx, ly), (rx, ry), (c, c, c), thickness=1)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
