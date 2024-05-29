"""
THE FOLLOWING CODE IS NOT NEEDED AS IT IS JUST A TESTING SCRIPT DURING DEVELOPEMENT
"""
import requests
import json

url = "http://127.0.0.1:5001"
data = {
    "token": "mytoken",
    "request": "get",
    "content": '{"tmp": "tmp"}'
}
response = requests.post(url, json=data)
print(response.text)