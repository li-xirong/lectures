from skimage import data, filter, transform, io
import matplotlib.pyplot as plt
import math
import numpy as np


image = io.imread('dolphins.jpg')
rotate0 = transform.rotate(image, 30)
rotate1 = transform.rotate(image, 60)

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 4))
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('input')

ax1.imshow(rotate0, cmap=plt.cm.gray)
ax1.set_title(r'$\theta=30$')

ax2.imshow(rotate1, cmap=plt.cm.gray)
ax2.set_title(r'$\theta=60$')

plt.tight_layout()
plt.savefig('%s.png' % __file__)
#plt.show()


