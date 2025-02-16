import requests

# Ex7: Запросы и методы
page = "https://playground.learnqa.ru/api/compare_query_type"
method = ['GET', 'POST', 'DELETE', 'PUT']
# #1
# response = requests.get(page)
# print(response.text)
# #2
# response = requests.head(page)
# print(response.text)
# #3
# response = requests.put(page, data='method=PUT')
# print(response.text)
# # 4
l = len(method)

for i in range(l):
    if 'GET' in method[i]:
        response = requests.get(page, params='method='+method[i],verify=False)
        print(method[i])
        print(response.text)
    elif 'DELETE' in method[i]:
        response = requests.delete(page, data='method=' + method[i],verify=False)
        print(method[i])
        print(response.text)
    elif 'POST' in method[i]:
        response = requests.post(page, data='method=' + method[i],verify=False)
        print(method[i])
        print(response.text)
    else:
        response = requests.put(page, data='method=' + method[i],verify=False)
        print(method[i])
        print(response.text)