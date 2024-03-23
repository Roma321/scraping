import requests
from bs4 import BeautifulSoup
import re

lst = [
    "https://www.krugosvet.ru/enc/religiya",
    "https://www.krugosvet.ru/enc/sociologiya",
    "https://www.krugosvet.ru/enc/psihologiya-i-pedagogika",
    "https://www.krugosvet.ru/enc/narody-i-yazyki",
    "https://www.krugosvet.ru/enc/gosudarstvo-i-politika",
    "https://www.krugosvet.ru/enc/voennoe-delo",
    "https://www.krugosvet.ru/enc/arheologiya",
    "https://www.krugosvet.ru/enc/istoriya",
    "https://www.krugosvet.ru/enc/lingvistika",
    "https://www.krugosvet.ru/enc/geologiya",
    "https://www.krugosvet.ru/enc/aviaciya-i-kosmonavtika",
    "https://www.krugosvet.ru/enc/astronomiya",
    "https://www.krugosvet.ru/enc/biologiya",
    "https://www.krugosvet.ru/enc/voennaya-tehnika",
    "https://www.krugosvet.ru/enc/matematika",
    "https://www.krugosvet.ru/enc/tehnologiya-i-promyshlennost",
    "https://www.krugosvet.ru/enc/transport-i-svyaz",
    "https://www.krugosvet.ru/enc/fizika",
    "https://www.krugosvet.ru/enc/himiya",
    "https://www.krugosvet.ru/enc/energetika-i-stroitelstvo",
    "https://www.krugosvet.ru/enc/medicina",
    "https://www.krugosvet.ru/enc/sport"]
i = 0
group_index = 0
while True:

    link = f"{lst[group_index]}/page/{i}"
    res_first = requests.get(link,
                             headers={'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                    'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                      'From': 'youremail@domain.example'})
    res_first = BeautifulSoup(res_first.text, features="html.parser")
    links = [x.find('a')['href'] for x in res_first.findAll('div', {'class': "article-teaser"})]
    if len(links) == 0:
        group_index += 1
        i = 0
        continue
    for link in links:
        print(f"https://www.krugosvet.ru{link}")
        res_article = requests.get(f"https://www.krugosvet.ru{link}",
                                   headers={
                                       'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 ('
                                                     'KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                                       'From': 'youremail@domain.example'})
        # print(res_article.text)
        res_article = BeautifulSoup(res_article.text.replace('<!--/noindex-->	', ''), features="html.parser")
        # print(res_article)
        text = "\n".join([x.text for x in res_article.find('div', {'class': 'body'}).findAll('p')])
        header = res_article.find('h1').text
        print(header)
        header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
        with open(f"C:\\Users\\roman\\Desktop\\scraping\\wiki\\krugosvet\\{header}___{len(text)}.txt", 'w',
                  encoding="utf-8") as f:
            f.write(text)
    i += 1
