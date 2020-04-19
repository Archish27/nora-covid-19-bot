import requests
import json
from nested_lookup import nested_lookup

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    "x-rapidapi-host": "corona-virus-world-and-india-data.p.rapidapi.com",
    "x-rapidapi-key": "038714b9f7msh7caaf92662b8e65p1905c6jsn9fb3ac6f6534",
}

response = requests.request("GET", url, headers=headers)
res = json.loads(response.text)

print(nested_lookup("Mumbai", res)[0]['confirmed'])