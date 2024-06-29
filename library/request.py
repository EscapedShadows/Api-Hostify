class Bucket():
    def __init__(self, token, bucketName, requestType, content, url):
        self.token = token
        self.bucketName = bucketName
        self.requestType = requestType
        self.content = content
        self.url = url
    
    def send(self):
        import requests
        data = {
            "token": self.token,
            "content": self.content,
            "request": self.requestType,
            "bucket": self.bucketName
        }

        response = requests.post(url=self.url, data=data)

        return response