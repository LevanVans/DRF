import requests



endpoint = "http://127.0.0.1:8000/api/products/1"


endpoint = "http://127.0.0.1:8000/api/products/create/"



get_response = requests.post(endpoint, json={"title":"Hello Man","content":"Good"})

print("-"*20)

print(get_response.json())





