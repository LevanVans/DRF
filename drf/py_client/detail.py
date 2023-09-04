import requests



endpoint = "http://127.0.0.1:8000/api/products/1/"


#endpoint = "http://127.0.0.1:8000/api/products/"



get_response = requests.get(endpoint, json={"title":"Hello Man"})

print("-"*20)

print(get_response.json())





