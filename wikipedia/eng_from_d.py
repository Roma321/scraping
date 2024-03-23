import time

import requests
from bs4 import BeautifulSoup
import re

count = 0

link = "https://en.wikipedia.org/w/index.php?title=Special:AllPages&from=Datcha"
while True:
    res_first = requests.get(link,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                      'From': 'youremail@domain.example'})
    res_first = BeautifulSoup(res_first.text, features="html.parser")
    res3 = res_first.find('ul', {'class': 'mw-allpages-chunk'}).findAll('li')
    res3 = [x.find('a')['href'] for x in res3]
    for r in res3:
        try:
            article_link = f"https://en.wikipedia.org{r}"
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
            with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\eng_d\\{header}___{len(text)}.txt", 'w',
                      encoding="utf-8") as f:
                f.write(text)
        except:
            print('бля')
            time.sleep(10)
    a = res_first.find('div', {'class': 'mw-allpages-nav'}).findAll('a')
    a = [x for x in a if x.text.__contains__('Next ')][0]
    link = f"https://en.wikipedia.org{a['href']}"
    print(link)
