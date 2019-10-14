import cv2
import numpy as np
import matplotlib.pyplot as plt


# Nereset Neighbor interpolation
def nn_interpolate(img, ax=1, ay=1):
	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	y = np.arange(aH).repeat(aW).reshape(aW, -1)
	x = np.tile(np.arange(aW), (aH, 1))
	y = np.round(y / ay).astype(np.int)
	x = np.round(x / ax).astype(np.int)

	out = img[y,x]

	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# Nearest Neighbor
out = nn_interpolate(img, ax=1.5, ay=1.5)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
