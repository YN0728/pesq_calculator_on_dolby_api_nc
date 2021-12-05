import glob
import os

from helpers.constants import EXISTING_RECORDING_PATH
from helpers.get_processed_recording import get_processed_recording
from helpers.pesq_calculator import pesq_calculator


def processing_existing_data():

    final_results = {}
    audios = glob.glob(EXISTING_RECORDING_PATH + '*wav')
    for i in audios:
        file_name = os.path.basename(i)
        get_processed_recording(file_name)
        wide_band, narrow_band = pesq_calculator(file_name)
        final_results[file_name] = {
            "narrow_band": narrow_band,
            "wide_band": wide_band
        }

    return final_results
