from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import csv
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    p=(str1.join(s))  
    return p 
url='https://indianexpress.com/elections/state-wise-winner-list-lok-sabha-elections-2019-5739099/'
r=requests.get(url)
cont=r.content
soup=BeautifulSoup(cont, 'html.parser')
'''
a=soup.find_all('table')
mydatastr=""
for tr in soup.find_all('tr'):
    #print(tr.text)
    mydatastr+=tr.text
    mydatastr=mydatastr[1:]
#print(mydatastr)
itemlist=mydatastr.split("\n\n")
city=['Mirzapur', 'Etah', 'Aligarh']
for item in itemlist:
    
    datalist=item.split('\n')
    #print(datalist[0])
    i=0
    if datalist[0] in city:
        print(datalist)
        print("SEAT:" + datalist[0] +" "+"PARTY:"+ datalist[1]+" "+"LEADER:" +" "+ datalist[2])
       # writer.writerow(datalist)
'''
city=['Mirzapur', 'Rampur','Kanpur','Etawah', 'Aligarh']
fopen=open('2019elections.csv', "w", newline='')
writer = csv.writer(fopen)
writer.writerow(["SEAT", "PARTY WON", "LEADER"])
tab=soup.find_all('tr')
for row in tab:
    cols=row.findChildren(recursive=False)
    cols=[ele.text.strip() for ele in cols]
    #print(cols)
    writer.writerow(cols)
    if cols[0] in city:
        print(cols) 