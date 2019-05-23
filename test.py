import numpy as np
import matplotlib.pyplot as plt

v=np.arange(20,120,5)
f=0.009+0.0012*v/100+0.0012*(v/100)**4

plt.plot(v,f,'r-')
plt.show()