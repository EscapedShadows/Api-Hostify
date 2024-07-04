from flask import Flask, request, jsonify
import os
import json
from flask_cors import CORS
from pathlib import Path

# Debug flag for additional console output
debug_mode = False

# Check if the 'buckets' directory exists; if not, create it
if not os.path.exists('buckets'):
    os.mkdir('buckets')

# Port number for the Flask server
port = 5001
# Tokens allowed for authentication
tokens = ["mytoken"]

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Main route for handling POST requests
@app.route('/', methods=['POST'])
def main():
    # Ensure only POST requests are allowed
    if request.method != "POST":
        return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid Method Provided!"}, 400)

    try:
        # Extract token, request method, and bucket name from JSON request
        req_data = request.get_json()
        token = req_data.get('token')
        method = req_data.get('request')
        bucket = req_data.get('bucket')
        sub_bucket = req_data.get('sub_bucket')

        # Append '.json' extension to the bucket name
        sub_bucket += ".json"

        # Check if the request method is valid
        valid_methods = ["createTop", "createSub", "getTop", "getSub", "set", "deleteTop", "deleteSub", "list"]
        if method not in valid_methods:
            return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid Method Provided!"}, 400)
    
    except Exception as e:
        if debug_mode:
            print(f"Exception: {e}")
        # Handle invalid or missing JSON data
        return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid or no JSON Provided!"}, 400)
    
    # Check if the token is valid
    if token not in tokens:
        return jsonify({"Status": "Error", "Code": "403", "Description": "Invalid Token Provided!"}, 403)
    
    path = Path('buckets')
    buckets = [file.name for file in path.iterdir() if file.is_file()]



# Run the Flask app
app.run(host="0.0.0.0", port=port)