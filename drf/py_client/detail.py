import requests



endpoint = "http://127.0.0.1:8000/api/products/12/"


#endpoint = "http://127.0.0.1:8000/api/products/"



get_response = requests.post(endpoint, json={"title":"Hello Mixin"})

print("-"*20)

print(get_response.json())





