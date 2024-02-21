import requests

page = "https://playground.learnqa.ru/api/compare_query_type"
method = ['GET', 'POST', 'DELETE', 'PUT']

l = len(method)

for i in range(l):
    if 'GET' in method[i]:
        response = requests.get(page, params='method='+method[i],verify=False)
        print(method[i])
        print(response.text)
    elif 'DELETE' in method[i]:
        response = requests.delete(page, data='method=' + method[i], verify=False)
        print(method[i])
        print(response.text)
    elif 'POST' in method[i]:
        response = requests.post(page, data='method=' + method[i], verify=False)
        print(method[i])
        print(response.text)
    else:
        response = requests.put(page, data='method=' + method[i], verify=False)
        print(method[i])
        print(response.text)