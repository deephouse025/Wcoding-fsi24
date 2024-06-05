import requests

r = requests.get("https://dov.ceo/api/breeds/list")
all_breeds = r.json()
print(all_breeds)