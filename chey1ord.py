from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


N, Wn = signal.cheb2ord([0.1, 0.6], [0.2, 0.5], 3, 60)
b, a = signal.cheby2(N, 60, Wn, 'stop')
w, h = signal.freqz(b, a)
plt.semilogx(w / np.pi, 20 * np.log10(abs(h)))
plt.title('Chebyshev II bandstop filter fit to constraints')
plt.xlabel('Normalized frequency')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.fill([.01, .1, .1, .01], [-3,  -3, -99, -99], '0.9', lw=0) # stop
plt.fill([.2,  .2, .5,  .5], [ 9, -60, -60,   9], '0.9', lw=0) # pass
plt.fill([.6,  .6,  2,   2], [-99, -3,  -3, -99], '0.9', lw=0) # stop
plt.axis([0.06, 1, -80, 3])
plt.show()
