import numpy as np
from scipy import cumsum, sin, linspace
from scipy import pi as mpi
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

def make_sweepsound(A, fs, start_freq, end_freq, sec):
    """
    make sweepsound.

    prameters
    ---------------------
    A = 1     #振幅
    fs = 44100 #サンプリング周波数
    start_freq = 20  #始まりの周波数
    end_freq = 20000 #終わりの周波数
    sec = 5   #秒

    return
    ---------------------
    pink: sweepsine signal (numpy array float64)
    """
    
    freqs = linspace(start_freq, end_freq, num = int(round(fs * sec)))
    ### 角周波数の変化量
    phazes_diff = 2. * mpi * freqs / fs
    ### 位相
    phazes = cumsum(phazes_diff)
    ### サイン波合成
    ret = A * sin(phazes)

    return ret
