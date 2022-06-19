import requests
import json
import sys



client_id = '6af92048bd2c99101e2a'
client_secret = '8729965be4f403d44682bff6ff53bb43'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком

with open(r'C:\Users\nikkr\Downloads\dataset_24476_4 (1).txt') as f, open('Resp.txt', 'a') as w:
    inputs = f.read().split()
    res = []
    for id in inputs:

        r = requests.get(f"https://api.artsy.net/api/artists/{id}", headers=headers)
        r.encoding = 'utf-8'

        j = json.loads(r.text)
        res.append((j['sortable_name'], j['birthday']))

    res = sorted(res, key=lambda x: (x[1], x[0]))
    [print(name[0])for name in res]
    # [w.write(name[0] + '\n') for name in res]


