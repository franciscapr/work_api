import requests

# Realiza una llamada a la API y verifica la respuesta.

url = "http://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


# Convierte el objeto de respuesta en una diccionario.
response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explora la informaciòn sobre los repositorios.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")


# Examina el primer repositorio.
repo_dict = repo_dicts[0]

print("\nSekected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

print(f"\nKeys: {len(repo_dict)}")

#for key in sorted(repo_dict.keys()):
#    print(key)