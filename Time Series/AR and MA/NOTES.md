## AR and MA Models 

### Autoregressive (AR) Models

An autoregressive model is a type of time series model where the current value of the series depends on its own previous values. The order of an AR model, denoted as AR(p), indicates the number of lagged values used in the model.

The general form of an AR(p) model is:

X(t) = c + φ₁X(t-1) + φ₂X(t-2) + ... + φₚX(t-p) + ε(t)

where:
- X(t) is the current value of the time series
- c is a constant
- φ₁, φ₂, ..., φₚ are the coefficients of the lagged values
- ε(t) is white noise

Python script for generating an AR(1) model:

[ar1_model.py](./ar1_model.py)

```python
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
```

### Moving Average (MA) Models

A moving average model is another type of time series model where the current value of the series depends on the past errors or residuals. The order of an MA model, denoted as MA(q), indicates the number of lagged errors used in the model.

The general form of an MA(q) model is:

X(t) = μ + ε(t) + θ₁ε(t-1) + θ₂ε(t-2) + ... + θₚε(t-q)

where:
- X(t) is the current value of the time series
- μ is the mean of the series
- ε(t), ε(t-1), ..., ε(t-q) are the white noise errors
- θ₁, θ₂, ..., θₚ are the coefficients of the lagged errors

Python script for generating an MA(1) model:

[ma1_model.py](./ma1_model.py)

```python
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
```
