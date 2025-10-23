import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3,4,5],[1,4,9,50,2], 'g-', linewidth=4.0 )
plt.axis([0,10,0,60])
plt.ylabel('Some numbers')
plt.xlabel('A meaningless axis')
plt.show()