from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

N, Wn = signal.cheb1ord(0.2, 0.3, 3, 40)
b, a = signal.cheby1(N, 3, Wn, 'low')
w, h = signal.freqz(b, a)
plt.semilogx(w / np.pi, 20 * np.log10(abs(h)))
plt.title('Chebyshev I lowpass filter fit to constraints')
plt.xlabel('Normalized frequency')
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.fill([.01, 0.2, 0.2, .01], [-3, -3, -99, -99], '0.9', lw=0) # stop
plt.fill([0.3, 0.3,   2,   2], [ 9, -40, -40,  9], '0.9', lw=0) # pass
plt.axis([0.08, 1, -60, 3])
plt.show()
