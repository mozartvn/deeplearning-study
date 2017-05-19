import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = -np.log10(x)

plt.plot(x, y)
plt.plot(x, np.zeros_like(x), 'b')
plt.plot(np.zeros_like(y), y, 'b')
plt.plot(1, 0, 'rx')
plt.show()

