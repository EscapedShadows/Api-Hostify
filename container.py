from flask import Flask, request, jsonify
import json
from flask_cors import CORS

# Debug flag for additional console output
debug_mode = False

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

        # Check if the request method is valid
        valid_methods = ["get", "set"]
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
        
        # Write content data to the specified bucket
        with open(f'bucket.json', 'w') as file:
            json.dump(json.loads(data), file, indent=2)
        
        return jsonify({"Status": "Success", "Code": "200", "Description": "Bucket Content was Successfully set!"}, 200)
    
    # Handle the 'get' method
    if method == "get":
        # Read content data from the specified bucket
        with open(f'bucket.json', 'r') as file:
            data = json.load(file)
        
        return jsonify(data)

# Run the Flask app
app.run(host="0.0.0.0", port=port)