import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("gazo.png").astype(np.float32)
H, W, C = img.shape

tmp = np.zeros((H, W), dtype=np.int)
tmp[img[..., 0] > 0] = 255

out = np.zeros_like(tmp)

flag = False
for y in range(H):
    for x in range(W):
        if flag:
            continue
        if tmp[y, x] == 255:
            tx = x
            ty = y
            pre = 7
            while True:
                print(tx, ty)
                
                if tmp[min(ty+1, H-1), max(tx-1,0)] == 255 and out[min(ty+1, H-1), max(tx-1,0)] == 0:
                    tx = max(tx-1, 0)
                    ty = min(ty+1, H-1)
                    out[ty, tx] = 255
                    pre = 0
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[min(ty+1, H-1), tx] == 255 and out[min(ty+1, H-1), tx] == 0:
                    tx = tx
                    ty = min(ty+1, H-1)
                    out[ty, tx] = 255
                    pre = 1
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[min(ty+1, H-1), min(tx+1, W-1)] == 255 and out[min(ty+1, H-1), min(tx+1, W-1)] == 0:
                    tx = min(tx+1, W-1)
                    ty = min(ty+1, H-1)
                    out[ty, tx] = 255
                    pre = 2
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[ty, min(tx+1, W-1)] == 255 and out[ty, min(tx+1, W-1)] == 0:
                    tx = min(tx+1, W-1)
                    ty = ty
                    out[ty, tx] = 255
                    pre = 3
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[max(ty-1, 0), min(tx+1, W-1)] == 255 and out[max(ty-1, 0), min(tx+1, W-1)] == 0:
                    tx = min(tx+1, W-1)
                    ty = max(ty-1, 0)
                    out[ty, tx] = 255
                    pre = 4
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[max(ty-1, 0), tx] == 255 and out[max(ty-1, 0), tx] == 0:
                    tx = tx
                    ty = max(ty-1, 0)
                    out[ty, tx] = 255
                    pre = 5
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[max(ty-1, 0), max(tx-1, 0)] == 255 and out[max(ty-1, 0), max(tx-1, 0)] == 0:
                    tx = max(tx-1, 0)
                    ty = max(ty-1, 0)
                    out[ty, tx] = 255
                    pre = 6
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue
                if tmp[ty, max(tx-1, 0)] == 255 and out[ty, max(tx-1, 0)] == 0:
                    tx = max(tx-1, 0)
                    ty = ty
                    out[ty, tx] = 255
                    pre = 7
                    if tx == x and ty == y:
                        flag = True
                        break
                    continue

out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
