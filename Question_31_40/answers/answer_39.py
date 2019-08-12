import cv2
import numpy as np
import matplotlib.pyplot as plt

channel = 3

# BGR -> Y Cb Cr
def BGR2YCbCr(img):
  H, W, _ = img.shape

  ycbcr = np.zeros([H, W, 3], dtype=np.float32)

  ycbcr[..., 0] = 0.2990 * img[..., 2] + 0.5870 * img[..., 1] + 0.1140 * img[..., 0]
  ycbcr[..., 1] = -0.1687 * img[..., 2] - 0.3313 * img[..., 1] + 0.5 * img[..., 0] + 128.
  ycbcr[..., 2] = 0.5 * img[..., 2] - 0.4187 * img[..., 1] - 0.0813 * img[..., 0] + 128.

  return ycbcr

# Y Cb Cr -> BGR
def YCbCr2BGR(ycbcr):
  H, W, _ = ycbcr.shape

  out = np.zeros([H, W, channel], dtype=np.float32)
  out[..., 2] = ycbcr[..., 0] + (ycbcr[..., 2] - 128.) * 1.4020
  out[..., 1] = ycbcr[..., 0] - (ycbcr[..., 1] - 128.) * 0.3441 - (ycbcr[..., 2] - 128.) * 0.7139
  out[..., 0] = ycbcr[..., 0] + (ycbcr[..., 1] - 128.) * 1.7718

  out = np.clip(out, 0, 255)
  out = out.astype(np.uint8)

  return out


# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# bgr -> Y Cb Cr
ycbcr = BGR2YCbCr(img)

# process
ycbcr[..., 0] *= 0.7

# YCbCr > RGB
out = YCbCr2BGR(ycbcr)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
