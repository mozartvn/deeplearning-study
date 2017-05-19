import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on sine and cosine cureves

#signmoid
x = np.arange(-15, 15, 0.1)
sig_y = 1 / ( 1 + np.exp(x))

#tanh
tan_y = np.tanh(x)


# Plot the points using matplotlib
plt.plot(x, np.zeros_like(x))
plt.plot(np.zeros_like(x), x)

plt.plot(x, sig_y, 'r')
plt.plot(x, tan_y, 'b')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Signmoid Activation')
plt.show()