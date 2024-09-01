import requests

API_URL = "http://127.0.0.1:5000/run-matlab"
matlab_code = "a = [1, 2, 3]; b = sum(a);"

response = requests.post(API_URL, json={'code': matlab_code})

print(response.json())
