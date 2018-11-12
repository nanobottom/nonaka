# -*- coding: utf-8 -*-

import requests, re, datetime
from bs4 import BeautifulSoup
from stock_share import StockShare

class ScrapingFromToredabi:
    
    def __init__(self):
        self.login_url = "https://www.k-zone.co.jp/td/users/login"
        self.login_info = {
                "login":"nanobottom@icloud.com",
                "remember_me":"true",      
                           }
        # 保有銘柄が記載されているページ
        self.holdings_url = "https://www.k-zone.co.jp/td/dashboards/position_hold"
        self.holdings_info = []
        self.session = requests.session()
        
    def input_password(self):
        print("Input password>>", end = "")
        self.login_info["password"] = input()
    
    def login(self):
        self.session.post(self.login_url, data = self.login_info)
        
    def get_holdings_info(self):      
        res = self.session.get(self.holdings_url)
        # エラーならここで例外が発生する
        res.raise_for_status()
        soup = BeautifulSoup(res.content, "html.parser")
        stock_datas = soup.find_all(attrs = {"class":"stockData"})
        values_label = ["quantity", "acquisition_price", "present_value",\
                        "profit_or_loss", "order", "change", "profit_or_loss_ratio"]        
        for stock_data in stock_datas:
            holdings_info = {}
            holdings_info["code"], holdings_info["name"] = \
                stock_data.find(href = re.compile("/td/quotes/")).string.split(" ")
            values = stock_data.find_all(attrs = {"class": "tblFont"})
            for i, value in enumerate(values):
                holdings_info[values_label[i]] = value.string
            self.holdings_info.append(holdings_info)
    
    def plt(self):
        today = datetime.date.today()
        for holding_info in self.holdings_info:
            stock_share = StockShare(holding_info["code"], today.strftime("%Y-%m-%d"))
            print(holding_info["name"])
            stock_share.plt()
            print("取得単価からの騰落率：" + holding_info["profit_or_loss_ratio"] + "%")
            print("※+10%または-3%で売り\n")

if __name__ == "__main__":
    scraping_toredabi = ScrapingFromToredabi()
    scraping_toredabi.input_password()
    scraping_toredabi.login()
    scraping_toredabi.get_holdings_info()
    scraping_toredabi.plt()