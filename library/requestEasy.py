class BucketCreate():
    def __init__(self, token, bucketName, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = "create"
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        import json

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "token": self.token,
            "content": json.dumps(self.content),
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)

        return response
    
class BucketGet():
    def __init__(self, token, bucketName, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = "get"
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        import json

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "token": self.token,
            "content": json.dumps(self.content),
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)

        return response
    
class BucketSet():
    def __init__(self, token, bucketName, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = "set"
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        import json

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "token": self.token,
            "content": json.dumps(self.content),
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)

        return response
    
class BucketDelete():
    def __init__(self, token, bucketName, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = "delete"
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        import json

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "token": self.token,
            "content": json.dumps(self.content),
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)

        return response
    
class BucketList():
    def __init__(self, token, bucketName, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = "list"
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        import json

        headers = {
            'Content-Type': 'application/json',
        }

        data = {
            "token": self.token,
            "content": json.dumps(self.content),
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=json.dumps(data), headers=headers)

        return response