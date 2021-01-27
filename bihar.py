import requests
from bs4 import BeautifulSoup
import csv
url='https://www.indiatoday.in/elections/bihar-assembly-polls-2020/story/bihar-election-result-full-list-of-winners-1739762-2020-11-10'
r=requests.get(url)
cont=r.content
soup=BeautifulSoup(cont, 'html.parser')
fopen=open('bihar.csv', "w", newline='')
writer=csv.writer(fopen)
tab=soup.find_all('tr')
for row in soup.find_all('tr'):
    cols=row.findChildren(recursive=False)
    cols=[ele.text.strip() for ele in cols]
    cols=cols[1:]
    print(cols)
    writer.writerow(cols)