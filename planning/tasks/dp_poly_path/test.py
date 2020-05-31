import matplotlib.pyplot as plt 
import numpy as np
x = np.linspace(-5, 6, 200)
y = (0.4 + np.exp(-1.5* (x - 1.5))) / (1.0 + np.exp(-1.5* (x - 1.5)))
plt.plot(x, y)
plt.show()