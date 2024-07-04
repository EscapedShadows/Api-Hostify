from library.requestCompact import Bucket

data = {
    "hi": "test"
}

sender = Bucket(token="mytoken", bucketName="mybucket", requestType="set", url="http://192.168.2.128:5001/", content=data).send()

print(sender.text)

"""
This segment is the Code originally needed to create a request to the Endpoint but as i said its supposed to be easy to use so i made a small "library" you can use to simplify it.
"""

#import requests
#import json
#
#headers = {
#    'Content-Type': 'application/json',
#}
#
#data = {
#    "token": "mytoken",
#    "content": {"hi": "test"},
#    "request": "set",
#    "bucket": "mybucket"
#}
#response = requests.post(url="http://192.168.2.128:5001/", data=json.dumps(data), headers=headers)