import os
import requests

# Set the server details
server_url = "https://example.com/upload"
server_username = "your_username"
server_password = "your_password"

# Set the file path
file_path = "/path/to/your/file.txt"

# Read the file
with open(file_path, "rb") as file:
    # Create the request
    response = requests.post(
        server_url,
        files={"file": file},
        auth=(server_username, server_password)
    )

# Check the response status
if response.status_code == 200:
    print("File uploaded successfully!")
else:
    print(f"Error uploading file: {response.status_code} - {response.text}")