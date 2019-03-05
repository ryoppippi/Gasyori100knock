import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Dicrease color
out = img.copy()

out = out // 64 * 64 + 32

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
