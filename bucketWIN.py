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

        # Append '.json' extension to the bucket name
        bucket += ".json"

        # Check if the request method is valid
        valid_methods = ["create", "get", "set", "delete", "list"]
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

    # Handle the 'set' method
    if method == "set":
        try:
            # Extract content data from the JSON request
            data = req_data.get('content')
            if debug_mode:
                print("Data received:", data)
        except Exception as e:
            if debug_mode:
                print(f"Exception: {e}")
            # If content data is missing or invalid, set it to 'null'
            data = "null"
            return jsonify({"Status": "Error", "Code": "400", "Description": "Invalid or no JSON Provided!"}, 400)
        
        # Check if the specified bucket exists
        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        # Write content data to the specified bucket
        with open(f'buckets/{bucket}', 'w') as file:
            json.dump(json.loads(data), file, indent=2)
        
        return jsonify({"Status": "Success", "Code": "200", "Description": "Bucket Content was Successfully set!"}, 200)
    
    # Handle the 'get' method
    if method == "get":
        # Check if the specified bucket exists
        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        # Read content data from the specified bucket
        with open(f'buckets/{bucket}', 'r') as file:
            data = json.load(file)
        
        return jsonify(data)
    
    # Handle the 'delete' method
    if method == "delete":
        if bucket not in buckets:
            return jsonify({"Status": "Error", "Code": "404", "Description": f"Bucket: {bucket} does not exist!"}, 404)
        
        os.remove(f'buckets/{bucket}')

        return jsonify({"Status": "Success", "Code": "200", "Description": f"Bucket: {bucket} was Successfully deleted!"}, 200)
    
    # Handle the 'create' method
    if method == "create":
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