import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/products/1/'

# API (Application programming interface) -> Method
get_response = requests.get(endpoint)  # HTTP Request
print(get_response.json())  # print raw response
# print(get_response.status_code)

# REST APIs -> Web API
# REST API HTTP Request -> JSON (Javascript Object Notation ~ Python Dict)
