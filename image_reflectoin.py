import sys
from skimage import data, filter, transform, io
import matplotlib.pyplot as plt
import math
import numpy as np


image = io.imread('dolphins.jpg')
height, width, depth = image.shape

A = np.matrix([ [-1, 0, width], [0, 1, 0], [0, 0, 1]])
tform = transform.AffineTransform(A)
h_flip = transform.warp(image, tform)

A = np.matrix([ [1, 0, 0], [0, -1, height], [0, 0, 1]])
tform = transform.AffineTransform(A)
v_flip = transform.warp(image, tform)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 4))
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('input')

ax1.imshow(h_flip, cmap=plt.cm.gray)
ax1.set_title(r'horizontal flip')

ax2.imshow(v_flip, cmap=plt.cm.gray)
ax2.set_title(r'vertical flip')

plt.tight_layout()
plt.savefig('%s.png' % __file__)
#plt.show()


