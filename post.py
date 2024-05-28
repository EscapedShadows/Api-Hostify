"""
THE FOLLOWING CODE IS NOT NEEDED AS IT IS JUST A TESTING SCRIPT DURING DEVELOPEMENT
"""

import requests

url = "http://127.0.0.1:5000"
data = {
    "token": "mytoken",
    "request": "create"
}

response = requests.post(url,json=data)

print(response)
print(response.json())