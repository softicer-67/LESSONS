import requests
import json


url = 'https://api.github.com'
user = 'softicer-67'


r = requests.get(f'{url}/users/{user}/repos').json()


for i in range(len(r)):
    x = f'Project Number: {i + 1}\nProject Name: {r[i]["name"]}\nProject URL: {r[i]["svn_url"]}'
    print(x)

with open('data.json', 'w') as f:
    json.dump(r, f)
