import cv2
import numpy as np
import matplotlib.pyplot as plt

def Canny_step1(img):

	# Gray scale
	def BGR2GRAY(img):
		b = img[:, :, 0].copy()
		g = img[:, :, 1].copy()
		r = img[:, :, 2].copy()

		# Gray scale
		out = 0.2126 * r + 0.7152 * g + 0.0722 * b
		out = out.astype(np.uint8)

		return out


	# Gaussian filter for grayscale
	def gaussian_filter(img, K_size=3, sigma=1.3):

		if len(img.shape) == 3:
			H, W, C = img.shape
		else:
			img = np.expand_dims(img, axis=-1)
			H, W, C = img.shape

		## Zero padding
		pad = K_size // 2
		out = np.zeros([H + pad * 2, W + pad * 2, C], dtype=np.float)
		out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)

		## prepare Kernel
		K = np.zeros((K_size, K_size), dtype=np.float)
		for x in range(-pad, -pad + K_size):
			for y in range(-pad, -pad + K_size):
				K[y+pad, x+pad] = np.exp( -(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
		K /= (sigma * np.sqrt(2 * np.pi))
		K /= K.sum()

		tmp = out.copy()

		# filtering
		for y in range(H):
			for x in range(W):
				for c in range(C):
					out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

		out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

		return out


	# sobel filter
	def sobel_filter(img, K_size=3):
		if len(img.shape) == 3:
			H, W, C = img.shape
		else:
			img = np.expand_dims(img, axis=-1)
			H, W, C = img.shape

		# Zero padding
		pad = K_size // 2
		out = np.zeros((H + pad * 2, W + pad * 2), dtype=np.float)
		out[pad: pad + H, pad: pad + W] = gray.copy().astype(np.float)
		tmp = out.copy()

		out_v = out.copy()
		out_h = out.copy()

		## Sobel vertical
		Kv = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]
		## Sobel horizontal
		Kh = [[1., 0., -1.],[2., 0., -2.],[1., 0., -1.]]

		# filtering
		for y in range(H):
			for x in range(W):
				out_v[pad + y, pad + x] = np.sum(Kv * (tmp[y: y + K_size, x: x + K_size]))
				out_h[pad + y, pad + x] = np.sum(Kh * (tmp[y: y + K_size, x: x + K_size]))

		out_v = np.clip(out_v, 0, 255)
		out_h = np.clip(out_h, 0, 255)

		out_v = out_v[pad: pad + H, pad: pad + W].astype(np.uint8)
		out_h = out_h[pad: pad + H, pad: pad + W].astype(np.uint8)

		return out_v, out_h


	def get_edge_tan(fx, fy):
		# get edge strength
		edge = np.sqrt(np.power(fx, 2) + np.power(fy, 2))
		fx = np.maximum(fx, 1e-5)

		# get edge angle
		tan = np.arctan(fy / fx)

		return edge, tan


	def angle_quantization(tan):
		angle = np.zeros_like(tan, dtype=np.uint8)
		angle[np.where((tan > -0.4142) & (tan <= 0.4142))] = 0
		angle[np.where((tan > 0.4142) & (tan < 2.4142))] = 45
		angle[np.where((tan >= 2.4142) | (tan <= -2.4142))] = 95
		angle[np.where((tan > -2.4142) & (tan <= -0.4142))] = 135

		return angle

	# grayscale
	gray = BGR2GRAY(img)

	# gaussian filtering
	gaussian = gaussian_filter(gray, K_size=5, sigma=1.4)

	# sobel filtering
	fy, fx = sobel_filter(gaussian, K_size=3)

	# get edge strength, angle
	edge, tan = get_edge_tan(fx, fy)

	# angle quantization
	angle = angle_quantization(tan)

	return angle


# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# Canny (step1)
angle = Canny_step1(img)

out = angle.astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
