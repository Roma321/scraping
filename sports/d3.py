import requests
from bs4 import BeautifulSoup
import re


def scrab(i):
    link = f"https://www.sports.ru/football/{i}"
    res = requests.get(link)
    if res.status_code == 404:
        return
    soup = BeautifulSoup(res.text, features="html.parser")
    try:
        text_ps = [x.text for x in
                   [y for y in soup.find('div', {'class': 'news-item__content js-mediator-article'}).findAll('p') if
                    y.find('a') is None or
                    y.text != y.find('a').text]
                   ]
    except:
        print('error 1')
        return
    print(i)
    header = soup.find('header', {'class': 'news-item__header'}).find('h1', {'class': 'h1_size_tiny'}).text[:100]
    header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
    text = '\n'.join(text_ps)
    with open(f"C:\\Users\\roman\\Desktop\\sports_corpora\\{header}___{i}.txt", 'w', encoding="utf-8") as f:
        f.write(text)


def c():
    for j in range(1113710000, 1113610000, -1):
        try:
            scrab(j)
        except Exception as e:
            print(f"Unknow error at {j}\n{e}")


c()
