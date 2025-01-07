import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def generate_ar1_process(n, phi, mean=0, std_dev=1):
    """
    Generate an AR(1) process.
    
    Parameters:
    -----------
    n : int
        Number of observations
    phi : float
        AR(1) coefficient (-1 < phi < 1)
    mean : float
        Mean of the white noise process
    std_dev : float
        Standard deviation of the white noise process
    
    Returns:
    --------
    numpy.ndarray
        Generated AR(1) process
    """
    if not -1 < phi < 1:
        raise ValueError("phi must be between -1 and 1")
    
    x = np.zeros(n)
    x[0] = np.random.normal(mean, std_dev)
    
    for i in range(1, n):
        x[i] = phi * x[i-1] + np.random.normal(mean, std_dev)
    
    return x

def analyze_ar1_process(x, phi):
    """Analyze the AR(1) process and create visualizations."""
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'AR(1) Process Analysis (φ={phi})')
    
    # Time series plot
    axs[0,0].plot(x)
    axs[0,0].set_title('Time Series Plot')
    axs[0,0].set_xlabel('Time')
    axs[0,0].set_ylabel('Value')
    
    # Autocorrelation plot
    lags = np.arange(20)
    acf = [np.corrcoef(x[:-k], x[k:])[0,1] for k in lags[1:]]
    axs[0,1].plot(lags[1:], acf, 'bo-')
    axs[0,1].set_title('Autocorrelation Function')
    axs[0,1].set_xlabel('Lag')
    axs[0,1].set_ylabel('ACF')
    
    # Histogram
    axs[1,0].hist(x, bins=30, density=True, alpha=0.7)
    xmin, xmax = axs[1,0].get_xlim()
    x_pdf = np.linspace(xmin, xmax, 100)
    axs[1,0].plot(x_pdf, stats.norm.pdf(x_pdf, np.mean(x), np.std(x)))
    axs[1,0].set_title('Distribution')
    
    # Scatter plot (x[t] vs x[t-1])
    axs[1,1].scatter(x[:-1], x[1:], alpha=0.5)
    axs[1,1].set_title('Lag Plot (x[t] vs x[t-1])')
    axs[1,1].set_xlabel('x[t-1]')
    axs[1,1].set_ylabel('x[t]')
    
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print(f"Mean: {np.mean(x):.3f}")
    print(f"Standard Deviation: {np.std(x):.3f}")
    print(f"First-order autocorrelation: {np.corrcoef(x[:-1], x[1:])[0,1]:.3f}")

if __name__ == "__main__":
    # Set parameters
    n = 1000
    phi = 0.8
    
    # Generate and analyze AR(1) process
    x = generate_ar1_process(n, phi)
    analyze_ar1_process(x, phi)