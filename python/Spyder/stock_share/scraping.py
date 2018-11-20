# -*- coding: utf-8 -*-
"""
@author :ryo
"""
__author__  = 'ryo'
__version__ = '1.0'
__date__    = '2018/11/20'

import requests
import re
from bs4 import BeautifulSoup

def scraping_code_from_yahoo_finance(URL):
    codes, names = [], []
    _response = requests.get(URL)
    _soup = BeautifulSoup(_response.content, 'html.parser')
    for _code_tag in _soup.find_all(href=re.compile("https://stocks.finance.yahoo.co.jp/stocks/detail/")):
        codes.append(_code_tag.string)
    
    for _name_tag in _soup.find_all(class_="normal yjSt"):
        names.append(_name_tag.string)
    return codes, names

if __name__ == "__main__":

    URL1 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=1&tm=d&vl=a" 
    URL2 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=2" 
    codes, names = scraping_code_from_yahoo_finance(URL1)
    codes2, names2 = scraping_code_from_yahoo_finance(URL2)
    codes.extend(codes2)

        
