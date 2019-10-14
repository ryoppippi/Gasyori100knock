import cv2
import numpy as np
import matplotlib.pyplot as plt


# histogram manipulation
def hist_mani(img, m0=128, s0=52):
	m = np.mean(img)
	s = np.std(img)

	out = img.copy()

	# normalize
	out = s0 / s * (out - m) + m0
	out[out < 0] = 0
	out[out > 255] = 255
	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori_dark.jpg").astype(np.float)

out = hist_mani(img)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.savefig("out_his.png")
plt.show()

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
