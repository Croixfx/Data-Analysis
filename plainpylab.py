import pylab as pl
import numpy as np

x1 = [2,15,5,20,5,30,26,60]
y1 = [1,5,10,18,20,25,26,27]
x2 = [3,20,6,15,9,30,50,62]
y2 = [2,6,11,20,22,26,25,30]

pl.axis([0,65,0,65])
pl.plot(x1,y1,'b*', x2,y2,'ro')
pl.show()