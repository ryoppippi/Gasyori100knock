import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("gazo.png").astype(np.float32)
H, W, C = img.shape

out = np.zeros((H, W), dtype=np.int)
out[img[..., 0]>0] = 1

out = 1 - out

while True:
    s1 = []
    s2 = []

    # step 1
    for y in range(1, H-1):
        for x in range(1, W-1):
            
            # condition 1
            if out[y, x] > 0:
                continue

            # condition 2
            f1 = 0
            if (out[y-1, x+1] - out[y-1, x]) == 1:
                f1 += 1
            if (out[y, x+1] - out[y-1, x+1]) == 1:
                f1 += 1
            if (out[y+1, x+1] - out[y, x+1]) == 1:
                f1 += 1
            if (out[y+1, x] - out[y+1,x+1]) == 1:
                f1 += 1
            if (out[y+1, x-1] - out[y+1, x]) == 1:
                f1 += 1
            if (out[y, x-1] - out[y+1, x-1]) == 1:
                f1 += 1
            if (out[y-1, x-1] - out[y, x-1]) == 1:
                f1 += 1
            if (out[y-1, x] - out[y-1, x-1]) == 1:
                f1 += 1

            if f1 != 1:
                continue
                
            # condition 3
            f2 = np.sum(out[y-1:y+2, x-1:x+2])
            if f2 < 2 or f2 > 6:
                continue
            
            # condition 4
            if out[y-1, x] + out[y, x+1] + out[y+1, x] < 1:
                continue

            # condition 5
            if out[y, x+1] + out[y+1, x] + out[y, x-1] < 1:
                continue
                
            s1.append([y, x])

    for v in s1:
        out[v[0], v[1]] = 1

    # step 2
    for y in range(1, H-1):
        for x in range(1, W-1):
            
            # condition 1
            if out[y, x] > 0:
                continue

            # condition 2
            f1 = 0
            if (out[y-1, x+1] - out[y-1, x]) == 1:
                f1 += 1
            if (out[y, x+1] - out[y-1, x+1]) == 1:
                f1 += 1
            if (out[y+1, x+1] - out[y, x+1]) == 1:
                f1 += 1
            if (out[y+1, x] - out[y+1,x+1]) == 1:
                f1 += 1
            if (out[y+1, x-1] - out[y+1, x]) == 1:
                f1 += 1
            if (out[y, x-1] - out[y+1, x-1]) == 1:
                f1 += 1
            if (out[y-1, x-1] - out[y, x-1]) == 1:
                f1 += 1
            if (out[y-1, x] - out[y-1, x-1]) == 1:
                f1 += 1

            if f1 != 1:
                continue
                
            # condition 3
            f2 = np.sum(out[y-1:y+2, x-1:x+2])
            if f2 < 2 or f2 > 6:
                continue
            
            # condition 4
            if out[y-1, x] + out[y, x+1] + out[y, x-1] < 1:
                continue

            # condition 5
            if out[y-1, x] + out[y+1, x] + out[y, x-1] < 1:
                continue
                
            s2.append([y, x])

    for v in s2:
        out[v[0], v[1]] = 1

    if len(s1) < 1 and len(s2) < 1:
        break

out = 1 - out
out = out.astype(np.uint8) * 255

# Save result
cv2.imwrite("out.png", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
