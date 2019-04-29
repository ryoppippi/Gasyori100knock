import cv2
import numpy as np
import matplotlib.pyplot as plt


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
            gabor[y, x] = np.exp(-(_x**2 + g**2 * _y**2) / (2 * s**2)) * np.cos(2*np.pi*_x/l + p)

    gabor /= np.sum(np.abs(gabor))

    return gabor

As = [0, 45, 90, 135]

plt.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0.2)

for i, A in enumerate(As):
    gabor = gabor_f(A=A)
    out = gabor - np.min(gabor)
    out /= np.max(out)
    out *= 255
    out = out.astype(np.uint8)
    plt.subplot(1, 4, i+1)
    plt.imshow(out, cmap='gray')
    plt.axis('off')
    plt.title("Angle "+str(A))

plt.savefig("out.png")
plt.show()
