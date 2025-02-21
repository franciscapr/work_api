import requests

# Realiza una llamada a la API y verifica la respuesta.

url = "http://api.github.com/search/repositories"
url += "?q=language:python+sort:stars-stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# Convierte el objeto de respuesta en una diccionario.
response_dict = r.json()

# Procesa los resulados.
print(response_dict.keys())