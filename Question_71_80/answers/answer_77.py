import cv2
import numpy as np
import matplotlib.pyplot as plt

# Gabor
K_size = 111
Sigma = 10
Gamma = 1.2
Lambda = 10.
Psi = 0.
angle = 0

d = K_size // 2

gabor = np.zeros((K_size, K_size), dtype=np.float32)

for y in range(K_size):
    for x in range(K_size):
        px = x - d
        py = y - d
        theta = angle / 180. * np.pi
        _x = np.cos(theta) * px + np.sin(theta) * py
        _y = -np.sin(theta) * px + np.cos(theta) * py
        gabor[x, y] = np.exp(-(_x**2 + Gamma**2 * _y**2) / (2 * Sigma**2)) * np.cos(2*np.pi*_x/Lambda + Psi)

gabor /= np.sum(np.abs(gabor))

# Visualize
out = gabor - np.min(gabor)
out /= np.max(out)
out *= 255
out = out.astype(np.uint8)
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
