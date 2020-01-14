import requests
import json
url = 'https://api.nasa.gov/planetary/apod?api_key='
token = 'BG3DOlJSB1qNQhT9r5kfFe0cSZiUb3WyLM3WDvEK'
headers = {
    'Content-Type': 'application/json',
    'API_KEY': token,
    'Account Email': 'droser@mail.ru',
    'Account ID': '47387baa-1a01-48bb-9688-37c632859908'
}
response=requests.get(f'{url}{token}', headers = headers)
final=response.json()

with open('nasa.json', 'w') as f:
        json.dump(final, f)
