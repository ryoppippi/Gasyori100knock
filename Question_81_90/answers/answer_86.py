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
pdb = []

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
    pdb.append(path)

## test
test = glob("dataset/test_*")
test.sort()

success_num = 0.

for path in test:
    img = dic_color(cv2.imread(path))

    hist = np.zeros(12, dtype=np.int32)
    for j in range(4):
        hist[j] = len(np.where(img[..., 0] == (64 * j + 32))[0])
        hist[j+4] = len(np.where(img[..., 1] == (64 * j + 32))[0])
        hist[j+8] = len(np.where(img[..., 2] == (64 * j + 32))[0])

    ## compute difference
    difs = np.abs(db[:, :12] - hist)
    difs = np.sum(difs, axis=1)
    pred_i = np.argmin(difs)
    pred = db[pred_i, -1]

    if pred == 0:
        pl = "akahara"
    elif pred == 1:
        pl = "madara"
    
    print(path, "is similar >>", pdb[pred_i], " Pred >>", pl)

    ## Count success
    gt = "akahara" if "akahara" in path else "madara"
    if gt == pl:
        success_num += 1.

accuracy = success_num / len(test)
print("Accuracy >>", accuracy, "({}/{})".format(int(success_num), len(test)))
