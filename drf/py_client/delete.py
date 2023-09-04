import requests


product_id = input("Give me pk of Item ")




endpoint = f"http://127.0.0.1:8000/api/products/{int(product_id)}/delete/"






get_response = requests.delete(endpoint)

print("-"*20)

print(get_response.status_code)






