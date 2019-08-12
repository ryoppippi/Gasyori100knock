import cv2
import numpy as np
import matplotlib.pyplot as plt


# gamma correction
def gamma_correction(img, c=1, g=2.2):
	out = img.copy()
	out /= 255.
	out = (1/c * out) ** (1/g)

	out *= 255
	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori_gamma.jpg").astype(np.float)

# Gammma correction
out = gamma_correction(img)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
