# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.nikkei.com/nkd/company/?scode=9707")
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
current_price_tag = soup.find(attrs = {"class": "m-stockPriceElm_value now"})
print(current_price_tag)
for i, current_price in enumerate(current_price_tag):
    if i == 0:
        print(current_price.string)
