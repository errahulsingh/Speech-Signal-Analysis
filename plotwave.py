#https://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

fig = plt.figure()

spf = wave.open('E:/mazhar/Workspace/audiosamples/afnan/AUD-20180825-WA0001.wav','r')

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')

ax = fig.add_subplot(2, 2, 1)
ax.set_title('AUD-20180825-WA0001')
ax.plot(signal)

##############

spf2 = wave.open('E:/mazhar/Workspace/audiosamples/afnan/AUD-20180825-WA0002.wav','r')

signal2 = spf2.readframes(-1)
signal2 = np.fromstring(signal2, 'Int16')

ax = fig.add_subplot(2, 2, 2)
ax.set_title('AUD-20180825-WA0002')
ax.plot(signal2)


##############

spf2 = wave.open('E:/mazhar/Workspace/audiosamples/afnan/AUD-20180825-WA0003.wav','r')

signal2 = spf2.readframes(-1)
signal2 = np.fromstring(signal2, 'Int16')

ax = fig.add_subplot(2, 2, 3)
ax.set_title('AUD-20180825-WA0003')
ax.plot(signal2)

##############

spf2 = wave.open('E:/mazhar/Workspace/audiosamples/afnan/AUD-20180825-WA0004.wav','r')

signal2 = spf2.readframes(-1)
signal2 = np.fromstring(signal2, 'Int16')

ax = fig.add_subplot(2, 2, 4)
ax.set_title('AUD-20180825-WA0004')
ax.plot(signal2)

plt.show()
