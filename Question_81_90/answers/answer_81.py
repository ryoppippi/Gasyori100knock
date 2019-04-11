import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("thorino.jpg").astype(np.float32)
H, W, C = img.shape

## Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
gray = gray.astype(np.uint8)

## Sobel
sobely = np.array(((1, 2, 1),
                   (0, 0, 0),
                   (-1, -2, -1)), dtype=np.float32)

sobelx = np.array(((1, 0, -1),
                   (2, 0, -2),
                   (1, 0, -1)), dtype=np.float32)

tmp = np.pad(gray, (1, 1), 'edge')

Ix = np.zeros_like(gray, dtype=np.float32)
Iy = np.zeros_like(gray, dtype=np.float32)

for y in range(H):
    for x in range(W):
        Ix[y, x] = np.mean(tmp[y:y+3, x:x+3] * sobelx)
        Iy[y, x] = np.mean(tmp[y:y+3, x:x+3] * sobely)
     
tmp = np.pad(Ix, (1, 1), 'edge')

Ix2 = np.zeros_like(gray, dtype=np.float32)
IxIy = np.zeros_like(gray, dtype=np.float32)

for y in range(H):
    for x in range(W):
        Ix2[y, x] = np.mean(tmp[y:y+3, x:x+3] * sobelx)
        IxIy[y, x] = np.mean(tmp[y:y+3, x:x+3] * sobely)

tmp = np.pad(Iy, (1, 1), 'edge')

Iy2 = np.zeros_like(gray, dtype=np.float32)

for y in range(H):
    for x in range(W):
        Iy2[y, x] = np.mean(tmp[y:y+3, x:x+3] * sobely)

out = np.array((gray, gray, gray))
out = np.transpose(out, (1,2,0))

## Hessian
Hes = np.zeros((H, W))

for y in range(H):
    for x in range(W):
        Hes[y,x] = Ix2[y,x] * Iy2[y,x] - IxIy[y,x] ** 2

## Detect Corner
for y in range(H):
    for x in range(W):
        if Hes[y,x] == np.max(Hes[max(y-1,0):min(y+2,H), max(x-1,0):min(x+2,W)]) and Hes[y,x] > np.max(Hes)*0.1:
            out[y, x] = [0, 0, 255]

out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
