import requests

# Ex6: Длинный редирект
page = "https://playground.learnqa.ru/api/long_redirect"

response = requests.get(page, allow_redirects=True)
h = response.history

print(len(h))
print(response.url)


