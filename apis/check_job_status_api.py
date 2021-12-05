import requests
import time
from helpers.constants import API_KEY


def wait_for_job_success(job_id):
    headers = {
        'Accept': 'application/json',
        'x-api-key': API_KEY
    }
    params = {'job_id': job_id}
    endpoint = 'https://api.dolby.com/media/enhance'
    time.sleep(2)
    status = requests.get(endpoint, headers=headers, params=params).json().get('status')
    while status == 'Running':
        status = requests.get(endpoint, headers=headers, params=params).json().get('status')
        time.sleep(2)
    if status == "Success":
        print("Done!")
        return
    else:
        raise Exception
