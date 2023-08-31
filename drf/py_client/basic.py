import requests



endpoint = "https://httpbin.org/status/200/"

endpoint = "https://httpbin.org/anything"

endpoint = "http://127.0.0.1:8000/api/"



get_response = requests.get(endpoint,params={"abc":123}, json={"query":"Hello World"})

print("-"*20)

print(get_response.json())

print(get_response.status_code)



class Hello():
    def __init__(self) -> None:
        pass
    
    @property
    def NN(self):
        return 2123
    @property
    def n2(self):
        return 1231312
    
m = Hello()
    
    
    
    
print(m.n2)
