"""
THE FOLLOWING CODE IS NOT NEEDED AS IT IS JUST A TESTING SCRIPT DURING DEVELOPEMENT
"""
import requests
import json

def send_request(request_type, bucket_name, content=None):
    url = "http://127.0.0.1:5000"
    data = {
        "token": "mytoken",
        "request": request_type,
        "bucket": bucket_name
    }
    if content:
        data["content"] = content

    response = requests.post(url, json=data)
    return response.json()

def main():
    bucket_name = "mybucket"

    while True:
        action = input("Enter the action (set/get/create/delete) or 'exit' to quit: ").lower()

        if action == "exit":
            break

        if action in ["set", "create"]:
            content_data = input("Enter JSON content data (press Enter to skip): ").strip()
            if content_data:
                try:
                    content_data = json.loads(content_data)
                except json.JSONDecodeError:
                    print("Invalid JSON format. Please try again.")
                    continue

        if action == "set":
            set_response = send_request("set", bucket_name, content=content_data)
            print("Set Response:", set_response)
        elif action == "get":
            get_response = send_request("get", bucket_name)
            print("Get Response:", get_response)
        elif action == "create":
            create_response = send_request("create", bucket_name)
            print("Create Response:", create_response)
        elif action == "delete":
            delete_response = send_request("delete", bucket_name)
            print("Delete Response:", delete_response)
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
