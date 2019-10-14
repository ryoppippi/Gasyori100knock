import cv2
import numpy as np

# motion filter
def motion_filter(img, K_size=3):
    H, W, C = img.shape

    # Kernel
    K = np.diag( [1] * K_size ).astype(np.float)
    K /= K_size

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


# Read image
img = cv2.imread("imori.jpg")

# motion filtering
out = motion_filter(img, K_size=3)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
