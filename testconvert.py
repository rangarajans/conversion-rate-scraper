#Import packages needed
from bs4 import BeautifulSoup
import urllib2
import csv
import datetime
import os

# This will extract the conversion rates of the top 20 currencies in the world against NZD.

# Top 20 traded currencies:
tgtCurrencies = ['USD','EUR','JPY','GBP','AUD','CAD','CHF','CNY','SEK','NZD','MXN','SGD','HKD','NOK','KRW','TRY','RUB','INR','BRL','ZAR']

# Base fields for csv:
fieldNames = ['row_id','date','time','day','hour']
rates = []

for tgt in tgtCurrencies:
    url = 'https://www.google.com/search?q=nzd+to+' + tgt

    #Mask bot as a browser so Google doesn't block it.
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')]

    # Test read - read the first 500 characters of HTML.
    # print openURL.read(500)
    # print opener.open(url).getcode()

    openURL = opener.open(url)
    
    # Scrape target value into variable 'rate'
    src = BeautifulSoup(openURL.read(), features = "html5lib")
    rate = src.find("span", {"id": "knowledge-currency__tgt-amount"}).get("data-value")
    if rate is not None:
        rates.append(rate)
    else:
        rates.append(0)

print rates