import cv2
import numpy as np
import matplotlib.pyplot as plt


# DFT hyper-parameters
K, L = 128, 128
channel = 3


# DFT
def dft(img):
	H, W, _ = img.shape

	# Prepare DFT coefficient
	G = np.zeros((L, K, channel), dtype=np.complex)

	# prepare processed index corresponding to original image positions
	x = np.tile(np.arange(W), (H, 1))
	y = np.arange(H).repeat(W).reshape(H, -1)

	# dft
	for c in range(channel):
		for l in range(L):
			for k in range(K):
				G[l, k, c] = np.sum(img[..., c] * np.exp(-2j * np.pi * (x * k / K + y * l / L))) / np.sqrt(K * L)
				#for n in range(N):
				#    for m in range(M):
				#        v += gray[n, m] * np.exp(-2j * np.pi * (m * k / M + n * l / N))
				#G[l, k] = v / np.sqrt(M * N)

	return G

# IDFT
def idft(G):
	# prepare out image
	H, W, _ = G.shape
	out = np.zeros((H, W, channel), dtype=np.float32)

	# prepare processed index corresponding to original image positions
	x = np.tile(np.arange(W), (H, 1))
	y = np.arange(H).repeat(W).reshape(H, -1)

	# idft
	for c in range(channel):
		for l in range(H):
			for k in range(W):
				out[l, k, c] = np.abs(np.sum(G[..., c] * np.exp(2j * np.pi * (x * k / W + y * l / H)))) / np.sqrt(W * H)

	# clipping
	out = np.clip(out, 0, 255)
	out = out.astype(np.uint8)

	return out



# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# DFT
G = dft(img)

# write poser spectal to image
ps = (np.abs(G) / np.abs(G).max() * 255).astype(np.uint8)
cv2.imwrite("out_ps.jpg", ps)

# IDFT
out = idft(G)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)



"""
fimg = np.fft.fft2(gray)
    
# 第1象限と第3象限, 第2象限と第4象限を入れ替え
fimg =  np.fft.fftshift(fimg)
print(fimg.shape)
# パワースペクトルの計算
mag = 20*np.log(np.abs(fimg))
    
# 入力画像とスペクトル画像をグラフ描画
plt.subplot(121)
plt.imshow(gray, cmap = 'gray')
plt.subplot(122)
plt.imshow(mag, cmap = 'gray')
plt.show()
"""