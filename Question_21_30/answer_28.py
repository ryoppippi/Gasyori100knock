import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape


# Affine
a = 1.
b = 0.
c = 0.
d = 1.
tx = 30
ty = -30

y = np.arange(H).repeat(W).reshape(W, -1)
x = np.tile(np.arange(W), (H, 1))

out = np.zeros((H+1, W+1, C), dtype=np.float32)

x_new = a * x + b * y + tx
y_new = c * x + d * y + ty

x_new = np.minimum(np.maximum(x_new, 0), W).astype(np.int)
y_new = np.minimum(np.maximum(y_new, 0), H).astype(np.int)

out[y_new, x_new] = img[y, x]
out = out[:H, :W]
out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
