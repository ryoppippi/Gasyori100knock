import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

## Dicrease color
def dic_color(img):
    img //= 63
    img = img * 64 + 32
    return img

## Database
train = glob("dataset/train_*")
train.sort()

db = np.zeros((len(train), 13), dtype=np.int32)

for i, path in enumerate(train):
    img = dic_color(cv2.imread(path))
    ## histogram
    for j in range(4):
        db[i, j] = len(np.where(img[..., 0] == (64 * j + 32))[0])
        db[i, j+4] = len(np.where(img[..., 1] == (64 * j + 32))[0])
        db[i, j+8] = len(np.where(img[..., 2] == (64 * j + 32))[0])

    ## class
    if 'akahara' in path:
        cls = 0
    elif 'madara' in path:
        cls = 1
    db[i, -1] = cls

    img_h = img.copy() // 64
    img_h[..., 1] += 4
    img_h[..., 2] += 8
    plt.subplot(2, 5, i+1)
    plt.hist(img_h.ravel(), bins=12, rwidth=0.8)
    plt.title(path)

print(db)
plt.show()


