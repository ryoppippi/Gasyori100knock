import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# k-Means
Class = 5

np.random.seed(0)

img = np.reshape(img, (H*W, -1))

i = np.random.choice(np.arange(H*W), Class, replace=False)
Cs = img[i].copy()

print(Cs)

clss = np.zeros((H*W), dtype=int)

for i in range(H*W):
    dis = np.sqrt(np.sum((Cs - img[i])**2, axis=1))
    clss[i] = np.argmin(dis)


out = np.reshape(clss, (H, W)) * 50
out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
