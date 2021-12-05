from apis.check_job_status_api import wait_for_job_success
from apis.getting_polished_recording import get_polished_recording
from apis.noise_cancellation_api import get_job_id
from apis.response_to_audio import content_to_file
from helpers.constants import *


def get_processed_recording(recording_name):
    input_url = S3_AMAZON_BASE_PATH + recording_name
    output_url = OUTPUT_BASE_URL + recording_name

    print("Working on " + recording_name)
    job_id = get_job_id(input_url, output_url)
    wait_for_job_success(job_id)
    content = get_polished_recording(output_url)

    content_to_file(PROCESSED_RECORDING_PATH + recording_name, content)
