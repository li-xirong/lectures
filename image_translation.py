import sys
from skimage import data, filter, transform, io
import matplotlib.pyplot as plt
import math
import numpy as np


image = io.imread('dolphins.jpg')
height, width, depth = image.shape

tform = transform.AffineTransform(translation=(-width/4,-height/4))
res1 = transform.warp(image, tform)

tform = transform.AffineTransform(translation=(-width/2, 0))
res2 = transform.warp(image, tform)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 4))
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('input')

ax1.imshow(res1, cmap=plt.cm.gray)
ax1.set_title(r'dx=w/4,dy=w/4')

ax2.imshow(res2, cmap=plt.cm.gray)
ax2.set_title(r'dx=w/2,dy=0')

plt.tight_layout()
plt.savefig('%s.png' % __file__)
#plt.show()


