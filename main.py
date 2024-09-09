import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from PIL import Image

load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")


auth = OAuth1(api_key, api_secret)

topic = input("What icon would you like to search for? ")
amount = int(input("Displayed amount? "))
search = f"https://api.thenounproject.com/v2/icon?query={topic}"
endpoint = "https://api.thenounproject.com/v2/icon/33"


response = requests.get(search, auth=auth)
response_data = json.loads(response.content)


thumbnail_urls = []
for icon in response_data["icons"]:
    thumbnail_urls.append(icon["thumbnail_url"])


for i in range(amount):
    response2 = requests.get(thumbnail_urls[i - 1], stream=True)
    img = Image.open(response2.raw)
    img.show()
