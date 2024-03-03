import requests
import json
import time

page = 'https://playground.learnqa.ru/ajax/api/longtime_job'

response = requests.get(page)
obj = json.loads(response.text)
key = 'token'
key2 = 'seconds'

time.sleep(obj[key2])
response2 = requests.get(page, params='token='+obj[key])

print(response2.text)

