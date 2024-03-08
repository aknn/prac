import numpy as np
import matplotlib.pyplot as plt

# Set parameters
n = 1000  # Number of observations
phi = 0.8  # AR(1) coefficient
mean = 0
std_dev = 1

# Generate AR(1) process
x = np.zeros(n)
x[0] = np.random.normal(mean, std_dev)

for i in range(1, n):
    x[i] = phi * x[i-1] + np.random.normal(mean, std_dev)

# Plot the AR(1) process
plt.figure(figsize=(10, 6))
plt.plot(x)
plt.title('AR(1) Process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()