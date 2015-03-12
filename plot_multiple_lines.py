"""
Demo using fontdict to control style of text and labels.
"""
import numpy as np
import matplotlib.pyplot as plt


COLORS = ['green', 'blue', 'red']

font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 16,
        }

x = np.linspace(0.0, 5.0, 50)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

for k, b, color in zip([0.5, 1, 1.5], [0,0,0], COLORS):
    y = k*x + b
    if abs(k-1)<1e-6:
        label = r'$y=x$'
    else:
        label=r'$y=%g x$'%k
    ax.plot(x, y, label=label, color=color)

ax.set_ylim([0, max(x)])
plt.legend(loc='upper left')

#ax.spines['right'].set_visible(False)
#ax.spines['top'].set_visible(False)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear transformation functions')
plt.savefig('plot_multiple_lines.png', bbox_inches='tight')
#plt.show()

    