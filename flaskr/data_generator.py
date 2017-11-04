import numpy as np
from swan import pycwt

def generate_data():
    # reference: https://qiita.com/yukiB/items/59f8484e72bb0471ad47
    x = np.arange(0, 20, 0.01)
    y = np.sin(2 * np.pi * 1 * x) * 2 + np.sin(2 * np.pi * 2 * x) * 2  + np.cos(2 * np.pi * 10 * x)

    # sampling frequency
    Fs = 1/0.01
    omega0 = 8
    # frequency axis
    freqs = np.arange(0.1,20,0.025)
    # time axis
    time = x
    # value axis
    value = y
    # do cwt
    r = pycwt.cwt_f(y,freqs,Fs,pycwt.Morlet(omega0))
    rr = np.abs(r)
    return time,value,freqs,rr
