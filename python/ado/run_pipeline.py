import requests
import base64
from dotenv import load_dotenv
import os


load_dotenv()

#url='https://dev.azure.com/{ORG}/{PRJ}/_apis/pipelines/{PID}/runs'


def encode_pat():
    data=":"+os.getenv("PAT")
    data_bytes = data.encode('ascii')
    base64_bytes = base64.b64encode(data_bytes)
    pat=base64_bytes.decode("utf-8")
    return pat 


def run_pipeline(pat):
    querystring = {"api-version":"7.0"}
    authorization_headers=f'Basic {pat}'
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
    url = os.getenv("URL") 
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    print(response.text)


pat=encode_pat()
run_pipeline(pat)
