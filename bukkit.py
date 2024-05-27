from flask import Flask, request, jsonify
import os
import json
from time import sleep
from flask_cors import CORS

port = 5000
tokens = ["your-api-token-here"]

app = Flask(__name__)

CORS(app)

app.run(debug=True, host="0.0.0.0", port=port)