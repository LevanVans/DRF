import requests



endpoint = "http://127.0.0.1:8000/api/products/update/1/"




get_response = requests.put(endpoint, json={"title":"Hello my Maaan "})

print("-"*20)







