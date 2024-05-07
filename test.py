import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 30, 1000)
Y = np.sin(X)

fig, ax = plt.subplots()
ax.plot(X, Y, color='blue')
ax.set_title('Original Image')

fig.savefig("fig.png")
plt.show()
