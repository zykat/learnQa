import requests

page="https://playground.learnqa.ru/api/check_type"
name={"name": "Olga"}
response = requests.post(page, data=name)

print(response.text)