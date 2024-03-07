import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Seed the random number generator for reproducibility
np.random.seed(42)

# Simulate a random walk
n_steps = 1000
epsilon = np.random.normal(loc=0, scale=1, size=n_steps)
random_walk = np.cumsum(epsilon)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))  # 1 row, 2 columns

# Plot the random walk on the first subplot
ax1.plot(random_walk)
ax1.set_title('Random Walk')
ax1.set_xlabel('Time')
ax1.set_ylabel('Value')

# Plot the ACF on the second subplot
plot_acf(random_walk, lags=50, ax=ax2)
ax2.set_title('Autocorrelation Function')

# Display the plots side by side
plt.tight_layout()
plt.show()