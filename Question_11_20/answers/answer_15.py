import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
H, W, C = img.shape

b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray scale
gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
gray = gray.astype(np.uint8)

# sobel Filter
K_size = 3

## Zero padding
pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2), dtype=np.float)
out[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float)
tmp = out.copy()

## Sobel vertical
K = [[1., 0., -1.],[2., 0., -2.],[1., 0., -1.]]
## Sobel horizontal
#K = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]

for y in range(H):
    for x in range(W):
        out[pad+y, pad+x] = np.sum(K * (tmp[y:y+K_size, x:x+K_size]))

out[out < 0] = 0
out[out > 255] = 255

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
