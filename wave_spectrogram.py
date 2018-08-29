import matplotlib.pyplot as plot
from scipy.io import wavfile

samplingFrequency, signalData = wavfile.read('E:/mazhar/Workspace/audiosamples/afnan/AUD-20180825-WA0004.wav')

plot.subplot(211)
plot.title('WA0004')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency)
plot.xlabel('Time')
plot.ylabel('Frequency')
plot.show()
