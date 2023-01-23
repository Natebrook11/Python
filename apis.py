import requests

Base_URL = 'https://fakestoreapi.com'

response = requests.delete(f"{Base_URL}/products/8")
print(response.json())