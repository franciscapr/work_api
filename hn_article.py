import requests
import json

# Hace una llamada a la API y guarda la respuesta.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)

print(f"Status code: {r.status_code}")

# Explora la estructura de los datos.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)