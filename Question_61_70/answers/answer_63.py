import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("gazo.png").astype(np.float32)
H, W, C = img.shape

out = np.zeros((H, W), dtype=np.int)
out[img[..., 0]>0] = 1

count = 1
while count > 0:
    count = 0
    tmp = out.copy()
    for y in range(H):
        for x in range(W):
            if out[y, x] < 1:
                continue
            
            judge = 0
            
            ## condition 1
            if (tmp[y,min(x+1,W-1)] + tmp[max(y-1,0), x] + tmp[y,max(x-1,0)] + tmp[min(y+1,H-1),x]) < 4:
                judge += 1
                
            ## condition 2
            c = 0
            c += (tmp[y,min(x+1,W-1)] - tmp[y,min(x+1,W-1)]*tmp[max(y-1,0),min(x+1,W-1)]*tmp[max(y-1,0),x])
            c += (tmp[max(y-1,0),x] - tmp[max(y-1,0),x]*tmp[max(y-1,0),max(x-1,0)]*tmp[y,max(x-1,0)])
            c += (tmp[y,max(x-1,0)] - tmp[y,max(x-1,0)]*tmp[min(y+1,H-1),max(x-1,0)]*tmp[min(y+1,H-1),x])
            c += (tmp[min(y+1,H-1),x] - tmp[min(y+1,H-1),x]*tmp[min(y+1,H-1),min(x+1,W-1)]*tmp[y,min(x+1,W-1)])
            if c == 1:
                judge += 1
                
            ##x condition 3
            if np.sum(tmp[max(y-1,0):min(y+2,H), max(x-1,0):min(x+2,W)]) >= 4:
                judge += 1
            
            if judge == 3:
                out[y,x] = 0
                count += 1

out = out.astype(np.uint8) * 255

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
