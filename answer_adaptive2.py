import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori2.jpg").astype(np.float32)
H, W, C = img.shape

# Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

# Magnitude and gradient
#gray = np.pad(gray, (1, 1), 'edge')
out = np.zeros_like(gray)

N = 9
D = N // 2
for y in range(H):
    for x in range(W):
        th = np.mean(gray[max(y-D,0):min(y+1+D,H), max(x-D,0):min(x+1+D,W)])
        out[y,x] = 255 if gray[y,x] > th else 0

out = out.astype(np.uint8)
        
# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
