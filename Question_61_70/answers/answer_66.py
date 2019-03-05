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

# Draw
_mag = (mag / mag.max() * 255).astype(np.uint8)

cv2.imwrite("out_mag.jpg", _mag)

# Save result
out = np.zeros((H, W, 3), dtype=np.uint8)
C = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255],
     [127, 127, 0], [127, 0, 127], [0, 127, 127]]
for i in range(9):
    out[gra_n == i] = C[i]

cv2.imwrite("out_gra.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
