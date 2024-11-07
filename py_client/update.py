import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    "title": "Updated Hello World",
    "price": 120.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
