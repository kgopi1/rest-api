# Python REST Api call to get list of azure devops projects 

import requests
import base64
import os
import json
from dotenv import load_dotenv
from GenB64PAT import get_base64_pat

load_dotenv()

# Global vars
baseUrl=os.getenv("baseURL")
organization=os.getenv("org")
project=os.getenv("project")
apiversion=os.getenv("apiversion")
pat=os.getenv("pat")

# local vars


def get_ado_projects():
    url = f"https://{baseUrl}/{organization}/_apis/projects?api-version={apiversion}"
    base64_pat=get_base64_pat(pat)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Basic {base64_pat}'
        }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


get_ado_projects()
