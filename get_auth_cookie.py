import requests

page = "https://playground.learnqa.ru/api/get_auth_cookie"
page2 = "https://playground.learnqa.ru/api/check_auth_cookie"
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post(page, data=payload)

cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post(page2, cookies=cookies)

print(response2.text)
