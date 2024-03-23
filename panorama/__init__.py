from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup
import re

start_date = date(2021, 3, 19)
end_date = date(2017, 1, 1)
delta = timedelta(days=-1)
while start_date >= end_date:
    str_date = start_date.strftime("%d-%m-%Y")
    link = f"https://panorama.pub/news/{str_date}"
    print(str_date, link)
    start_date += delta
    res = requests.get(link)
    if res.status_code == 404:
        continue
    soup = BeautifulSoup(res.text, features="html.parser")
    links = soup.findAll('a', {'class': 'flex flex-col rounded-md hover:text-secondary hover:bg-accent/[.1] mb-2'})
    links = [x['href'] for x in links]

    for article_link in links:
        link = f"https://panorama.pub{article_link}"
        res = requests.get(link)
        if res.status_code == 404:
            continue
        soup = BeautifulSoup(res.text, features="html.parser")
        header = soup.find('h1', {'class': 'font-bold text-2xl md:text-3xl lg:text-4xl pl-1 pr-2 self-center'}).text
        text = soup.find('div', {'class': 'entry-contents pr-0 md:pr-8'}).text
        file_header = re.sub(r"[?/\\!:'\"<>*\n\r\t|]", "", header)[:200]
        with open(f"C:\\Users\\roman\\Desktop\\scraping\\panorama\\{file_header} — {str_date}.txt", 'w',
                  encoding="utf-8") as f:
            f.write(f"{header}\n{text}")
