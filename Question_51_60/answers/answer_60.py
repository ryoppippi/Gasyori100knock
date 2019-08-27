import cv2
import numpy as np
import matplotlib.pyplot as plt


# alpha blend
def alpha_blend(img1, img2, alpha):
	# blend
	out = img * alpha + img2 * (1 - alpha)
	out = out.astype(np.uint8)
	return out

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# Read blend target image
img2 = cv2.imread("thorino.jpg").astype(np.float32)

out = alpha_blend(img, img2, alpha=0.6)
    
# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
