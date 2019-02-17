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

out_v = out.copy()
out_h = out.copy()

## Sobel vertical
Kv = [[0., -1., 0.],[0., 1., 0.],[0., 0., 0.]]
## Sobel horizontal
Kh = [[0., 0., 0.],[-1., 1., 0.], [0., 0., 0.]]

for y in range(H):
    for x in range(W):
        out_v[pad+y, pad+x] = np.sum(Kv * (tmp[y:y+K_size, x:x+K_size]))
        out_h[pad+y, pad+x] = np.sum(Kh * (tmp[y:y+K_size, x:x+K_size]))

#out_v = np.abs(out_v)
#out_h = np.abs(out_h)
out_v[out_v < 0] = 0
out_h[out_h < 0] = 0
out_v[out_v > 255] = 255
out_h[out_h > 255] = 255

out_v = out_v[pad:pad+H, pad:pad+W].astype(np.uint8)
out_h = out_h[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out_v.jpg", out_v)
cv2.imshow("result", out_v)
cv2.waitKey(0)

cv2.imwrite("out_h.jpg", out_h)
cv2.imshow("result", out_h)
cv2.waitKey(0)
cv2.destroyAllWindows()
