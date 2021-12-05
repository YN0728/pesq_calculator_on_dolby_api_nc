import requests
from helpers.constants import API_KEY


def get_polished_recording(output_url):
    headers = {
        'Accept': 'application/json',
        'x-api-key': API_KEY
    }
    params = {'url': output_url}
    endpoint = 'https://api.dolby.com/media/output'
    response_content = requests.get(endpoint, headers=headers, params=params).content
    return response_content

