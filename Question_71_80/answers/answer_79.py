import cv2
import numpy as np
import matplotlib.pyplot as plt

# Grayscale
def BGR2GRAY(img):
	# Grayscale
	gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
	return gray

# Gabor
def Gabor_filter(K_size=111, Sigma=10, Gamma=1.2, Lambda=10, Psi=0, angle=0):
	# get half size
	d = K_size // 2

	# prepare kernel
	gabor = np.zeros((K_size, K_size), dtype=np.float32)

	# each value
	for y in range(K_size):
		for x in range(K_size):
			# distance from center
			px = x - d
			py = y - d

			# degree -> radian
			theta = angle / 180. * np.pi

			# get kernel x
			_x = np.cos(theta) * px + np.sin(theta) * py

			# get kernel y
			_y = -np.sin(theta) * px + np.cos(theta) * py

			# fill kernel
			gabor[y, x] = np.exp(-(_x**2 + Gamma**2 * _y**2) / (2 * Sigma**2)) * np.cos(2*np.pi*_x/Lambda + Psi)

	# kernel normalization
	gabor /= np.sum(np.abs(gabor))

	return gabor


def Gabor_filtering(gray, K_size=111, Sigma=10, Gamma=1.2, Lambda=10, Psi=0, angle=0):
    # get shape
    H, W = gray.shape

    # padding
    gray = np.pad(gray, (K_size//2, K_size//2), 'edge')

    # prepare out image
    out = np.zeros((H, W), dtype=np.float32)

    # get gabor filter
    gabor = Gabor_filter(K_size=K_size, Sigma=Sigma, Gamma=Gamma, Lambda=Lambda, Psi=0, angle=angle)
        
    # filtering
    for y in range(H):
        for x in range(W):
            out[y, x] = np.sum(gray[y : y + K_size, x : x + K_size] * gabor)

    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)

    return out


def Gabor_process(img):
    # gray scale
    gray = BGR2GRAY(img).astype(np.float32)

    # define angle
    As = [0, 45, 90, 135]

    # prepare pyplot
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0, wspace=0.2)

    # each angle
    for i, A in enumerate(As):
        # gabor filtering
        out = Gabor_filtering(gray, K_size=11, Sigma=1.5, Gamma=1.2, Lambda=3, angle=A)

        plt.subplot(1, 4, i+1)
        plt.imshow(out, cmap='gray')
        plt.axis('off')
        plt.title("Angle "+str(A))

    plt.savefig("out.png")
    plt.show()

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# gabor process
Gabor_process(img)


