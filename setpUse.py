import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)

# lines = plt.plot(t,t, 'bo', t, t**2, 'r+', t, t**3,'gx')
# plt.setp(lines, 'color', 'r', 'linewidth',2.0)
plt.plot(t,t, 'b-', linewidth=2.0, label = 'Thing1')
plt.plot(t,t**2,'r-',linewidth=2.0,label='Thing 2')
plt.plot(t,t**3,'g-',linewidth=2.0,label='Thing 3')

plt.text(1,80,'Croix with Sharoze')
plt.annotate('Divergence point', xy=(1.4,3), xytext= (3, 1.4), arrowprops=dict(facecolor='black', shrink=0.05))
plt.legend(bbox_to_anchor=(1.05,1), loc=2,borderaxespad=0.5)
plt.tight_layout()
plt.savefig('test.png')
plt.show()