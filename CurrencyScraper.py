#Import packages needed
from bs4 import BeautifulSoup
import urllib2
import csv
import datetime
import os

#Base URL
url = 'https://www.google.com/search?q=nzd+to+inr' 

#Mask bot as a browser
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]
openURL = opener.open(url)
#print openURL.read(500)

src = BeautifulSoup(openURL.read(), features = "html5lib")
rate = src.find("span", {"id": "knowledge-currency__tgt-amount"}).get("data-value")

fieldNames = ['row_id','date','time','day','hour','NZD','INR']


# if os.stat('raw_data.csv') == 0:
#     with open ('raw_data.csv', mode = 'w') as raw_data:
#         csv.DictWriter(raw_data, fieldnames = fieldNames).writeheader()

with open ('raw_data.csv', mode = 'a') as raw_data:
    # Fieldnames = ['row_id','date','time','day','hour','NZD','INR']
    writer = csv.DictWriter(raw_data, fieldnames = fieldNames)
    writeHeaderFlag = 0
    while os.stat('raw_data.csv').st_size == 0:
        writer.writeheader()
        writeHeaderFlag = 1
        break

    # Check if the header was written in this iteration, update row index.
    if writeHeaderFlag == 1:
        row_id = 1
        indexFile = open('index.txt', 'w')
        indexFile.write(str(row_id))
        indexFile.close()
    else:
        indexFile = open('index.txt', 'r')
        row_id = int(indexFile.read()) + 1
        indexFile.close()
        indexFile = open('index.txt', 'w')
        indexFile.write(str(row_id))
        indexFile.close()

    record = {'row_id':row_id,
        'date':datetime.date.today(),
        'time': datetime.datetime.now().time(),
        'day':datetime.datetime.now().strftime("%A"), 
        'hour':datetime.datetime.now().strftime("%H"), 
        'NZD':1, 
        'INR':rate}
    writer.writerow({'row_id':record['row_id'],
                'date':record['date'],
                'time':record['time'],
                'day':record['day'],
                'hour':record['hour'],
                'NZD':record['NZD'],
                'INR':record['INR']})
    #write the header
    # writer.writeheader()
    # writer.writerow({'row_id':record['row_id'],
    #                 'date':record['date'],
    #                 'day':record['day'],
    #                 'hour':record['hour'],
    #                 'NZD':record['NZD'],
    #                 'INR':record['INR']})


"""
Notes
https://www.google.com/search?q=nzd+to+inr
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36


To-Do:
Add auto increment (with check for blank file) for row_id in  csv
Write header only if file is empty. Better yet, write to MySQL DB. Simpler.
"""