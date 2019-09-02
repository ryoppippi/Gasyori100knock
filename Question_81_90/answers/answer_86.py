import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# Dicrease color
def dic_color(img):
    img //= 63
    img = img * 64 + 32
    return img

# Database
def get_DB():
    # get training image path
    train = glob("dataset/train_*")
    train.sort()

    # prepare database
    db = np.zeros((len(train), 13), dtype=np.int32)

    # prepare path database
    pdb = []

    # each image
    for i, path in enumerate(train):
        # read image
        img = dic_color(cv2.imread(path))

        #get histogram
        for j in range(4):
            db[i, j] = len(np.where(img[..., 0] == (64 * j + 32))[0])
            db[i, j+4] = len(np.where(img[..., 1] == (64 * j + 32))[0])
            db[i, j+8] = len(np.where(img[..., 2] == (64 * j + 32))[0])

        # get class
        if 'akahara' in path:
            cls = 0
        elif 'madara' in path:
            cls = 1

        # store class label
        db[i, -1] = cls

        # store image path
        pdb.append(path)

    return db, pdb

# test
def test_DB(db, pdb):
    # get test image path
    test = glob("dataset/test_*")
    test.sort()

    accurate_N = 0.

    # each image
    for path in test:
        # read image
        img = dic_color(cv2.imread(path))

        # get histogram
        hist = np.zeros(12, dtype=np.int32)
        for j in range(4):
            hist[j] = len(np.where(img[..., 0] == (64 * j + 32))[0])
            hist[j+4] = len(np.where(img[..., 1] == (64 * j + 32))[0])
            hist[j+8] = len(np.where(img[..., 2] == (64 * j + 32))[0])

        # get histogram difference
        difs = np.abs(db[:, :12] - hist)
        difs = np.sum(difs, axis=1)

        # get argmin of difference
        pred_i = np.argmin(difs)

        # get prediction label
        pred = db[pred_i, -1]

        if pred == 0:
            pred_label = "akahara"
        elif pred == 1:
            pred_label = "madara"

        gt = "akahara" if "akahara" in path else "madara"

        if gt == pred_label:
            accurate_N += 1
        
        print(path, "is similar >>", pdb[pred_i], " Pred >>", pred_label)

    accuracy = accurate_N / len(test)
    print("Accuracy >>", accuracy, "({}/{})".format(int(accurate_N), len(test)))

db, pdb = get_DB()
test_DB(db, pdb)


