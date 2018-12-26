import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# RGB > YCbCr
Y = 0.2990 * img[..., 2] + 0.5870 * img[..., 1] + 0.1140 * img[..., 0]
Cb = -0.1687 * img[..., 2] - 0.3313 * img[..., 1] + 0.5 * img[..., 0] + 128.
Cr = 0.5 * img[..., 2] - 0.4187 * img[..., 1] - 0.0813 * img[..., 0] + 128.

Y *= 0.7

# YCbCr > RGB
out = np.zeros_like(img, dtype=np.float32)
out[..., 2] = Y + (Cr - 128.) * 1.4020
out[..., 1] = Y - (Cb - 128.) * 0.3441 - (Cr - 128.) * 0.7139
out[..., 0] = Y + (Cb - 128.) * 1.7718

out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
