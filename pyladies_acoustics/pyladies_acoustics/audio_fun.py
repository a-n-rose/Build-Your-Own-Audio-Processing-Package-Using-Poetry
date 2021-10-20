"""Module for audio functionality
"""
from scipy.io.wavfile import read

def load_audio(pathway):
    """Returns `samples` and `sampling_rate` of .wav `pathway`.
    """
    sampling_rate, samples = read(pathway)
    return samples, sampling_rate
 
def adjust_amplitude(samples, amount):
    """Multiplies amplitude values in `samples` by `amount`.
    """
    samps = samples.copy()
    samps = samps * amount
    return samps
