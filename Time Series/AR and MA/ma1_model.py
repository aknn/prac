import numpy as np
import matplotlib.pyplot as plt

# Set parameters
n = 1000  # Number of observations
theta = 0.6  # MA(1) coefficient
mean = 0
std_dev = 1

# Generate white noise
eps = np.random.normal(mean, std_dev, n)

# Generate MA(1) process
x = np.zeros(n)
x[0] = eps[0]

for i in range(1, n):
    x[i] = eps[i] + theta * eps[i-1]

# Plot the MA(1) process
plt.figure(figsize=(10, 6))
plt.plot(x)
plt.title('MA(1) Process')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()