import numpy as np
import matplotlib.pyplot as plt

# Set the random seed for reproducibility
np.random.seed(42)

# Generate a random walk
n_steps = 1000
steps = np.random.choice([-1, 1], size=n_steps)
random_walk = np.cumsum(steps)

# Make the random walk stationary by taking the first difference
stationary_random_walk = np.diff(random_walk, n=1)

# Plot the stationary random walk
plt.figure(figsize=(12, 6))

# Plot the original random walk
plt.subplot(1, 2, 1)
plt.plot(random_walk)
plt.title('Non-Stationary Random Walk')

# Plot the differenced (stationary) random walk
plt.subplot(1, 2, 2)
plt.plot(stationary_random_walk)
plt.title('Stationary Random Walk')

plt.tight_layout()
plt.show()