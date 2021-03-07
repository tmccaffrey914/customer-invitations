import json
import requests
from requests import HTTPError


def yield_json_from_url(url):
    response = requests.get(url, stream=True)

    if response.encoding is None:
        # Server didn't provide Encoding Info
        response.encoding = 'utf-8'

    if response.status_code in range(200, 300):
        for line in response.iter_lines(decode_unicode=True):
            if line:
                yield json.loads(line)
    else:
        raise HTTPError
