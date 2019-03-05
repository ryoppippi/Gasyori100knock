import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Otsu binary
## Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
gray = gray.astype(np.uint8)

# Gabor
def gabor_f(k=111, s=10, g=1.2, l=10, p=0, A=0):
    d = k // 2

    gabor = np.zeros((k, k), dtype=np.float32)
    
    for y in range(k):
        for x in range(k):
            px = x - d
            py = y - d
            theta = A / 180. * np.pi
            _x = np.cos(theta) * px + np.sin(theta) * py
            _y = -np.sin(theta) * px + np.cos(theta) * py
            gabor[x, y] = np.exp(-(_x**2 + g**2 * _y**2) / (2 * s**2)) * np.cos(2*np.pi*_x/l + p)

    gabor /= np.sum(np.abs(gabor))

    return gabor

K_size = 11
Sigma = 1.5
Gamma = 1.2
Lambda = 3.
Psi = 0.

gray = np.pad(gray, (K_size//2, K_size//2), 'edge')

As = [0, 45, 90, 135]

gs = []

plt.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0.2)

for i, A in enumerate(As):
    gabor = gabor_f(k=K_size, s=Sigma, g=Gamma, l=Lambda, p=Psi, A=A)

    out = np.zeros((H, W), dtype=np.float32)
    
    for y in range(H):
        for x in range(W):
            out[y, x] = np.sum(gray[y:y+K_size, x:x+K_size] * gabor)

    out[out < 0] = 0
    out[out > 255] = 255
    
    gs.append(out)


out = np.zeros((H, W), dtype=np.float32)
for g in gs:
    out += g

    
out = out / out.max() * 255
out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)

