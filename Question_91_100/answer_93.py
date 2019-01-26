import numpy as np

# [x1, y1, x2, y2]
a = np.array((50, 50, 150, 150), dtype=np.float32)

b = np.array((60, 60, 170, 160), dtype=np.float32)

def iou(a, b):
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    iou_x1 = np.maximum(a[0], b[0])
    iou_y1 = np.maximum(a[1], b[1])
    iou_x2 = np.minimum(a[2], b[2])
    iou_y2 = np.minimum(a[3], b[3])
    iou_w = iou_x2 - iou_x1
    iou_h = iou_y2 - iou_y1
    area_iou = iou_w * iou_h
    iou = area_iou / (area_a + area_b - area_iou)

    return iou

print(iou(a, b))
