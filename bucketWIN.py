from flask import Flask, request, jsonify
import os
import json
from flask_cors import CORS
from pathlib import Path

# Check if the 'buckets' directory exists; if not, create it
if not os.path.isdir('buckets'):
    os.mkdir('buckets')

# Port number for the Flask server
port = 5000
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
        token = request.get_json()['token']
        method = request.get_json()['request']
        bucket = request.get_json()['bucket']

        # Append '.json' extension to the bucket name
        bucket = bucket + ".json"

        # Check if the request method is valid
        if method not in ["create", "get", "set", "delete", "list"]:
            return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid Method Provided!"}, 400)
    
    except:
        # Handle invalid or missing JSON data
        return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid or no JSON Provided!"}, 400)
    
    # Check if the token is valid
    if token not in tokens:
        return jsonify({"Status": "Error", "Code": "403", "Description": "Invalid Token Provided!"}, 403)
    
    # Handle the 'set' method
    if method == "set":
        try:
            # Extract content data from the JSON request
            data = request.get_json()['content']
            print(data)
        except:
            # If content data is missing or invalid, set it to 'null'
            data = "null"
            return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid or no JSON Provided!"}, 400)
        
        # Get a list of existing buckets
        path = Path('buckets')
        buckets = [file.name for file in path.iterdir() if file.is_file()]

        # Check if the specified bucket exists
        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        # Write content data to the specified bucket
        with open(f'buckets/{bucket}', 'w') as file:
            json.dump(json.loads(data), file, indent=2)
        
        return jsonify({"Status": "Success", "Code": "200", "Description": "Bucket Content was Successfully set!"}, 200)
    
    # Handle the 'get' method
    if method == "get":
        path = Path('buckets')
        buckets = [file.name for file in path.iterdir() if file.is_file()]

        # Check if the specified bucket exists
        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        # Read content data from the specified bucket
        with open(f'buckets/{bucket}', 'r') as file:
            data = json.loads(file.read())
        
        return jsonify(data)
    
    # Handle the 'delete' method
    if method == "delete":
        path = Path('buckets')
        buckets = [file.name for file in path.iterdir() if file.is_file()]

        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        os.remove(f'buckets/{bucket}')

        return jsonify({"Status": "Success", "Code": "200", "Description": f"Bucket: {bucket} was Successfully deleted!"}, 200)
    
    # Handle the 'create' method
    if method == "create":
        path = Path('buckets')
        buckets = [file.name for file in path.iterdir() if file.is_file()]

        if bucket in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} already exists!"}, 404)
        
        with open(f'buckets/{bucket}', 'w') as file:
            json.dump({"placeholder": "placeholder"}, file, indent=2)
        file.close()
        
        return jsonify({"Status": "Success", "Code": "200", "Description": f"Bucket: {bucket} was Successfully created!"}, 200)
    
    # Handle other methods (not implemented)
    return jsonify({"Status": "Error", "Code": "500", "Description": "Unknown"}), 500

# Run the Flask app
app.run(host="0.0.0.0", port=port)