import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori_dark.jpg").astype(np.float)
H, W, C = img.shape

# Trans [0, 255]
a, b = 0., 255.

vmin = img.min()
vmax = img.max()

out = img.copy()
out[out<a] = a
out[out>b] = b
out = (b-a) / (vmax - vmin) * (out - vmin) + a
out = out.astype(np.uint8)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("out_his.png")
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
