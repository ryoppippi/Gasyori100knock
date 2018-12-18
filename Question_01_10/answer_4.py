import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

h, w, c = img.shape

# Grayscale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = out[np.where(out < _t)[0]]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (h * w)
    v1 = out[np.where(out >= _t)[0]]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (h * w)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

# Binarization
print("threshold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
