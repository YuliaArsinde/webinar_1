import requests
import json

response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
data = json.loads(response.text)
print(json.dumps(data, indent=4, sort_keys=True))
