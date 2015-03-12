"""
Demo using fontdict to control style of text and labels.
"""
import numpy as np
import matplotlib.pyplot as plt


font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

x = np.linspace(0.0, 5.0, 100)
y = -x

plt.plot(x, y, 'k')
plt.xlabel('x', fontdict=font)
plt.ylabel('y', fontdict=font)
plt.title(r'$y=-x$', fontdict=font)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.savefig('plot_line.png')
plt.show()
