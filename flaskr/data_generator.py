import numpy as np
from swan import pycwt

def cwt(time,value,omega0=8,wavelet_type="morlet",f_min=0.1,f_res=50):
    # sampling frequency
    Fs = 1/(time[1] - time[0])
    Fs_n = Fs/2  #nyquist
    # select wavelet
    if wavelet_type == "morlet":
        wavelet = pycwt.Morlet(omega0)
    else:
        raise NotImplementedError()
    # frequency
    freqs = np.linspace(f_min,Fs_n,f_res)
    # do cwt
    r = pycwt.cwt_f(value,freqs,Fs,wavelet)
    rr = np.abs(r)
    return freqs,rr

def generate_data():
    # reference: https://qiita.com/yukiB/items/59f8484e72bb0471ad47
    x1 = np.arange(0, 10, 0.01)
    y1 = np.sin(2 * np.pi * 1 * x1) * 2 + np.sin(2 * np.pi * 2 * x1) * 2  + np.cos(2 * np.pi * 10 * x1)
    x2 = np.arange(10,20,0.01)
    y2 = np.sin(2 * np.pi * 3 * x2) * 3
    x3 = np.arange(20,30,0.01)
    y3 = np.sin(2 * np.pi * 10 * x3) * 2 + np.sin(2 * np.pi * 3 * x3) * 2

    x = np.concatenate([x1,x2,x3])
    y = np.concatenate([y1,y2,y3])

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
    # r = pycwt.cwt_f(y,freqs,Fs,pycwt.Morlet(omega0))
    # rr = np.abs(r)
    rr = np.random.rand(x.shape[0],freqs.shape[0])
    return time,value,freqs,rr
