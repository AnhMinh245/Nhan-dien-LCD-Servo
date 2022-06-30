# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:22:47 2022

@author: pamin
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
soup = BeautifulSoup(response.content, "html.parser")
titles = soup.findAll('h3', class_='title-news')
links = [link.find('a').attrs["href"] for link in titles]

for link in links:

    news = requests.get("https://tuoitre.vn" + link)

    soup = BeautifulSoup(news.content, "html.parser")

    title = soup.find("h1", class_="article-title").text

    abstract = soup.find("h2", class_="sapo").text

    body = soup.find("div", id="main-detail-body")

    content = "{0}{1}".format(body.findChildren("p", recursive=False)[0].text,
                              body.findChildren("p", recursive=False)[1].text)

    image = body.find("img").attrs["src"]

    print('\033[1m' + 'Tiêu đề: ' + '\033[0m' + title)

    print('\033[1m' + 'Mô tả: ' + '\033[0m' + abstract)

    print('\033[1m' + 'Nội dung: ' + '\033[0m' + content)

    print('\033[1m' + 'Ảnh minh họa: ' + '\033[0m' + image)
    print("____________________________________________________________________")
