import time

import requests
from bs4 import BeautifulSoup
import re

count = 0

link = "https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%92%D1%81%D0%B5_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B&from=https://ru.wikipedia.org/wiki/%D0%A7%D0%BC%D1%8B%D1%85%D0%BE%D0%B2%D0%B0,_%D0%98%D1%80%D0%B8%D0%BD%D0%B0_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D0%BD%D0%B0"
while True:
    res_first = requests.get(link,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                      'From': 'youremail@domain.example'})
    res_first = BeautifulSoup(res_first.text, features="html.parser")
    try:
        res3 = res_first.find('ul', {'class': 'mw-allpages-chunk'}).findAll('li')
        res3 = [x.find('a')['href'] for x in res3]
    except:
        continue
    for r in res3:
        try:
            article_link = f"https://ru.wikipedia.org{r}"
            print(article_link)
            try:
                res2 = requests.get(article_link).text
            except:
                time.sleep(60)
                continue
            res2 = BeautifulSoup(res2, features="html.parser")
            res = res2.find('div', {'class': 'mw-body-content mw-content-ltr'}).findAll(['p', 'ul'])
            res = [x.text for x in res if x.find('span', {'class': 'toctext'}) is None]
            text = "\n".join(res)
            header = res2.find('h1', {'class': 'firstHeading mw-first-heading'}).text
            header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
            with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\result\\{header}___{len(text)}.txt", 'w',
                      encoding="utf-8") as f:
                f.write(text)
        except:
            print('бля')
    a = res_first.find('div', {'class': 'mw-allpages-nav'}).findAll('a')
    a = [x for x in a if x.text.__contains__('Следующая ')][0]
    link = f"https://ru.wikipedia.org{a['href']}"
    print(link)
