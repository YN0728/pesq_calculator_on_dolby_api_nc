import json
import requests

from helpers.constants import API_KEY


def get_job_id(input_url, output_url):
    session = requests.Session()
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    session.headers.update(headers)
    endpoint = 'https://api.dolby.com/media/enhance'

    json_body = {
        "content": {
            "type": "voice_recording"
        },
        "audio": {
            "noise": {
                "reduction": {
                    "enable": True,
                    "amount": "max"
                }
            },
            "speech": {
                "isolation": {
                    "enable": True,
                    "amount": 100
                }
            }
        },
        "input": input_url,
        "output": output_url
    }

    response_body = requests.post(endpoint, data=json.dumps(json_body), headers=headers)
    if response_body.status_code != 200:
        raise Exception
    return dict(response_body.json()).get('job_id')
