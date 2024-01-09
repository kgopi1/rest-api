import requests

url = "https://dev.azure.com/KGDL02/PP1/_apis/pipelines/38/runs"

querystring = {"api-version":"7.0"}

payload = {
    "resources": {"repositories": {"self": {"refName": "refs/heads/main"}}},
    "templateParameters": {
        "name": "gopi-rest-api",
        "school": "sbioa"
    }
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic <token>"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
# print response 
print(response.text)
