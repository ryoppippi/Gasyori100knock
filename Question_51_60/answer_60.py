import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

img2 = cv2.imread("thorino.jpg").astype(np.float32)

a = 0.6
out = img * a + img2 * (1 - a)
out = out.astype(np.uint8)
    
# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
