import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt

# Parameters
n_periods = 100  # number of periods
sigma_w = 20     # standard deviation of the white noise
phi = 0.8        # AR(1) coefficient

# Simulate the linear trend T_t
t = np.arange(n_periods)
T_t = 50 + 3 * t

# Simulate the AR(1) process Y_t
np.random.seed(0)
W_t = np.random.normal(scale=sigma_w, size=n_periods)
Y_t = np.zeros(n_periods)
for i in range(1, n_periods):
    Y_t[i] = phi * Y_t[i-1] + W_t[i]
    print(f"Y_t[{i}] = {phi} * Y_t[{i-1}] + W_t[{i}] = {phi} * {Y_t[i-1]} + {W_t[i]} = {Y_t[i]}")

# Combine to get X_t
X_t = T_t + Y_t
# plot the simulated data
plt.figure(figsize=(12, 6))
plt.plot(X_t)
plt.title('Simulated Data')
plt.xlabel('Time')
plt.ylabel('X_t')
plt.show()


# Fit an AR(1) model to the simulated data (without the trend component)
# Since we know the process includes a deterministic trend, we can first detrend the data.
X_t_detrended = X_t - T_t

# Fit the AR(1) model to the detrended data
model = ARIMA(X_t_detrended, order=(1, 0, 0))
fit = model.fit()

# Get the residuals
residuals = fit.resid

# Plot the ACF of the residuals
plot_acf(residuals, lags=20, alpha=0.05)
plt.title('ACF of Residuals')
plt.show()
