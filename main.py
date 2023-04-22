import requests

response = requests.get('https://dnd5eapi.co/api/classes')
print(response.status_code)  # prints the status code of the response
print(response.json())  # prints the JSON content of the response
