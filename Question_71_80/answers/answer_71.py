import cv2
import numpy as np
import matplotlib.pyplot as plt

# BGR -> HSV
def BGR2HSV(_img):
	img = _img.copy() / 255.

	hsv = np.zeros_like(img, dtype=np.float32)

	# get max and min
	max_v = np.max(img, axis=2).copy()
	min_v = np.min(img, axis=2).copy()
	min_arg = np.argmin(img, axis=2)

	# H
	hsv[..., 0][np.where(max_v == min_v)]= 0
	## if min == B
	ind = np.where(min_arg == 0)
	hsv[..., 0][ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
	## if min == R
	ind = np.where(min_arg == 2)
	hsv[..., 0][ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
	## if min == G
	ind = np.where(min_arg == 1)
	hsv[..., 0][ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
		
	# S
	hsv[..., 1] = max_v.copy() - min_v.copy()

	# V
	hsv[..., 2] = max_v.copy()
	
	return hsv

# make mask
def get_mask(hsv):
	mask = np.zeros_like(hsv[..., 0])
	#mask[np.where((hsv > 180) & (hsv[0] < 260))] = 255
	mask[np.logical_and((hsv[..., 0] > 180), (hsv[..., 0] < 260))] = 1
	return mask

# masking
def masking(img, mask):
	mask = 1 - mask
	out = img.copy()
	# mask [h, w] -> [h, w, channel]
	mask = np.tile(mask, [3, 1, 1]).transpose([1, 2, 0])
	out *= mask

	return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# RGB > HSV
hsv = BGR2HSV(img / 255.)

# color tracking
mask = get_mask(hsv)

# masking
out = masking(img, mask)

out = out.astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
