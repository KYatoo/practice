import wave
from playsound import playsound
import numpy as np
import pylab as pl

screenshot = wave.open('./screenshot.wav', 'rb')
params = screenshot.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
# print(params)
str_data = screenshot.readframes(nframes)
wave_data = np.frombuffer(str_data, dtype=np.short)
# playsound("screenshot.wav")
wave_data.shape = -1, 2
wave_data = wave_data.T[0]
time = np.arange(0, nframes) * (1.0 / framerate)
print(len(time), len(wave_data))
print(time)
print(wave_data)
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()

