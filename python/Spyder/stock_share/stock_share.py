# -*- coding: utf-8 -*-
import jsm, datetime, requests
import matplotlib.pyplot as plt
import matplotlib.finance as finance
import pandas as pd
from bs4 import BeautifulSoup

class StockShare:
    # ルール１「１シグマより上で買う」
    # ルール２「ボリンジャーサイクルの初期で買う」
    # ルール３「ボラティリティの低いものは買わない」
    # ルール４「28日間の終値最良日で買う」
    # end=time:yyyy-mm-dd形式で記述する
    def __init__(self, code, end_date = None, term = 100):
        self.code = code
        
        # 移動平均線（SMA）で平均する日付パラメータ
        self.sma_date = 25
        year, month, day = end_date.split('-')
        self.end = datetime.date(int(year),int(month), 
                                 int(day))
        self.start = self.end - datetime.timedelta(days = term)
        # 過去の株価データを取得する
        q = jsm.Quotes()
        target = q.get_historical_prices(code, jsm.DAILY, self.start, self.end)
        
        self.ohcl = {}
        date      = [data.date       for data in target]
        open      = [data.open       for data in target]
        close     = [data.close      for data in target]
        high      = [data.high       for data in target]
        low       = [data.low        for data in target]
        # 日付が古い順に並べ替える
        self.ohcl["date"]  = date[::-1]
        self.ohcl["open"]  = open[::-1]
        self.ohcl["close"] = close[::-1]
        self.ohcl["high"]  = high[::-1]
        self.ohcl["low"]   = low[::-1]
        # 当日の株価データを取得する
        # 日本経済新聞のページから現在値（当日の終値）　を取得する
        response = requests.get("https://www.nikkei.com/nkd/company/?scode=" + str(code))
        soup = BeautifulSoup(response.content, 'html.parser')
        current_price_tag = soup.find(attrs = {"class": "m-stockPriceElm_value now"})
        for i, current_price in enumerate(current_price_tag):
            if i == 0:
                self.ohcl["close"].append(float(current_price.string.replace(",", "")))
        target = q.get_price(code)
        self.ohcl["date"].append(target.date)
        self.ohcl["open"].append(target.open)
        self.ohcl["high"].append(target.high)
        self.ohcl["low"].append(target.low)

    def plt(self):
        # 動作が重くならないようにクリアする
        plt.clf()
        fig = plt.figure(figsize = (7.5, 5))
        ax = fig.add_subplot(111)
        ax.set_title('code:' + str(self.code), loc = 'center', fontsize = 20)
        ax.set_xlabel('day')
        ax.set_ylabel('price')
        ax.autoscale_view()
        finance.candlestick2_ochl(ax, opens  = self.ohcl["open"], 
                                      highs  = self.ohcl["high"],
                                      lows   = self.ohcl["low"], 
                                      closes = self.ohcl["close"], 
                                      width = 0.5, colorup = 'r', 
                                      colordown = 'g', alpha = 0.75)
        # ボリンジャーバンドの計算
        series = pd.Series(self.ohcl["close"])
        base = series.rolling(window = self.sma_date).mean()
        base.plot(ax = ax, color = "#1e8eff")
        #plt.plot(base, color="#1e8eff")
        sigma = series.rolling(window = self.sma_date).std(ddof = 0)
        upper_sigma  = base + sigma
        upper_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        upper2_sigma = base + sigma * 2
        upper2_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        upper3_sigma = base + sigma * 3
        upper3_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        lower_sigma  = base - sigma
        lower_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        lower2_sigma = base - sigma * 2
        lower2_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        lower3_sigma = base - sigma * 3
        lower3_sigma.plot(ax = ax, ls = "--", color = "#1e8eff")
        
        # エンベロープを計算する
        base2 = series.rolling(window = 45).mean()
        upper_env = base2 * (1 + 0.12)
        upper_env.plot(color = 'k')
        upper_env2 = base2 * (1 + 0.11)
        upper_env2.plot(color = 'k')
        lower_env = base2 * (1 - 0.12)
        lower_env.plot(color = 'k')
        lower_env2 = base2 * (1 - 0.11)
        lower_env2.plot(color = 'k')
        plt.xlim([68 - 28, 68])
        plt.grid(True, linestyle='--', color='0.75')
        plt.show()
        
    def calc_change_in_price(self):
        # 騰落率を計算する
        return (self.ohcl["close"][-1] - self.ohcl["close"][-2]) / self.ohcl["close"][-2] * 100
    
    def is_high_value_for28days(self):
        # ルール４「28日間の終値最良日で買う」
        x = self.ohcl["close"][-28:]
        max_index = x.index(max(x))
        if max_index + 1 == 28:
            return True
        else:
            return False
            

if __name__ == "__main__":
    today = datetime.date.today()
    stock_share = StockShare(3541, end_date = today.strftime("%Y-%m-%d"))
    stock_share.plt()
    ratio = stock_share.calc_change_in_price()
    print(ratio)
    rule4 = stock_share.is_high_value_for28days()
    print(rule4)
        

