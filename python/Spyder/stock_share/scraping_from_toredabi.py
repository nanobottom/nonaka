# -*- coding: utf-8 -*-

import requests, re, datetime, os
from bs4 import BeautifulSoup
from stock_share import StockShare
from getpass import getpass

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
        
    def enter_password(self):
        self.login_info["password"] = getpass('Enter password>>')
    
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
            name_and_code = stock_data.find(href = re.compile("/td/quotes/")).string
            holdings_info["code"], holdings_info["name"] = name_and_code.split(" ", 1)
            values = stock_data.find_all(attrs = {"class": "tblFont"})
            for i, value in enumerate(values):
                holdings_info[values_label[i]] = value.string
            self.holdings_info.append(holdings_info)
            
    def plt(self):
        today = datetime.date.today()
        script_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        success_dir = os.path.join(script_dir, "toredabi", "success")
        failure_dir = os.path.join(script_dir, "toredabi", "failure")
        for holding_info in self.holdings_info:
            stock_share = StockShare(holding_info["code"], today.strftime("%Y-%m-%d"))
            stock_share.get_stock_data()
            print(holding_info["name"])
            # 画像を保存するディレクトリに移動する

            if float(holding_info["profit_or_loss_ratio"]) > 5:
                os.chdir(success_dir)
                stock_share.plt(is_savefig = True)
            elif float(holding_info["profit_or_loss_ratio"]) < -3:
                os.chdir(failure_dir)
                stock_share.plt(is_savefig = True)
            else:
                stock_share.plt()               
            print("取得単価からの騰落率：" + holding_info["profit_or_loss_ratio"] + "%")
            print("※+10%または-2%で売り\n")

if __name__ == "__main__":
    
    scraping_toredabi = ScrapingFromToredabi()
    scraping_toredabi.enter_password()
    scraping_toredabi.login()
    scraping_toredabi.get_holdings_info()
    scraping_toredabi.plt()