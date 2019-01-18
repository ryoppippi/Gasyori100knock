import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float32)
H, W, C = img.shape

# Grayscale
gray = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]

def resize(img, a):
    _h, _w  = img.shape
    h = int(a * _h)
    w = int(a * _w)
    """
    y = np.arange(h).repeat(w).reshape(w, -1)
    x = np.tile(np.arange(w), (h, 1))
    y = np.floor(y / a).astype(np.int)
    x = np.floor(x / a).astype(np.int)
    y = np.minimum(y, _h-1)
    x = np.minimum(x, _w-1)
    out = img[y,x]
    """
    y = np.arange(h).repeat(w).reshape(w, -1)
    x = np.tile(np.arange(w), (h, 1))
    y = (y / a)
    x = (x / a)

    ix = np.floor(x).astype(np.int)
    iy = np.floor(y).astype(np.int)
    ix = np.minimum(ix, _w-2)
    iy = np.minimum(iy, _w-2)

    dx = x - ix
    dy = y - iy
    #dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)
    #dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)
    
    out = (1-dx) * (1-dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix+1] + (1 - dx) * dy * img[iy+1, ix] + dx * dy * img[iy+1, ix+1]
    out[out>255] = 255

    return out

pyramid = [gray]
for i in range(1, 6):
    a = 2. ** i
    p = resize(gray, 1. / a)
    p = resize(p, a)
    pyramid.append(p)
    
out = np.zeros((H, W), dtype=np.float32)

out += np.abs(pyramid[0] - pyramid[1])
out += np.abs(pyramid[0] - pyramid[3])
out += np.abs(pyramid[0] - pyramid[5])
out += np.abs(pyramid[1] - pyramid[4])
out += np.abs(pyramid[2] - pyramid[3])
out += np.abs(pyramid[3] - pyramid[5])


out = out / out.max() * 255

out = out.astype(np.uint8)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.imwrite("out.jpg", out)
