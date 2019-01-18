import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# Display histogram
plt.hist(img.ravel(), bins=128, rwidth=0.8, range=(0, 255))
plt.show()
