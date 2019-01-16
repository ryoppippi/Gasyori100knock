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
    _tmp = 1 - tmp
    
    for y in range(H):
        for x in range(W):
            # condition 1
            if out[y, x] < 1:
                continue
            
            judge = 0

            out_a = np.abs(out)
            
            ## condition 2
            if 1 - out_a[y, min(x+1, W-1)] + 1 - out_a[max(y-1, 0), x] + 1 - out_a[y, max(x-1,0)] + 1 - out_a[min(y+1,H-1), x] >= 1:
                judge += 1
                
            ## condition 3
            n8 = out[max(y-1,0):min(y+2,H), max(x-1,0):min(x+2,W)]
            if np.sum(np.abs(n8)) >= 3:
                judge += 1

            ## condition 4
            if np.sum(n8[n8==1]) >= 2:
                judge += 1

            ## condition 5
            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1
                
            ## condition 6
            c = 0
            c += (0 - 0 * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * 0)
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * 0 * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * 0)
            c += (0 - 0 * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * 0 * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * 0)
            c += (0 - 0 * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * 0 * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * 0)
            c += (0 - 0 * out_a[min(y+1,H-1),min(x+1,W-1)] * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1

            c = 0
            c += (out_a[y,min(x+1,W-1)] - out_a[y,min(x+1,W-1)] * out_a[max(y-1,0),min(x+1,W-1)] * out_a[max(y-1,0),x])
            c += (out_a[max(y-1,0),x] - out_a[max(y-1,0),x] * out_a[max(y-1,0),max(x-1,0)] * out_a[y,max(x-1,0)])
            c += (out_a[y,max(x-1,0)] - out_a[y,max(x-1,0)] * out_a[min(y+1,H-1),max(x-1,0)] * out_a[min(y+1,H-1),x])
            c += (out_a[min(y+1,H-1),x] - out_a[min(y+1,H-1),x] * 0 * out_a[y,min(x+1,W-1)])
            if c == 1:
                judge += 1
                
                
            if judge >= 5:
                out[y,x] = -1
                count += 1

    out[out == -1] = 0
    
                
out = out.astype(np.uint8) * 255

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
