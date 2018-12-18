import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float) / 255.
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB > HSV
out = np.zeros_like(img)

max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy()
min_arg = np.argmin(img, axis=2)

H = np.zeros_like(max_v)

for num, i in enumerate(range(0, 2, 1)):
    ind = np.where(min_arg == i)
    _ind = np.where((max_v[ind] - min_v[ind]) == 0)
    H[ind][_ind] = 0
    _ind = np.where((max_v[ind] - min_v[ind]) > 0)
    H[ind][_ind] = 60. * (img[..., ((i+1)%3)][ind][_ind] - img[..., ((i+2)%3)][ind][_ind]) / (max_v[ind] - min_v[ind])[_ind] + 60. * (2*num+1)

V = max_v.copy()
S = max_v.copy() - min_v.copy()

# Transpose Hue
H += 180 % 360

# HSV > RGB

C = S
H_ = H / 60
X = C * (1 - np.abs( H_ % 2 - 1))
Z = np.zeros_like(H)

vals = [[Z,X,C], [Z,C,X], [X,C,Z], [C,X,Z], [C,Z,X], [X,Z,C]]

for i in range(6):
    ind = np.where((i <= H_) & (H_ < (i+1)))
    out[..., 0][ind] = (V-C)[ind] + vals[i][0][ind]
    out[..., 1][ind] = (V-C)[ind] + vals[i][1][ind]
    out[..., 2][ind] = (V-C)[ind] + vals[i][2][ind]

out[np.where(max_v == min_v)] = 0
out = (out * 255).astype(np.uint8) 

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
