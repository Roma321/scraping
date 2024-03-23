import time

import requests
from bs4 import BeautifulSoup
import re

page_all = "https://slovaronline.com/tags/Энциклопедии"
r = requests.get(page_all,
                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                        'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                          'From': 'youremail@domain.example'})
r = BeautifulSoup(r.text, features="html.parser")
encs = [f"https:{x['href']}/" for x in
        r.find('table', {'class': "table table-hover"}).findAll('a', {'target': '_blank'})[13:]]

lst = encs
group_index = 2
while True:
    print(lst[group_index])

    r = requests.get(lst[group_index],
                     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                            'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                              'From': 'youremail@domain.example'})

    r = BeautifulSoup(r.text, features="html.parser")
    r = r.find('div', {'class': 'col-lg-4 col-md-6 col-sm-12 article-link'}).findAll('a')
    r = [r[0]['href'], r[len(r) // 2]['href']]
    link1 = f"{lst[group_index]}{r[0]}"
    link2 = f"{lst[group_index]}{r[1]}"
    print(link1)

    while True:
        was = False
        try:
            res_first = requests.get(link1,
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                       'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                         'From': 'youremail@domain.example'})
            res_first = BeautifulSoup(res_first.text, features="html.parser")
            text = res_first.find('div', {'itemprop': 'content'}).text
            header = res_first.find('div', {'itemprop': 'title'}).text
            header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
            with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\q\\{header}___{len(text)}.txt", 'w',
                      encoding="utf-8") as f:
                f.write(text)
            a = res_first.find('p', {'class': 'prev-next-articles'}).find('a', {'class': 'float-right valign-wrapper'})[
                'href']
            link1 = a

            res_first = requests.get(link2,
                                     headers={
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                       'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                         'From': 'youremail@domain.example'})
            res_first = BeautifulSoup(res_first.text, features="html.parser")
            text = res_first.find('div', {'itemprop': 'content'}).text
            header = res_first.find('div', {'itemprop': 'title'}).text
            header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
            with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\q\\{header}___{len(text)}.txt", 'w',
                      encoding="utf-8") as f:
                f.write(text)
            a = res_first.find('p', {'class': 'prev-next-articles'}).find('a', {'class': 'float-right valign-wrapper'})[
                'href']
            link2 = a
        except:
            if was:
                group_index += 1
                break
            else:
                was = True
