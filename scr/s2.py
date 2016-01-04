"""
Plot
"""
#Plots a stereo .wav file
#Decibels on the y-axis
#Frequency Hz on the x-axis

import matplotlib.pyplot as plt
import numpy as np

from pylab import*
from scipy.io import wavfile


def plot(file_name):

    sampFreq, snd = wavfile.read(file_name)

    snd = snd / (2.**15) #convert sound array to float pt. values

    s1 = snd[:,0] #left channel

    s2 = snd[:,1] #right channel

    n = len(s1)
    p = fft(s1) # take the fourier transform of left channel

    m = len(s2)
    p2 = fft(s2) # take the fourier transform of right channel

    nUniquePts = ceil((n+1)/2.0)
    p = p[0:nUniquePts]
    p = abs(p)

    mUniquePts = ceil((m+1)/2.0)
    p2 = p2[0:mUniquePts]
    p2 = abs(p2)
    '''
    Left Channel
    '''
    p = p / float(n) # scale by the number of points so that
             # the magnitude does not depend on the length
             # of the signal or on its sampling frequency
    p = p**2  # square it to get the power
    # multiply by two (see technical document for details)
    # odd nfft excludes Nyquist point
    if n % 2 > 0: # we've got odd number of points fft
        p[1:len(p)] = p[1:len(p)] * 2
    else:
        p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

    freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
    plt.plot(freqArray/1000, 10*log10(p), color='k')
    plt.xlabel('LeftChannel_Frequency (kHz)')
    plt.ylabel('LeftChannel_Power (dB)')
    plt.show()
    '''
    Right Channel
    '''
    p2 = p2 / float(m) # scale by the number of points so that
             # the magnitude does not depend on the length
             # of the signal or on its sampling frequency
    p2 = p2**2  # square it to get the power
    # multiply by two (see technical document for details)
    # odd nfft excludes Nyquist point
    if m % 2 > 0: # we've got odd number of points fft
         p2[1:len(p2)] = p2[1:len(p2)] * 2
    else:
         p2[1:len(p2) -1] = p2[1:len(p2) - 1] * 2 # we've got even number of points fft

    freqArray2 = arange(0, mUniquePts, 1.0) * (sampFreq / m);
    plt.plot(freqArray2/1000, 10*log10(p2), color='k')
    plt.xlabel('RightChannel_Frequency (kHz)')
    plt.ylabel('RightChannel_Power (dB)')
    plt.show()


plot('./Downloads/k13.wav')
