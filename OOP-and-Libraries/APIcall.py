import requests
import json

api_url = "http://api.open-notify.org/astros.json"

response = requests.get(api_url)
print(response)

json_data = response.json()

print(json_data)

for this_Person in json_data["people"]:
    print(this_Person["name"] , this_Person["craft"])