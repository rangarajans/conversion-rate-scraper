#Import packages needed
from bs4 import BeautifulSoup
import urllib2
import csv
import datetime



url = 'https://www.google.com/search?q=nzd+to+inr' 
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
openURL = opener.open(url)
#print openURL.read(500)

src = BeautifulSoup(openURL.read(), features = "html5lib")
rate = src.find("span", {"id": "knowledge-currency__tgt-amount"}).get("data-value")
"""
date =  datetime.date.today()
day = datetime.datetime.now().strftime("%A")
hour = datetime.datetime.now().strftime("%H")
NZD = 1
"""
record = {'row_id':1,
        'date':datetime.date.today(), 
        'day':datetime.datetime.now().strftime("%A"), 
        'hour':datetime.datetime.now().strftime("%H"), 
        'NZD':1, 
        'INR':rate}
with open ('raw_data.csv', mode = 'a') as raw_data:
    Fieldnames = ['row_id','date','day','hour','NZD','INR']
    writer = csv.DictWriter(raw_data, fieldnames = Fieldnames)
    #write the header
    writer.writeheader()
    writer.writerow({'row_id':record['row_id'],
                    'date':record['date'],
                    'day':record['day'],
                    'hour':record['hour'],
                    'NZD':record['NZD'],
                    'INR':record['INR']})

"""
while urllib2.urlopen(url).getcode() == 200:
    src = BeautifulSoup(html)
    print src

    title = src.find("div", {"id": "ctitle"}).text
    div = src.find("div", {"id": "comic"})
    img = 'http:'+div.find("img")["src"]
    print img
    loc = 'F:\\Python\\xkcd\\' + title + ".png"
    #~ urllib.urlretrieve(img, loc)
    print src.find("a", {"rel": "next"}).get('href')
 """



"""
Notes
https://www.google.com/search?q=nzd+to+inr
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36


To-Do:
Add auto increment (with check for blank file) for row_id in  csv
Write header only if file is empty. Better yet, write to MySQL DB. Simpler.
"""