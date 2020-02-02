import numpy as np
import scipy.fftpack as fft

def whitenoise(t, fs):
    """
    This program makes white noise.

    prameters
    ---------------------
    t: time[s] (int or float)
    fs: sampling frequency[Hz] (int or float)

    return
    ---------------------
    white: white noise (numpy array float64)
    """
    tap = int(t*fs)
    white = np.random.randn(tap)
    white /= np.max(np.abs(white))
    return white

def pinknoise(t, fs):
    """
    This program makes pink noise.

    prameters
    ---------------------
    t: time[s] (int or float)
    fs: sampling frequency[Hz] (int or float)

    return
    ---------------------
    pink: pink noise (numpy array float64)
    """
    tap = int(t*fs)
    white = mkwhite(t, fs)
    WHITE = fft.fft(white)
    pink_filter = np.concatenate((np.array([1]), 1/np.sqrt(np.arange(start=fs/tap, stop=fs, step=fs/tap))))
    PINK = WHITE * pink_filter
    pink = np.real(fft.ifft(PINK))
    pink /= np.max(np.abs(pink))
    return pink
