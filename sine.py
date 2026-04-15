from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd

sampleR = 48000
duration = 1

frequency = 440

t = np.linspace(0, duration, int(sampleR * duration), endpoint = False)

amplitude = 0.25

wave = amplitude * np.sin(2 * np.pi * frequency * t)

wave_int16 = np.int16(wave * 32767)

write("sine.wav", sampleR, wave_int16)

amplitude = 0.5

wave = amplitude * np.sin(2 * np.pi * frequency * t)

clipped = np.clip(wave, -0.25, 0.25)

wave_int16 = np.int16(clipped * 32767)

write("clipped.wav", sampleR, wave_int16)

sd.play(clipped, samplerate=sampleR)
sd.wait()