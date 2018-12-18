import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape

# Dicrease color
out = img.copy()

for i in range(4):
    ind = np.where(((64*i-1) <= out) & (out < (64*(i+1)-1)))
    out[ind] = 32 * (2*i+1)

# Display histogram
plt.hist(img.ravel(), rwidth=0.8)

plt.subplots()
plt.hist(out.ravel(), rwidth=0.8)
plt.show()
