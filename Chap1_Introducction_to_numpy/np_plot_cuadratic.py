import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, num=100)[:,None]
y = 0.5 + 2.2*x + 0.3*x**3 + 2*np.random.randn(100, 1)

plt.plot(x, y)
plt.show()