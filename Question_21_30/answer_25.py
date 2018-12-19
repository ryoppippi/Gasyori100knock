import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape


# Nearest Neighbor
a = 1.5
a_shape = (int(a*H), int(a*W), C)
out = np.zeros_like(a_shape)

y = np.arange(a_shape[0]).repeat(a_shape[1]).reshape(a_shape[1], -1)
x = np.tile(np.arange(a_shape[1]), (a_shape[0],1))
y = np.round(y / a).astype(np.int)
x = np.round(x / a).astype(np.int)

out = img[y,x]

out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
