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

# emboss filter
def emboss_filter(img, K_size=3):
	H, W, C = img.shape

	# zero padding
	pad = K_size // 2
	out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
	tmp = out.copy()

	# emboss kernel
	K = [[-2., -1., 0.],[-1., 1., 1.], [0., 1., 2.]]

	# filtering
	for y in range(H):
		for x in range(W):
			out[pad + y, pad + x] = np.sum(K * (tmp[y: y + K_size, x: x + K_size]))

	out = np.clip(out, 0, 255)
	out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float)

# grayscale
gray = BGR2GRAY(img)

# emboss filtering
out = emboss_filter(gray, K_size=3)


# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
