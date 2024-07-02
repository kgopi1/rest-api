import requests
import base64
from dotenv import load_dotenv
import os

url = "https://dev.azure.com/KGDL02/PP1/_apis/pipelines/38/runs"
load_dotenv()


def encode_pat():
    data=":"+os.getenv("PAT")
    data_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(data_bytes)
    pat=base64_bytes.decode("utf-8")
    return pat 


def run_pipeline(pat):
    querystring = {"api-version":"7.0"}
    authorization_headers=f'Basic {pat}'
    print(authorization_headers)
    payload = {
        "resources": {"repositories": {"self": {"refName": "refs/heads/main"}}},
        "templateParameters": {
            "name": "gopi-rest-api-2-Jul",
            "school": "sbioa"
        }
    }
    headers = {
        "Content-Type": "application/json",
       "Authorization": f"{authorization_headers}"
    }   
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    print(response.text)


pat=encode_pat()
run_pipeline(pat)
