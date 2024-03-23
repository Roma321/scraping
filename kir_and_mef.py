import requests
from bs4 import BeautifulSoup
import re

i = 12184

while True:
    print(i)
    link = f"https://megabook.ru/encyclopedia/alphabet?page={i}"
    res_first = requests.get(link,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                      'From': 'youremail@t.example'})
    res_first = BeautifulSoup(res_first.text, features="html.parser")
    links = [x['href'] for x in res_first.findAll('a', {'class': "heading"})]
    if len(links) == 0:
        break
    for article_link in links:
        print(f"https://megabook.ru{article_link}")
        res_article = requests.get(f"https://megabook.ru{article_link}",
                                   headers={
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ('
                                                     'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                       'From': 'u@u.example'})
        # print(res_article.text)
        res_article = BeautifulSoup(res_article.text.replace('<!--/noindex-->	', ''), features="html.parser")
        text = res_article.find('div', {'class': 'ArticleContent'}).text
        header = res_article.find('h1').text
        print(header)
        header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
        with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\kirill\\{header}___{len(text)}.txt", 'w',
                  encoding="utf-8") as f:
            f.write(text)
    i += 1
