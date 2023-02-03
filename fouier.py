import numpy as np
import matplotlib.pyplot as plt

# Define the function to be transformed
def f(x):
    return np.sin(x)

# Discretize the function
N = 512
x = np.linspace(0, 2*np.pi, N)
y = f(x)

# Compute the Fourier transform
Y = np.fft.fft(y)

# Plot the original and transformed functions
plt.figure()
plt.plot(x, y)
plt.title("Original function")

plt.figure()
plt.plot(x, np.abs(Y))
plt.title("Fourier transform of the function")

plt.show()