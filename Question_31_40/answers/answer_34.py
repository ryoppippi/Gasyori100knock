import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Gray scale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

# DFT
K = W
L = H
M = W
N = H

G = np.zeros((L, K), dtype=np.complex)

x = np.tile(np.arange(W), (H, 1))
y = np.arange(H).repeat(W).reshape(H, -1)

for l in range(L):
    for k in range(K):
        G[l, k] = np.sum(gray * np.exp(-2j * np.pi * (x * k / M + y * l / N))) / np.sqrt(M * N)

# low-pass filter
_G = np.zeros_like(G)
_G[:H//2, :W//2] = G[H//2:, W//2:]
_G[:H//2, W//2:] = G[H//2:, :W//2]
_G[H//2:, :W//2] = G[:H//2, W//2:]
_G[H//2:, W//2:] = G[:H//2, :W//2]
p = 0.2
_x = x - W // 2
_y = y - H // 2
r = np.sqrt(_x ** 2 + _y ** 2)
mask = np.ones((H, W), dtype=np.float32)
mask[r<(W//2*p)] = 0

_G *= mask

G[:H//2, :W//2] = _G[H//2:, W//2:]
G[:H//2, W//2:] = _G[H//2:, :W//2]
G[H//2:, :W//2] = _G[:H//2, W//2:]
G[H//2:, W//2:] = _G[:H//2, :W//2]

# IDFT
out = np.zeros((H, W), dtype=np.float32)

for n in range(N):
    for m in range(M):
        out[n,m] = np.abs(np.sum(G * np.exp(2j * np.pi * (x * m / M + y * n / N)))) / np.sqrt(M * N)

out[out>255] = 255
out = out.astype(np.uint8)
    
# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
