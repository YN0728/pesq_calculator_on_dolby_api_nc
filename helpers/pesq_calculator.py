from scipy.io import wavfile
from pesq import pesq

from helpers.constants import EXISTING_RECORDING_PATH, PROCESSED_RECORDING_PATH


def pesq_calculator(recording):
    rate, ref = wavfile.read(EXISTING_RECORDING_PATH + recording)
    rate, deg = wavfile.read(PROCESSED_RECORDING_PATH + recording)
    pesq_wide_band = pesq(rate, ref, deg, 'wb')
    pesq_narrow_band = pesq(rate, ref, deg, 'nb')
    return pesq_wide_band, pesq_narrow_band
