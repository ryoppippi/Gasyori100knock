import cv2
import numpy as np
import matplotlib.pyplot as plt

# histogram equalization
def hist_equal(img, z_max=255):
	H, W, C = img.shape
	S = H * W * C * 1.

	out = img.copy()

	sum_h = 0.

	for i in range(1, 255):
		ind = np.where(img == i)
		sum_h += len(img[ind])
		z_prime = z_max / S * sum_h
		out[ind] = z_prime

	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# histogram normalization
out = hist_equal(img)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("out_his.png")
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
