import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Gray scale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

#fimg = np.fft.fft2(gray)
    
# 第1象限と第3象限, 第2象限と第4象限を入れ替え
#fimg =  np.fft.fftshift(fimg)
#print(fimg)
# パワースペクトルの計算
#mag = 20*np.log(np.abs(fimg))
    
# 入力画像とスペクトル画像をグラフ描画
#plt.subplot(121)
#plt.imshow(gray, cmap = 'gray')
#plt.subplot(122)
#plt.imshow(mag, cmap = 'gray')
#plt.show()


# Fourier
U = W
V = H

X = np.zeros((V, U), dtype=np.complex)
X_r = np.zeros((V, U), dtype=np.complex)
X_i = np.zeros((V, U), dtype=np.float32)

x = np.tile(np.arange(W), (H, 1))
y = np.arange(H).repeat(W).reshape(H, -1)

for v in range(V):
    for u in range(U):
        #X_r[v, u] = np.sum(re)
        #X_i[v, u] = np.sum(img)
        theta = (-2j * np.pi * (1. * v * y / H + 1. * u * x / W))
        X[v, u] = np.sum(gray * np.exp(theta)) / (H * W)

print(X)
#X = np.sqrt(np.power(X_r, 2), np.power(X_i, 2))
X = np.abs(X.imag).astype(np.uint8)
print(X)
plt.imshow(X, cmap='gray')
plt.show()

out = np.zeros((V, U), dtype=np.float32)

for v in range(V):
    for u in range(U):
        theta = (2. * np.pi * (1. * v * y / H + 1. * u * x / W))
        out[v, u] = np.sum(X_r[v, u] * np.cos(theta) + X_i[v, u] * np.sin(theta))

out = out.astype(np.uint8)
    
# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
