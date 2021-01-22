from bs4 import BeautifulSoup
import requests
import time
from plyer import notification
url="https://news.google.com/news/rss"
r=requests.get(url)
cont=r.content
soup=BeautifulSoup(cont, "xml")
news_list=soup.find_all("item")
for news in news_list:
        print(news.title.text)
        #print(news.link.text)
        print(news.pubDate.text)
        print('-'*70)

