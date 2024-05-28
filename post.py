"""
THE FOLLOWING CODE IS NOT NEEDED AS IT IS JUST A TESTING SCRIPT DURING DEVELOPEMENT
"""

import requests


def setData():
    url = "http://127.0.0.1:5000"
    data = {
        "token": "mytoken",
        "request": "set",
        "bucket": "mybucket55",
        "content": r'{"phone": "+49 52629611962", "name": "Max Weber"}'
    }

    response = requests.post(url,json=data)

    print(response)
    print(response.json())

def getData():
    url = "http://127.0.0.1:5000"
    data = {
        "token": "mytoken",
        "request": "get",
        "bucket": "mybucket"
    }

    response = requests.post(url,json=data)

    print(response)
    print(response.json())

def createData():
    url = "http://127.0.0.1:5000"
    data = {
        "token": "mytoken",
        "request": "create",
        "bucket": "mybucket"
    }

    response = requests.post(url,json=data)

    print(response)
    print(response.json())

def deleteData():
    url = "http://127.0.0.1:5000"
    data = {
        "token": "mytoken",
        "request": "delete",
        "bucket": "mybucket"
    }

    response = requests.post(url,json=data)

    print(response)
    print(response.json())

deleteData()