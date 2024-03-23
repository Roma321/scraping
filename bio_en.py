import requests
from bs4 import BeautifulSoup
import re

link = "https://rus-biological.slovaronline.com/2-Абиогенные%20субстраты"
while True:
    res_first = requests.get(link,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                      'From': 'youremail@domain.example'})
    res_first = BeautifulSoup(res_first.text, features="html.parser")
    text = res_first.find('div', {'itemprop': 'content'}).text
    header = res_first.find('div', {'itemprop': 'title'}).text
    header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
    with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\bio_en\\{header}___{len(text)}.txt", 'w',
              encoding="utf-8") as f:
        f.write(text)
    a = res_first.find('p', {'class': 'prev-next-articles'}).find('a', {'class': 'float-right valign-wrapper'})['href']
    link = a
