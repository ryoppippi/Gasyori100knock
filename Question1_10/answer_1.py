import cv2

img = cv2.imread("assets/imori.jpg")
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.imwrite("out.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
