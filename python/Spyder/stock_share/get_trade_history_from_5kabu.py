# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:32:57 2018

@author: 亮
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


class GetTradeHistoryFrom5Kabu:
    """
    5日株トレード法の取引履歴のページからEXCELデータで取引履歴を作成する
    """
    def __init__(self, year):
        # 5日株トレード法の通算成績のページ
        self._trade_history_url = "http://kabu5days.com/archives/152"
        # 取得する取引履歴の年
        self._year = year
        self.driver = None
        # 指定した年の取引履歴のURL
        self._trade_history_urls = []
        self.trade_data = {}
        self.filename = "損益管理表5日株.xlsx"
    
    def boot_up_browser(self):
        _options = Options()
        _options.add_argument("--headless")
        self.driver = webdriver.Chrome("chromedriver.exe", chrome_options=_options)
        
    def get_trade_history_urls(self):
        """通算成績のページの指定した年の取引履歴URLを獲得する"""
        
        # 5日株トレード法の通算成績のページへ移動する
        self.driver.get(self._trade_history_url)
        
        # 通算成績のリンクが記載されているテーブルの要素を取得する
        table_elem = self.driver.find_element_by_xpath(
                '//*[@id="post-152"]/div[2]/table')
        tags_a = table_elem.find_elements(By.TAG_NAME, "a")
        
        # "a"タグのテキストに指定した年が含まれていればリンク先URLを取得する
        for a in tags_a:
            if self._year in a.text:
                url = a.get_attribute("href")
                self._trade_history_urls.append(url)
        # 古い月の順に並べ替える
        self._trade_history_url = self._trade_history_url[::-1]
        
    def get_trade_history(self):
        """取得した取引履歴URLから取引履歴を抽出する"""
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
        
        # 月毎の取引履歴ページへ移動する
        #self.driver.get(self._trade_history_urls[0])
        for url in self._trade_history_urls:
            self.driver.get(url)
            print(url)
            #各銘柄の取引履歴が記載されているテーブルの要素を取り出す
            table_elem = self.driver.find_elements_by_tag_name("table")[1]
            #table_elem = self.driver.find_element_by_xpath(
            #       '//*[@id="post-6901"]/div[2]/table[2]')
            tags_tr = table_elem.find_elements(By.TAG_NAME, "tr")
            # ページ内に記載されている銘柄数を取得する
            trade_num = len(tags_tr) - 3
            for i_row in range(1, trade_num + 1):
            
                tr = tags_tr[i_row]
                # 最初の行は飛ばす
                if i_row != 0:
                    tags_td = tr.find_elements(By.TAG_NAME, "td")
                    self.trade_data["number_of_stock"].append(0)
                    self.trade_data["profit_loss_price"].append(0)
                
                    # 各列から株価の情報を変数に格納する
                    for i_data, td in enumerate(tags_td):
                        # コード
                        if i_data == 0:
                            self.trade_data["code"].append(td.text)
                        # 銘柄名
                        elif i_data == 1:
                            self.trade_data["name"].append(td.text)
                        # 売却単価
                        elif i_data == 2:
                            _selling_unit_price = float(td.text.split(" ", 1)[0].replace(",", ""))
                            self.trade_data["selling_unit_price"].append(_selling_unit_price)
                        # 損益率
                        elif i_data == 3:
                            b = td.find_element(By.TAG_NAME, "b")
                            _profit_loss_ratio = float(b.text.split(" ", 1)[0])
                            self.trade_data["profit_loss_ratio"].append(_profit_loss_ratio)
                        # 購入単価
                        elif i_data == 4:
                            _purchase_unit_price = float(td.text.split(" ", 1)[0].replace(",", ""))
                            self.trade_data["purchase_unit_price"].append(_purchase_unit_price)
                        # 購入日、 売却日
                        elif i_data == 5:
                            _purchase_date = td.text
                            _p_month, _p_day = _purchase_date.split("/")
                        elif i_data == 7:
                            _selling_date = td.text
                            _s_month, _s_day = _selling_date.split("/")
                            # 年をまたいでいるか判断する
                            if _p_month > _s_month:
                                _p_year = str(int(self._year) - 1)
                            else:
                                _p_year = self._year
                            _purchase_date = _p_year + "-" + _p_month + "-" + _p_day
                            self.trade_data["purchase_date"].append(_purchase_date)
                            _selling_date = self._year + "-" + _s_month + "-" + _s_day
                            self.trade_data["selling_date"].append(_selling_date)
                        # 保有日    
                        elif i_data == 8:
                            _holding_date = int(td.text.replace("日", ""))
                            self.trade_data["holding_day"].append(_holding_date)

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
        df.to_excel(self.filename, sheet_name=self._year + "年")
        
        
if __name__ == "__main__":
    scraping = GetTradeHistoryFrom5Kabu("2014") 
    scraping.boot_up_browser()
    scraping.get_trade_history_urls()
    scraping.get_trade_history()
    scraping.to_excel()
    print(scraping.trade_data)