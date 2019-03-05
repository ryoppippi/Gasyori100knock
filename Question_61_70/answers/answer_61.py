import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("renketsu.png").astype(np.float32)
H, W, C = img.shape

tmp = np.zeros((H, W), dtype=np.int)
tmp[img[..., 0]>0] = 1

out = np.zeros((H, W, 3), dtype=np.uint8)

for y in range(H):
    for x in range(W):
        if tmp[y, x] < 1:
            continue

        c = 0
        c += (tmp[y,min(x+1,W-1)] - tmp[y,min(x+1,W-1)] * tmp[max(y-1,0),min(x+1,W-1)] * tmp[max(y-1,0),x])
        c += (tmp[max(y-1,0),x] - tmp[max(y-1,0),x] * tmp[max(y-1,0),max(x-1,0)] * tmp[y,max(x-1,0)])
        c += (tmp[y,max(x-1,0)] - tmp[y,max(x-1,0)] * tmp[min(y+1,H-1),max(x-1,0)] * tmp[min(y+1,H-1),x])
        c += (tmp[min(y+1,H-1),x] - tmp[min(y+1,H-1),x] * tmp[min(y+1,H-1),min(x+1,W-1)] * tmp[y,min(x+1,W-1)])
        
        if c == 0:
            out[y,x] = [0, 0, 255]
        elif c == 1:
            out[y,x] = [0, 255, 0]
        elif c == 2:
            out[y,x] = [255, 0, 0]
        elif c == 3:
            out[y,x] = [255, 255, 0]
        elif c == 4:
            out[y,x] = [255, 0, 255]
                
out = out.astype(np.uint8)

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
