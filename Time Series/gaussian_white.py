import numpy as np

# Set the parameters
np.random.seed(0)  # For reproducibility
n_samples = 1000   # Number of samples
mean = 0           # Mean of the distribution
std_dev = 1        # Standard deviation of the distribution

# Generate white noise
white_noise = np.random.normal(mean, std_dev, size=n_samples)

import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Calculate and plot the autocorrelation function
plot_acf(white_noise, lags=50)
plt.title('Autocorrelation Function (ACF) of White Noise')
plt.xlabel('Lags')
plt.ylabel('ACF')
plt.show()