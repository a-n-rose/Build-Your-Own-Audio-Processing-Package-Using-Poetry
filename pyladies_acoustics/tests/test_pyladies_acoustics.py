from pyladies_acoustics import __version__
import pyladies_acoustics as pa
import numpy as np

def test_version():
    assert __version__ == '0.1.0'
    
def test_amplitude_doubled():
    x = np.ones((5,))
    y = pa.audio_fun.adjust_amplitude(
        x,
        2)
    expected = np.array([2,2,2,2,2])
    assert np.array_equal(y,expected)

def test_amplitude_halved():
    x = np.ones((5,))
    y = pa.audio_fun.adjust_amplitude(
        x,
        0.5)
    expected = np.array([0.5,0.5,0.5,0.5,0.5])
    assert np.array_equal(y,expected)
