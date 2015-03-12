from skimage import data, filter
import matplotlib.pyplot as plt

image = data.coins()
edges = filter.sobel(image)

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('input')

ax1.imshow(edges, cmap=plt.cm.gray)
ax1.set_title('output')

plt.tight_layout()
plt.savefig('plot_filter.png')
plt.show()


