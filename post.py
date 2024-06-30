from library.request import Bucket

data = {
    "hi": "test"
}

sender = Bucket(token="mytoken", bucketName="mybucket", requestType="set", url="http://192.168.2.128:5001/", content=data).send()

print(sender.text)