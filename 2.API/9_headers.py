import requests

headers = {"some_header": "123"}
page="https://playground.learnqa.ru/api/show_all_headers"
response = requests.get(page, headers = headers)
print(response.text)
print(response.headers)