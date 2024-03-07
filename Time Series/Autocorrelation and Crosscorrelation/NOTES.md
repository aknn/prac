
# Autocorrelation and Crosscorrelation Notes


## Introduction

Autocorrelation and crosscorrelation are essential concepts in time series analysis. Autocorrelation measures the correlation of a signal with a delayed copy of itself, while crosscorrelation measures the correlation between two different signals. These techniques help in identifying patterns, trends, and relationships within and between time series data.

## White Noise Autocorrelation

White noise is a random signal with a constant power spectral density. In the context of autocorrelation, white noise has a theoretical autocorrelation function (ACF) where all lags are zero except for lag 0 (which is 1 due to normalization). However, due to random variations, you will see small non-zero values at different lags in the plot, which should not be significant and should not show any pattern as illustrated below:

![White Noise Autocorrelation](./images/white_ACF.png)

Python script for white noise autocorrelation here: [gaussian_white.py](./gaussian_white.py)

## Crosscorrelation

Crosscorrelation is a measure of similarity between two different time series as a function of the displacement of one relative to the other. It is used to find the relationship between two signals and determine if they are related or if one signal is influencing the other. Crosscorrelation can help in identifying time delays, phase differences, and common periodicities between two time series.

The crosscorrelation function (CCF) is computed by sliding one signal over the other and calculating the dot product at each shift. The resulting CCF will have peaks at lags where the signals are most similar and valleys where they are most dissimilar. The magnitude of the peaks indicates the strength of the correlation, while the lag at which the peak occurs represents the time delay between the signals.

Crosscorrelation is widely used in various fields, such as signal processing, pattern recognition, and econometrics, to analyze the relationship between different time series and extract meaningful insights from the data.