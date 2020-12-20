import requests
import json


def postData(url: str, data) -> bool:
    if(data is None):
        print("params is empty")
        return False
    payload: dict = {
        "data": data
    }
    headers: dict = {
        'Content-Type': 'application/json',
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers)
    if(response.status_code == 200 and response.text == "success"):
        print("post succeeded")
        return True
    return False
