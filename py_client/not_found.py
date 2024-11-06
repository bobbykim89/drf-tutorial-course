import requests

endpoint = 'http://localhost:8000/api/products/1231231231232434523454352/'

get_response = requests.get(endpoint)
print(get_response.json())
