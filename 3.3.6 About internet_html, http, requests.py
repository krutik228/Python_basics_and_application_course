import requests
import re


def main():

    url_A, url_B = input(), input()

    pattern = r"href=\"(\S*)\""

    url = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'

    req = requests.get(url_A)

    links = re.findall(pattern, req.text)
    for link in links:
        req_2 = requests.get(link)
        if re.search(link, req_2.text):
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    print(main())
