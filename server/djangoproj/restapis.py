import requests
import json
from django.conf import settings

def get_request(url, **kwargs):
    print(f"GET from {url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print(f"With status {status_code}")
    json_data = json.loads(response.text)
    return json_data

def post_request(url, json_payload, **kwargs):
    print(f"POST to {url}")
    try:
        response = requests.post(url, params=kwargs, json=json_payload)
    except:
        print("Network exception occurred")
    status_code = response.status_code
    print(f"With status {status_code}")
    json_data = json.loads(response.text)
    return json_data