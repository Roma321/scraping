import requests
from bs4 import BeautifulSoup
import re

my_id = 594
for i in range(13, 10000):  # дошёл до страницы 1979, число: 9 марта 2023
    try:
        page_link = f"https://www.woman.ru/forum/{i}/?sort=new"
        res_page = requests.get(page_link)
        soup = BeautifulSoup(res_page.text, features="html.parser")
        links = [x['href'] for x in soup.findAll('a', {'class': 'list-item__link'})]
        for link in links:
            try:
                com_id = 1
                req_link = f"https://www.woman.ru/{link}"
                res = requests.get(req_link)
                soup = BeautifulSoup(res.text, features="html.parser")
                topic_start = soup.find('div', {'class': 'card card_topic-start'})
                header = topic_start.find('h1', {'class': 'card__topic-title'}).text
                header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)
                longer_header = topic_start.find('p', {'class': 'card__comment'}).text
                with open(f"C:\\Users\\roman\\Desktop\\woman_ru_corpora\\asks\\{my_id}___{header}.txt", 'w',
                          encoding="utf-8") as f:
                    f.write(longer_header)

                comments = soup.findAll('div', {'class': 'card card_answer'})
                comments = [x.find('p', {'class': 'card__comment'}).text for x in comments]
                my_id += 1
                for comment in comments:
                    with open(f"C:\\Users\\roman\\Desktop\\woman_ru_corpora\\comments\\{my_id}___{com_id}.txt", 'w',
                              encoding="utf-8") as f:
                        f.write(comment)
                    com_id += 1
                print(my_id, com_id, i)
            except:
                print('b')
    except:
        print('a')
