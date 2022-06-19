import requests


with open(r'C:\Users\nikkr\Downloads\dataset_24476_3 (2).txt', 'r') as f, open('Resp.txt', 'a') as w:
    s = f.read().split()

    for num in s:
        req = requests.get(f'http://numbersapi.com/{num}/math?json=true')
        resp = req.json()
        if resp['found'] == True:
            w.write('Interesting\n')
        else:
            w.write('Boring\n')
