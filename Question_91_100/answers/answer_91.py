import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob


# K-means step1
def k_means_step1(img, Class=5):
	#  get shape
	H, W, C = img.shape

	# initiate random seed
	np.random.seed(0)

	# reshape
	img = np.reshape(img, (H * W, -1))

	# select one index randomly
	i = np.random.choice(np.arange(H * W), Class, replace=False)
	Cs = img[i].copy()

	print(Cs)

	clss = np.zeros((H * W), dtype=int)

	# each pixel
	for i in range(H * W):
		# get distance from base pixel
		dis = np.sqrt(np.sum((Cs - img[i]) ** 2, axis=1))
		# get argmin distance
		clss[i] = np.argmin(dis)

	# show
	out = np.reshape(clss, (H, W)) * 50
	out = out.astype(np.uint8)

	return out


# read image
img = cv2.imread("imori.jpg").astype(np.float32)

# K-means step2
out = k_means_step1(img)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
