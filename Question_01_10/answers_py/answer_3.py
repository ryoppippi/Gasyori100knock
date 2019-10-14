import cv2
import numpy as np

# Gray scale
def BGR2GRAY(img):
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()

	# Gray scale
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(np.uint8)

	return out

# binalization
def binarization(img, th=128):
	img[img < th] = 0
	img[img >= th] = 255
	return img
	

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# Grayscale
out = BGR2GRAY(img)

# Binarization
out = binarization(out)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
