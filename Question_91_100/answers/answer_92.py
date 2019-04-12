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


while True:

    clss = np.zeros((H*W), dtype=int)
    
    for i in range(H*W):
        dis = np.sqrt(np.sum((Cs - img[i])**2, axis=1))
        clss[i] = np.argmin(dis)

    Cs_tmp = np.zeros((Class, 3))
    
    for i in range(Class):
        Cs_tmp[i] = np.mean(img[clss==i], axis=0)

    if (Cs == Cs_tmp).all():
        break
    else:
        Cs = Cs_tmp.copy()

out = np.zeros((H*W, 3), dtype=np.float32)
        
for i in range(Class):
    out[clss == i] = Cs[i]

print(Cs)
    
out[out < 0] = 0
out[out > 255] = 255
out = np.reshape(out, (H, W, 3))
out = out.astype(np.uint8)

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
