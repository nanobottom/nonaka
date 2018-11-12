# -*- coding: utf-8 -*-
import requests, datetime
from bs4 import BeautifulSoup
from stock_share import StockShare

class ScrapingFromKabuCom:
    
    def __init__(self):
        self.login_info = {
            "SsLogonUser":"01159503",
            "CookieOn":"1",
            "SsLogonHost":"100",
            "SsLoginPage":"/Members/Personal/KBSSettei/KBSRule.asp",
            }
        self.login_url = "https://s10.kabu.co.jp/_mem_bin/Members/verifpwd.asp"
        self.session = requests.session()
        self.holdings_url = "https://s20.si1.kabu.co.jp/ap/PC/Stocks/Stock/Position/List?actType=TOKUTEI"
        self.holdings_info = []
        
    def input_password(self):
        print("Input password>>", end = "")
        self.login_info["SsLogonPassword"] = input()
        
    def login(self):
        self.session.post(self.login_url, data = self.login_info)
        
    def get_holdings_info(self):
        res = self.session.get(self.holdings_url)
        # エラーならここで例外が発生する
        res.raise_for_status()
        # 資産管理>現物株式>残高照会ページをパースする
        soup = BeautifulSoup(res.content, "html.parser")
        holdings = soup.find_all(attrs = {"class": " open"})
        for holding in holdings:
            holding_info = {}
            # 銘柄名、コードを取得する
            elems = holding.find(attrs = {"align": "left", "class":"m b2", "valign":"middle"})
            for i, elem in enumerate(elems.childGenerator()):
                # 銘柄名
                if i == 1:
                    holding_info["name"] = elem.string.strip()
                # コード
                elif i == 2:
                    holding_info["code"] = elem.string.strip()[1:-1]
            # その他の情報を取得する
            elems = holding.find_all(attrs = {"align": "right", "class":"m b2", "nowrap":""})
            for i, elem in enumerate(elems):
                # 保有株数
                if i == 0:
                    for j, elem2 in enumerate(elem.childGenerator()):
                        if j == 0:
                            holding_info["quantity"] = elem2.string.strip()[:-1]
                # 現在値、平均取得単価
                elif i == 1:
                    for j, elem2 in enumerate(elem.childGenerator()):
                        if j == 0:
                            holding_info["present_value"] = elem2.string.strip()[:-1]
                        elif j == 2:
                            holding_info["average_acquisition_price"] = elem2.string.strip()[:-1]
                # 時価評価額、取得金額
                elif i == 2:
                    for j, elem2 in enumerate(elem.childGenerator()):
                        if j == 0:
                            holding_info["market_value"] = elem2.string.strip()[:-1]
                        elif j == 2:
                            holding_info["acquisition_price"] = elem2.string.strip()[:-1]
                # 評価損益、評価損益率
                elif i == 3:
                    for j, elem2 in enumerate(elem.childGenerator()):
                        if j == 1:
                            holding_info["profit_or_loss"] = elem2.string.strip()
                        if j == 5:
                            holding_info["profit_or_loss_ratio"] = elem2.string.strip()
            self.holdings_info.append(holding_info)

    def plt(self):
        today = datetime.date.today()
        for holding_info in self.holdings_info:
            stock_share = StockShare(holding_info["code"], today.strftime("%Y-%m-%d"))
            print(holding_info["name"])
            stock_share.plt()
            print("取得単価からの騰落率：" + holding_info["profit_or_loss_ratio"] + "%")
            print("※+10%または-3%で売り\n")
                
        
if __name__ == "__main__":
    scraping_kabu_com = ScrapingFromKabuCom()
    scraping_kabu_com.input_password()
    scraping_kabu_com.login()
    scraping_kabu_com.get_holdings_info()
    scraping_kabu_com.plt()