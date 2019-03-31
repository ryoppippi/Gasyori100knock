import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("gazo.png").astype(np.float32)
H, W, C = img.shape

out = np.zeros((H, W), dtype=np.int)
out[img[..., 0]>0] = 1

tmp = out.copy()
_tmp = 1 - tmp

count = 1
while count > 0:
    count = 0
    tmp = out.copy()
    _tmp = 1 - tmp

    tmp2 = out.copy()
    _tmp2 = 1 - tmp2
    
    for y in range(H):
        for x in range(W):
            if out[y, x] < 1:
                continue
            
            judge = 0
            
            ## condition 1
            if (tmp[y,min(x+1,W-1)] * tmp[max(y-1,0), x] * tmp[y,max(x-1,0)] * tmp[min(y+1,H-1),x]) == 0:
                judge += 1
                
            ## condition 2
            c = 0
            c += (_tmp[y,min(x+1,W-1)] - _tmp[y,min(x+1,W-1)] * _tmp[max(y-1,0),min(x+1,W-1)] * _tmp[max(y-1,0),x])
            c += (_tmp[max(y-1,0),x] - _tmp[max(y-1,0),x] * _tmp[max(y-1,0),max(x-1,0)] * _tmp[y,max(x-1,0)])
            c += (_tmp[y,max(x-1,0)] - _tmp[y,max(x-1,0)] * _tmp[min(y+1,H-1),max(x-1,0)] * _tmp[min(y+1,H-1),x])
            c += (_tmp[min(y+1,H-1),x] - _tmp[min(y+1,H-1),x] * _tmp[min(y+1,H-1),min(x+1,W-1)] * _tmp[y,min(x+1,W-1)])
            if c == 1:
                judge += 1
                
            ## condition 3
            if np.sum(tmp[max(y-1,0):min(y+2,H), max(x-1,0):min(x+2,W)]) >= 3:
                judge += 1

            ## condition 4
            if np.sum(out[max(y-1,0):min(y+2,H), max(x-1,0):min(x+2,W)]) >= 2:
                judge += 1

            ## condition 5
            _tmp2 = 1-out

            c = 0
            c += (_tmp2[y,min(x+1,W-1)] - _tmp2[y,min(x+1,W-1)] * _tmp2[max(y-1,0),min(x+1,W-1)] * _tmp2[max(y-1,0),x])
            c += (_tmp2[max(y-1,0),x] - _tmp2[max(y-1,0),x] * (1-tmp[max(y-1,0),max(x-1,0)]) * _tmp2[y,max(x-1,0)])
            c += (_tmp2[y,max(x-1,0)] - _tmp2[y,max(x-1,0)] * _tmp2[min(y+1,H-1),max(x-1,0)] * _tmp2[min(y+1,H-1),x])
            c += (_tmp2[min(y+1,H-1),x] - _tmp2[min(y+1,H-1),x] * _tmp2[min(y+1,H-1),min(x+1,W-1)] * _tmp2[y,min(x+1,W-1)])
            if c == 1 or (out[max(y-1,0), max(x-1,0)] != tmp[max(y-1,0), max(x-1,0)]):
                judge += 1

            c = 0
            c += (_tmp2[y,min(x+1,W-1)] - _tmp2[y,min(x+1,W-1)] * _tmp2[max(y-1,0),min(x+1,W-1)] * (1-tmp[max(y-1,0),x]))
            c += ((1-tmp[max(y-1,0),x]) - (1-tmp[max(y-1,0),x]) * _tmp2[max(y-1,0),max(x-1,0)] * _tmp2[y,max(x-1,0)])
            c += (_tmp2[y,max(x-1,0)] - _tmp2[y,max(x-1,0)] * _tmp2[min(y+1,H-1),max(x-1,0)] * _tmp2[min(y+1,H-1),x])
            c += (_tmp2[min(y+1,H-1),x] - _tmp2[min(y+1,H-1),x] * _tmp2[min(y+1,H-1),min(x+1,W-1)] * _tmp2[y,min(x+1,W-1)])
            if c == 1 or (out[max(y-1,0), x] != tmp[max(y-1,0), x]):
                judge += 1

            c = 0
            c += (_tmp2[y,min(x+1,W-1)] - _tmp2[y,min(x+1,W-1)] * (1-tmp[max(y-1,0),min(x+1,W-1)]) * _tmp2[max(y-1,0),x])
            c += (_tmp2[max(y-1,0),x] - _tmp2[max(y-1,0),x] * _tmp2[max(y-1,0),max(x-1,0)] * _tmp2[y,max(x-1,0)])
            c += (_tmp2[y,max(x-1,0)] - _tmp2[y,max(x-1,0)] * _tmp2[min(y+1,H-1),max(x-1,0)] * _tmp2[min(y+1,H-1),x])
            c += (_tmp2[min(y+1,H-1),x] - _tmp2[min(y+1,H-1),x] * _tmp2[min(y+1,H-1),min(x+1,W-1)] * _tmp2[y,min(x+1,W-1)])
            if c == 1 or (out[max(y-1,0), min(x+1,W-1)] != tmp[max(y-1,0), min(x+1,W-1)]):
                judge += 1

            c = 0
            c += (_tmp2[y,min(x+1,W-1)] - _tmp2[y,min(x+1,W-1)] * _tmp2[max(y-1,0),min(x+1,W-1)] * _tmp2[max(y-1,0),x])
            c += (_tmp2[max(y-1,0),x] - _tmp2[max(y-1,0),x] * _tmp2[max(y-1,0),max(x-1,0)] * (1-tmp[y,max(x-1,0)]))
            c += ((1-tmp[y,max(x-1,0)]) - (1-tmp[y,max(x-1,0)]) * _tmp2[min(y+1,H-1),max(x-1,0)] * _tmp2[min(y+1,H-1),x])
            c += (_tmp2[min(y+1,H-1),x] - _tmp2[min(y+1,H-1),x] * _tmp2[min(y+1,H-1),min(x+1,W-1)] * _tmp2[y,min(x+1,W-1)])
            if c == 1 or (out[y, max(x-1,0)] != tmp[y, max(x-1,0)]):
                judge += 1
            
            if judge >= 8:
                out[y,x] = 0
                count += 1
                
out = out.astype(np.uint8) * 255

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
