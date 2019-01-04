import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("thorino.jpg").astype(np.float32)
H, W, C = img.shape

# Gray
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

# Gaussian Filter
K_size = 5
sigma = 1.4

## Zero padding
pad = K_size // 2
gau = np.zeros((H + pad*2, W + pad*2), dtype=np.float32)
#gau[pad:pad+H, pad:pad+W] = gray.copy().astype(np.float32)
gau = np.pad(gray, (pad, pad), 'edge')
tmp = gau.copy()

## Kernel
K = np.zeros((K_size, K_size), dtype=np.float32)
for x in range(-pad, -pad+K_size):
    for y in range(-pad, -pad+K_size):
        K[y+pad, x+pad] = np.exp( -(x**2 + y**2) / (2* (sigma**2)))
K /= (sigma * np.sqrt(2 * np.pi))
K /= K.sum()

for y in range(H):
    for x in range(W):
        gau[pad+y, pad+x] = np.sum(K * tmp[y:y+K_size, x:x+K_size])

## Sobel vertical
KSV = np.array(((-1., -2., -1.), (0., 0., 0.), (1., 2., 1.)), dtype=np.float32)
## Sobel horizontal
KSH = np.array(((-1., 0., 1.), (-2., 0., 2.), (-1., 0., 1.)), dtype=np.float32)

gau = gau[pad-1:H+pad+1, pad-1:W+pad+1]
fy = np.zeros_like(gau, dtype=np.float32)
fx = np.zeros_like(gau, dtype=np.float32)
K_size = 3
pad = K_size // 2

for y in range(H):
    for x in range(W):
        fy[pad+y, pad+x] = np.sum(KSV * gau[y:y+K_size, x:x+K_size])
        fx[pad+y, pad+x] = np.sum(KSH * gau[y:y+K_size, x:x+K_size])
        
fx = fx[pad:pad+H, pad:pad+W]
fy = fy[pad:pad+H, pad:pad+W]

# Non-maximum suppression
edge = np.sqrt(np.power(fx, 2) + np.power(fy, 2))
fx[fx == 0] = 1e-5
tan = np.arctan(fy / fx)
## Angle quantization
angle = np.zeros_like(tan, dtype=np.uint8)
angle[np.where((tan > -0.4142) & (tan <= 0.4142))] = 0
angle[np.where((tan > 0.4142) & (tan < 2.4142))] = 45
angle[np.where((tan >= 2.4142) | (tan <= -2.4142))] = 95
angle[np.where((tan > -2.4142) & (tan <= -0.4142))] = 135

for y in range(H):
    for x in range(W):
        if angle[y, x] == 0:
            dx1, dy1, dx2, dy2 = -1, 0, 1, 0
        elif angle[y, x] == 45:
            dx1, dy1, dx2, dy2 = -1, 1, 1, -1
        elif angle[y, x] == 90:
            dx1, dy1, dx2, dy2 = 0, -1, 0, 1
        elif angle[y, x] == 135:
            dx1, dy1, dx2, dy2 = -1, -1, 1, 1
        if x == 0:
            dx1 = max(dx1, 0)
            dx2 = max(dx2, 0)
        if x == W-1:
            dx1 = min(dx1, 0)
            dx2 = min(dx2, 0)
        if y == 0:
            dy1 = max(dy1, 0)
            dy2 = max(dy2, 0)
        if y == H-1:
            dy1 = min(dy1, 0)
            dy2 = min(dy2, 0)
        if max(max(edge[y, x], edge[y+dy1, x+dx1]), edge[y+dy2, x+dx2]) != edge[y, x]:
            edge[y, x] = 0


# Histeresis threshold
HT = 100
LT = 30
edge[edge >= HT] = 255
edge[edge <= LT] = 0

_edge = np.zeros((H+2, W+2), dtype=np.float32)
_edge[1:H+1, 1:W+1] = edge

## 8 - Nearest neighbor
nn = np.array(((1., 1., 1.), (1., 0., 1.), (1., 1., 1.)), dtype=np.float32)

for y in range(1, H+2):
    for x in range(1, W+2):
        if _edge[y, x] < LT or _edge[y, x] > HT:
            continue
        if np.max(_edge[y-1:y+2, x-1:x+2] * nn) >= HT:
            _edge[y, x] = 255
        else:
            _edge[y, x] = 0

edge = _edge[1:H+1, 1:W+1].astype(np.uint8)

## Canny finish

# Hough

## Voting
drho = 1
dtheta = 1
rho_max = np.ceil(np.sqrt(H**2 + W**2)).astype(np.int)
hough = np.zeros((rho_max, 180), dtype=np.int)

ind = np.where(edge == 255)

## hough transformation
for y, x in zip(ind[0], ind[1]):
    for theta in range(0, 180, dtheta):
        t = np.pi / 180 * theta
        rho = int(x * np.cos(t) + y * np.sin(t))
        hough[rho, theta] += 1

plt.imshow(hough, cmap='gray')

## non maximum suppression
for y in range(rho_max):
    for x in range(180):
        x1 = max(x-1, 0)
        x2 = min(x+2, 180)
        y1 = max(y-1, 0)
        y2 = min(y+2, rho_max)
        if np.max(hough[y1:y2, x1:x2]) == hough[y,x] and hough[y, x] != 0:
            pass
            #hough[y,x] = 255
        else:
            hough[y,x] = 0
ind_x = np.argsort(hough.ravel())[::-1][:10]
ind_y = ind_x.copy()
thetas = ind_x % 180
rhos = ind_y // 180
_hough = np.zeros_like(hough, dtype=np.int)
_hough[rhos, thetas] = 255
        
out = _hough.astype(np.uint8)
            
# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
