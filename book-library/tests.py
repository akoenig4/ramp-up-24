import requests

# Define the base URL of your FastAPI server
base_url = "http://127.0.0.1:8001"

# Data for creating a new book
data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}

# Send a POST request to create a new book
response = requests.post(f"{base_url}/books/", json=data)

# Print the response
print("Response status code:", response.status_code)
print("Response body:", response.json())
