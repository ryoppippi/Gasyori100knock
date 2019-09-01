import cv2
import numpy as np
import matplotlib.pyplot as plt

# Connect 4
def connect_4(img):
    # get shape
    H, W, C = img.shape

    # prepare temporary image
    tmp = np.zeros((H, W), dtype=np.int)

    # binarize
    tmp[img[..., 0] > 0] = 1

    # prepare out image
    out = np.zeros((H, W, 3), dtype=np.uint8)

    # each pixel
    for y in range(H):
        for x in range(W):
            if tmp[y, x] < 1:
                continue

            S = 0
            S += (tmp[y,min(x+1,W-1)] - tmp[y,min(x+1,W-1)] * tmp[max(y-1,0),min(x+1,W-1)] * tmp[max(y-1,0),x])
            S += (tmp[max(y-1,0),x] - tmp[max(y-1,0),x] * tmp[max(y-1,0),max(x-1,0)] * tmp[y,max(x-1,0)])
            S += (tmp[y,max(x-1,0)] - tmp[y,max(x-1,0)] * tmp[min(y+1,H-1),max(x-1,0)] * tmp[min(y+1,H-1),x])
            S += (tmp[min(y+1,H-1),x] - tmp[min(y+1,H-1),x] * tmp[min(y+1,H-1),min(x+1,W-1)] * tmp[y,min(x+1,W-1)])
            
            if S == 0:
                out[y,x] = [0, 0, 255]
            elif S == 1:
                out[y,x] = [0, 255, 0]
            elif S == 2:
                out[y,x] = [255, 0, 0]
            elif S == 3:
                out[y,x] = [255, 255, 0]
            elif S == 4:
                out[y,x] = [255, 0, 255]
                    
    out = out.astype(np.uint8)

    return out



# Read image
img = cv2.imread("renketsu.png").astype(np.float32)

# connect 4
out = connect_4(img)

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
