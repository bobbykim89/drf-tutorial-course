import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'

# API (Application programming interface) -> Method
get_response = requests.get(endpoint, params={'abc': 123}, json={
                            'query': 'Hello World'})  # HTTP Request
print(get_response.json())  # print raw response
# print(get_response.status_code)

# REST APIs -> Web API
# REST API HTTP Request -> JSON (Javascript Object Notation ~ Python Dict)
