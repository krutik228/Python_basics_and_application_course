import re
import requests

pattern = r"(<a (.*)?)href=(\'|\")(.*?:\/\/)?(://)?([a-zA-Z\.\-\_0-9]+)"
pattern5 = r"([a-zA-Z\.\-\_0-9]+)"

req = requests.get(input())

content = req.content.decode('utf-8')

match = re.findall(pattern, content)

domains = set()
for link in set(match):
    if re.match(pattern5, link[-1]) and (not link[-1].startswith('.')):
        domains.add(re.match(pattern5, link[-1]).group())

domains = sorted(domains)
[print(i) for i in domains]