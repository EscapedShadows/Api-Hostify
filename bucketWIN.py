from flask import Flask, request, jsonify
import os
import json
from time import sleep
from flask_cors import CORS

port = 5000
tokens = ["your-api-token-here"]

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST','GET'])
def main():
    token = request.get_json()['token']
    try:
        token = request.get_json()['token']
        method = request.get_json()['request']
    except:
        return jsonify({"Status":"Error","Code":"400","Description":"Invalid or no JSON Provided! For Information on how to Format API requests take a look at this page: https://github.com/EscapedShadows/Api-Hostify/blob/main/guide.txt"},400)
    
    return jsonify({"Status":"Success","Code":"200","Description":"None"}),200

app.run(debug=True, host="0.0.0.0", port=port)