import requests
import json

def postData(data, gss_url):
    if(data is None):
        print("params is empty")
        return False
    payload = {
        "data": data
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(gss_url, data=json.dumps(payload), headers=headers)
    if(response.status_code == 200 and response.text == "success"):
        print("post succeeded")
        return True
    return False