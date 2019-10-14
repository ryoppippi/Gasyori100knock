import cv2

# function: BGR -> RGB
def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # RGB > BGR
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img

# Read image
img = cv2.imread("imori.jpg")

# BGR -> RGB
img = BGR2RGB(img)

# Save result
cv2.imwrite("out.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
