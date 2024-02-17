import requests
from json.decoder import JSONDecodeError

page="https://playground.learnqa.ru/api/hello"
name={"name": "Olga"}
response = requests.get(page, params=name)

print(response.text)

# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not JSON format")