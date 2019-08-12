import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# RGB > YCbCr
Y = 0.2990 * img[..., 2] + 0.5870 * img[..., 1] + 0.1140 * img[..., 0]
Cb = -0.1687 * img[..., 2] - 0.3313 * img[..., 1] + 0.5 * img[..., 0] + 128.
Cr = 0.5 * img[..., 2] - 0.4187 * img[..., 1] - 0.0813 * img[..., 0] + 128.

YCC = np.zeros_like(img, dtype=np.float32)
YCC[..., 0] = Y
YCC[..., 1] = Cb
YCC[..., 2] = Cr


# DCT
T = 8
K = 8
X = np.zeros((H, W, C), dtype=np.float64)

Q1 = np.array(((16, 11, 10, 16, 24, 40, 51, 61),
               (12, 12, 14, 19, 26, 58, 60, 55),
               (14, 13, 16, 24, 40, 57, 69, 56),
               (14, 17, 22, 29, 51, 87, 80, 62),
               (18, 22, 37, 56, 68, 109, 103, 77),
               (24, 35, 55, 64, 81, 104, 113, 92),
               (49, 64, 78, 87, 103, 121, 120, 101),
               (72, 92, 95, 98, 112, 100, 103, 99)), dtype=np.float32)

Q2 = np.array(((17, 18, 24, 47, 99, 99, 99, 99),
               (18, 21, 26, 66, 99, 99, 99, 99),
               (24, 26, 56, 99, 99, 99, 99, 99),
               (47, 66, 99, 99, 99, 99, 99, 99),
               (99, 99, 99, 99, 99, 99, 99, 99),
               (99, 99, 99, 99, 99, 99, 99, 99),
               (99, 99, 99, 99, 99, 99, 99, 99),
               (99, 99, 99, 99, 99, 99, 99, 99)), dtype=np.float32)

def w(x, y, u, v):
    cu = 1.
    cv = 1.
    if u == 0:
        cu /= np.sqrt(2)
    if v == 0:
        cv /= np.sqrt(2)
    theta = np.pi / (2 * T)
    return (( 2 * cu * cv / T) * np.cos((2*x+1)*u*theta) * np.cos((2*y+1)*v*theta))
    
for yi in range(0, H, T):
    for xi in range(0, W, T):
        for v in range(T):
            for u in range(T):
                for y in range(T):
                    for x in range(T):
                        for c in range(C):
                            X[v+yi, u+xi, c] += YCC[y+yi, x+xi, c] * w(x,y,u,v)
                            
        X[yi:yi+T, xi:xi+T, 0] = np.round(X[yi:yi+T, xi:xi+T, 0] / Q1) * Q1
        X[yi:yi+T, xi:xi+T, 1] = np.round(X[yi:yi+T, xi:xi+T, 1] / Q2) * Q2
        X[yi:yi+T, xi:xi+T, 2] = np.round(X[yi:yi+T, xi:xi+T, 2] / Q2) * Q2
                

# IDCT
IYCC = np.zeros((H, W, 3), dtype=np.float64)

for yi in range(0, H, T):
    for xi in range(0, W, T):
        for y in range(T):
            for x in range(T):
                for v in range(K):
                    for u in range(K):
                        IYCC[y+yi, x+xi] += X[v+yi, u+xi] * w(x,y,u,v)


# YCbCr > RGB
out = np.zeros_like(img, dtype=np.float32)
out[..., 2] = IYCC[..., 0] + (IYCC[..., 2] - 128.) * 1.4020
out[..., 1] = IYCC[..., 0] - (IYCC[..., 1] - 128.) * 0.3441 - (IYCC[..., 2] - 128.) * 0.7139
out[..., 0] = IYCC[..., 0] + (IYCC[..., 1] - 128.) * 1.7718

out[out>255] = 255
out = out.astype(np.uint8)
                        
# MSE
v_max = 255.
mse = np.sum(np.power(np.abs(img.astype(np.float32) - out.astype(np.float32)), 2)) / (H * W * C)
psnr = 10 * np.log10(v_max ** 2 / mse)

print("PSNR >>", psnr)

bitrate = 1. * T * K ** 2 / (T ** 2)
print("bitrate >>", bitrate)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
