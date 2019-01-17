from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-7,7,100)
x2 = np.linspace(-7,0,100)
x3 = np.linspace(0,7,100)

y1 = x1**2
y2 = 1.1*x2**2 - 3
y3 = 0.9*x3**2 + 3

plt.plot(x1,y1,'--k')
plt.plot(x2,y2,'-r')
plt.plot(x3,y3,'-b')
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')
plt.plot((-5.5,5.5),(30.25,30.25),'--k')
plt.plot((0,6),(36,36),'-b')
plt.plot((-5,0),(25,25),'-r')

plt.annotate('$E_F$ down', xy=(-5,25), xytext=(-5,26), color='red') 
plt.annotate('$E_F$ up', xy=(4.5,36), xytext=(4.5,34), color='blue')
plt.annotate('Electrons flip spins', xytext=(2.5,33), xy=(-3.5,27), color='red', arrowprops=dict(facecolor='blue', shrink=0.05))
plt.annotate('k (up)', xy=(6,1), xytext=(6,1), color='black')
plt.annotate('k (down)', xy=(-5,1), xytext=(-5,1), color='black')
plt.annotate('E', xy=(0.1,37), xytext=(0.1,37), color='black')
plt.annotate('0',xy=(0,0),xytext=(0.1,-1),color='black')

plt.show()
