import cv2
import numpy as np
import matplotlib.pyplot as plt


# get HOG step1
def HOG_step1(img):
     # Grayscale
     def BGR2GRAY(img):
          gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
          return gray

     # Magnitude and gradient
     def get_gradXY(gray):
          H, W = gray.shape

          # padding before grad
          gray = np.pad(gray, (1, 1), 'edge')

          # get grad x
          gx = gray[1:H+1, 2:] - gray[1:H+1, :W]
          # get grad y
          gy = gray[2:, 1:W+1] - gray[:H, 1:W+1]
          # replace 0 with 
          gx[gx == 0] = 1e-6

          return gx, gy

     # get magnitude and gradient
     def get_MagGrad(gx, gy):
          # get gradient maginitude
          magnitude = np.sqrt(gx ** 2 + gy ** 2)

          # get gradient angle
          gradient = np.arctan(gy / gx)

          gradient[gradient < 0] = np.pi / 2 + gradient[gradient < 0] + np.pi / 2

          return magnitude, gradient

     # Gradient histogram
     def quantization(gradient):
          # prepare quantization table
          gradient_quantized = np.zeros_like(gradient, dtype=np.int)

          # quantization base
          d = np.pi / 9

          # quantization
          for i in range(9):
               gradient_quantized[np.where((gradient >= d * i) & (gradient <= d * (i + 1)))] = i

          return gradient_quantized

     # 1. BGR -> Gray
     gray = BGR2GRAY(img)

     # 1. Gray -> Gradient x and y
     gx, gy = get_gradXY(gray)

     # 2. get gradient magnitude and angle
     magnitude, gradient = get_MagGrad(gx, gy)

     # 3. Quantization
     gradient_quantized = quantization(gradient)

     return magnitude, gradient_quantized


# Read image
img = cv2.imread("imori.jpg").astype(np.float32)

# get HOG step1
magnitude, gradient_quantized = HOG_step1(img)

# Write gradient magnitude to file
_magnitude = (magnitude / magnitude.max() * 255).astype(np.uint8)

cv2.imwrite("out_mag.jpg", _magnitude)

# Write gradient angle to file
H, W, C = img.shape
out = np.zeros((H, W, 3), dtype=np.uint8)

# define color
C = [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [255, 0, 255], [0, 255, 255],
     [127, 127, 0], [127, 0, 127], [0, 127, 127]]

# draw color
for i in range(9):
     out[gradient_quantized == i] = C[i]


cv2.imwrite("out_gra.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
