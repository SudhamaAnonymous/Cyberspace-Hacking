import requests
import urllib
import json

url = "www.google.com" # for example
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://www.ipqualityscore.com/api/json/url/P8lOwwVZknP7Yt6QBRyf8YVeaxoqUlaG/URL_HERE"
data = requests.get(api_url + encoded_url)
print(json.dumps(data.json(), indent=4))