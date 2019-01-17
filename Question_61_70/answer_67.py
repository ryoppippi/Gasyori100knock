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
                

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(Hist[..., i])
    plt.axis('off')
    plt.xticks(color="None")
    plt.yticks(color="None")
plt.savefig("out.png")
plt.show()

