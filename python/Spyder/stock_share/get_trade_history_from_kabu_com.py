# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 02:02:58 2018

@author: 亮
"""

import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from getpass import getpass
from time import sleep

from wareki import Gengo, Wareki

class GetTradeHistoryFromKabuCom:
    
    def __init__(self):
        self._login_url = "https://s10.kabu.co.jp/_mem_bin/members/login.asp?/members/"
        self._session = requests.session()
        # 取引履歴のURL
        self._trade_hist_url = "https://s20.si1.kabu.co.jp/ap/PC/Stocks/Stock/History/List"
        self.driver = None
        self._password = None
        self._trade_hist_detail_url = []
        self.trade_data = {}
        self.history_date = "2017年すべて"

    def boot_up_browser(self):
        _options = Options()
        _options.add_argument("--headless")
        self.driver = webdriver.Chrome("chromedriver.exe", chrome_options=_options)
        
    def enter_password(self):
        self._password = getpass('Enter password>>')
        
    def login(self):
        self.driver.get(self._login_url)
        self.driver.find_element_by_name("SsLogonUser").send_keys("01159503")
        self.driver.find_element_by_name("SsLogonPassword").send_keys(self._password)
        # パスワードのボックスでEnterを押下する
        self.driver.find_element_by_id("image1").click()
        self.driver.implicitly_wait(2)
        print("URL:" + self.driver.current_url) 
                
    def get_trading_history_url(self):
        # 指定した年の取引履歴のあるページへ移動する
        self.__move_trade_history_period()
        
        # 最後のページ番号取得する
        last_page_url = self.driver.find_element_by_xpath(
                "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/\
                table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/\
                td[3]/a[2]").get_attribute("href")
        _, last_page = last_page_url.split("PageNo=")
        last_page, _ = last_page.split("&", 1)
        
        # ページ番号をformatメソッドで変換できる、URLのフォーマットを作成する
        page_url_format = last_page_url.replace("PageNo=" + last_page, "PageNo={0}")
        
        # 全ページにある、売買が「売」となっている銘柄の「詳細」ボタンリンク先URLを取得する
        print("売買した銘柄の詳細リンク先URLを抽出中...")
        for i in range(1, int(last_page)):
        #for i in range(1,2):
            current_page_url = page_url_format.format(str(i))
            self.driver.get(current_page_url)
            self.__get_trading_history_detail_URL()
        
        
        """
        cnt = 1
        while history_page_url.format(str(cnt)) != last_page_url:
            self.driver.get(history_page_url.format(str(cnt)))
            print("URL:" + self.driver.current_url)
            cnt += 1
        """
        """
        page_set = set()
        # ページ番号の一覧を示す要素を取得する
        tag_page_num = self.driver.find_element_by_xpath(
                "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td/\
                table[4]/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[2]")
        for tag_a in tag_page_num.find_elements_by_tag_name("a"):
            page_set.add(int(tag_a.text))
        print(page_set)
        """
        """
        trade_history_page_url = self.driver.current_url.replace("PageNo=1", "PageNo={0}")
        for i in range(1, 30):
            result = self.driver.get(trade_history_page_url.format(str(i)))
            print(self.driver.page_source)
        """
        # 売買が「売」となる銘柄の詳細を示すページのURLを取得する
        #self.__get_trading_history_detail_URL()
        
        
        """
        elements = self.driver.find_elements_by_class_name('F_SELcolor')
        for element in elements:
            tag_a = element.find_elements(By.TAG_NAME, "a")
            print(type(tag_a))
            print("URL:" + self.driver.current_url)
        """
    def extract_trading_data(self):
        self.trade_data["name"] = []
        self.trade_data["code"] = []
        self.trade_data["selling_date"] = []
        self.trade_data["purchase_date"] = []
        self.trade_data["holding_day"] = []
        self.trade_data["number_of_stock"] = []
        self.trade_data["purchase_unit_price"] = []
        self.trade_data["selling_unit_price"] = []
        self.trade_data["profit_loss_price"] = []
        self.trade_data["profit_loss_ratio"] = []
        
        for detail_url in self._trade_hist_detail_url:
            
            # 売却ページへ移動する
            self.driver.get(detail_url)
            
            # 銘柄名、コード
            _name , _code = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[1]/tbody/tr[2]/td[2]/a").text.split("/ ")
            self.trade_data["name"].append(_name)
            self.trade_data["code"].append(_code)
            
            # 売却日
            _selling_date = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[1]/tbody/tr[6]/td[2]").text
            _selling_datetime = self.__get_datetime_from_date_str(_selling_date)
            self.trade_data["selling_date"].append(_selling_datetime.strftime("%Y-%m-%d"))
            
            # 株数
            _number_of_stock = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]\
                    /td/table[2]/tbody/tr[2]/td[1]").text
            _number_of_stock = int(_number_of_stock[:-1].replace(",", ""))
            self.trade_data["number_of_stock"].append(_number_of_stock)
            
            # 売却単価
            _selling_price = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[2]/tbody/tr[2]/td[3]").text
            _selling_price = int(_selling_price[:-1].replace(",", ""))
            _selling_unit_price = int(_selling_price/_number_of_stock)
            self.trade_data["selling_unit_price"].append(_selling_unit_price)
            
            # 購入日が２つ以上ある場合は計算が煩雑になるため無視する
            if bool(self.driver.find_elements(By.XPATH, "/html/body/table[4]/tbody/tr[1]/\
                    td[1]/table/tbody/tr[2]/td/table[3]/tbody/tr/td[2]/a[2]")) == True:
                self.trade_data["name"].pop(-1)
                self.trade_data["code"].pop(-1)
                self.trade_data["selling_date"].pop(-1)
                self.trade_data["number_of_stock"].pop(-1)
                self.trade_data["selling_unit_price"].pop(-1)
                continue
            
            # 購入ページへ移動する
            _purchase_url = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[3]/tbody/tr/td[2]/a").get_attribute("href")
            self.driver.get(_purchase_url)
 
            # 購入日
            _purchase_date = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[1]/tbody/tr[7]/td[2]").text
            _purchase_datetime = self.__get_datetime_from_date_str(_purchase_date)
            self.trade_data["purchase_date"].append(_purchase_datetime.strftime("%Y-%m-%d"))
            

            # 購入単価
            _purchase_price = self.driver.find_element_by_xpath(
                    "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]/\
                    td/table[2]/tbody/tr[2]/td[3]").text
            _purchase_price = int(_purchase_price[:-1].replace(",", ""))
            _purchase_unit_price = int(_purchase_price/_number_of_stock)
            self.trade_data["purchase_unit_price"].append(_purchase_unit_price)
            
            # 保有日
            _holding_day = self.__get_holding_date(_purchase_date, _selling_date)
            self.trade_data["holding_day"].append(_holding_day)
            
            # 損益価格
            self.trade_data["profit_loss_price"].append(_selling_price-_purchase_price)
            
            # 損益率
            self.trade_data["profit_loss_ratio"].append(
                    round((_selling_price-_purchase_price)/_purchase_price*100, 2)
                    )
    def to_excel(self):
        print("EXCELに書き込み中...")
        df = pd.DataFrame({
                "01.コード": self.trade_data["code"],
                "02.社名": pd.Series(self.trade_data["name"]),
                "06.株数": pd.Series(self.trade_data["number_of_stock"]),
                "07.購入日": pd.Series(self.trade_data["purchase_date"]),
                "08.売却日": pd.Series(self.trade_data["selling_date"]),
                "09.購入単価": pd.Series(self.trade_data["purchase_unit_price"]),
                "10.売却単価": pd.Series(self.trade_data["selling_unit_price"]),
                "03.保有日": pd.Series(self.trade_data["holding_day"]),
                "04.損益価格": pd.Series(self.trade_data["profit_loss_price"]),
                "05.損益率": pd.Series(self.trade_data["profit_loss_ratio"])
                })
        df.to_excel("損益管理表.xlsx", sheet_name=self.history_date)
        
    def __move_trade_history_period(self):
        # 取引履歴のページへ移動する
        self.driver.get(self._trade_hist_url)
        print("URL:" + self.driver.current_url) 
        select_history_date = Select(self.driver.find_element_by_id("PeriodType_Value"))
        # プルダウンメニューから取引履歴の表示する年月を指定する
        select_history_date.select_by_visible_text(self.history_date)
        # 「選択」ボタンをクリックする
        self.driver.find_element_by_xpath(
                "/html/body/table[4]/tbody/tr[1]/td[1]/table/tbody/tr[2]\
                /td/table[2]/tbody/tr/td/form/table/tbody/tr/td[3]/input").click()
        self.driver.implicitly_wait(2)
        print("URL:" + self.driver.current_url)
    
    def __get_trading_history_detail_URL(self):
        table_elem = self.driver.find_element_by_class_name("table1")
        tr_tags = table_elem.find_elements(By.TAG_NAME, "tr")
        for tr in tr_tags:
            # 売買が「売」となっている列の場合
            if tr.find_elements_by_class_name('F_SELcolor'):
                # 「詳細」ボタンのリンク先URLを取得する
                link = tr.find_elements_by_tag_name("a")[1].get_attribute("href")
                self._trade_hist_detail_url.append(link)
                print(link)
    
    def __get_holding_date(self, purchase_date, selling_date):
        _purchase_date = self.__get_datetime_from_date_str(purchase_date)
        _selling_date = self.__get_datetime_from_date_str(selling_date)
        return (_selling_date - _purchase_date).days
    
    def __get_datetime_from_date_str(self, date):
        _gengo = date[:2]
        _year, _date = date.split("年")
        _year = _year[2:]
        _year = Wareki(Gengo(_gengo), int(_year)).to_ad()        
        _month, _date = _date.split("月", 1)
        _day, _ = _date.split("日", 1)
        _year, _month, _day = int(_year), int(_month), int(_day)
        return datetime.date(_year, _month, _day)
        
        
if __name__ == "__main__":
    scraping = GetTradeHistoryFromKabuCom()
    scraping.boot_up_browser()
    scraping.enter_password()
    scraping.login()
    scraping.get_trading_history_url()
    scraping.extract_trading_data()
    scraping.to_excel()
    
    print(scraping.trade_data)

