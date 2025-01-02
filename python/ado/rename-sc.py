import requests
import base64
import os
import json
from dotenv import load_dotenv
from GenB64PAT import get_base64_pat

load_dotenv()

# Global vars
baseURL=os.getenv("baseURL")
organization=os.getenv("org")
project=os.getenv("project")
apiversion=os.getenv("apiversion")
pat=os.getenv("pat")

# local vars
#pipelineId="38" # definitionId
endpointId="EndpointID" # ARMSC-WI in PP1 


#base64_pat=get_base64_pat(pat)

def share_service_connection(endpointId):
    print(f"Sharing the Service Connection of {endpointId}")
    url = f"https://{baseURL}/{organization}/_apis/serviceendpoint/endpoints/{endpointId}?api-version={apiversion}"
    print(url)
    base64_pat=get_base64_pat(pat)
    payload = json.dumps([
        {
            "description": "PipelineDemo-ServiceConnection",
            "name": "ARMSCWIPP1",
            "projectReference": {
                "id": "fea40019-5244-4f3d-95df-d90c51fa9659",
                "name": "PipelineDemo"
            }
        },
        {
            "description": "Agile-ServiceConnection",
            "name": "AgileServiceConnection",
            "projectReference": {
                "id": "0104c47c-ebeb-4280-9c98-13c8fb18672b",
                "name": "Project1-Agile"
            }
        }
        ]
        )
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Basic {base64_pat}'
        }   
    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)


# main
share_service_connection(endpointId)
