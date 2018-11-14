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
    def __init__(self, code, end_date = None, term = 200):
        self.code = code
        self.end_date = end_date        
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
        date      = [data.date   for data in target]
        open      = [data.open   for data in target]
        close     = [data.close  for data in target]
        high      = [data.high   for data in target]
        low       = [data.low    for data in target]
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
        tags = soup.find(attrs = {"class": "m-stockPriceElm_value now"})
    
        for i, stock_price_tag in enumerate(tags):
            # 2番目の文字は「円」のため、無視する
            if i == 0:
                current_price = float(stock_price_tag.string.replace(",", ""))
        
        # 当日の日足の更新時間が不明なため、前日の値と比較して動作を変える
        target = q.get_price(code)
        if self.ohcl["high"][-1] == target.high and self.ohcl["low"][-1] == target.low and self.ohcl["open"][-1] == target.open:
            self.ohcl["close"][-1] = current_price
            
        else:
            self.ohcl["date"].append(target.date)
            self.ohcl["open"].append(target.open)
            self.ohcl["high"].append(target.high)
            self.ohcl["low"].append(target.low)
            self.ohcl["close"].append(current_price)
        
        self.span1 = None
        self.span2 = None
    
    def calc_cloud(self):
        # 一目均衡雲を計算する
        # 転換線
        high_series = pd.Series(self.ohcl["high"])
        low_series = pd.Series(self.ohcl["low"])
        high9 = high_series.rolling(window = 9,center=False).max()
        low9 = low_series.rolling(window = 9,center=False).min()
        change_line = ( high9 + low9 ) / 2
        # 基準線
        high26 = high_series.rolling(window = 26,center=False).max()
        low26 =  low_series.rolling(window = 26,center=False).min()
        standart_line = ( high26 + low26 ) / 2
        # 先行スパン1
        self.span1 = (change_line + standart_line) / 2
        # 先行スパン2
        high52 = high_series.rolling(window = 52,center=False).max()
        low52 =  low_series.rolling(window = 52,center=False).min()
        self.span2 = ( high52 + low52 ) / 2
            
    def plt(self, is_savefig = False):
        # 動作が重くならないようにクリアする
        #plt.clf()
        fig = plt.figure(figsize = (10, 7.5))
        ax = fig.add_subplot(111)
        ax.set_title('code:' + str(self.code), loc = 'center', fontsize = 20)
        ax.set_xlabel('day')
        ax.set_ylabel('price')
        ax.autoscale_view()
        ax.patch.set_facecolor('black')# 背景色
        ax.patch.set_alpha(0.6)# 透明度
        finance.candlestick2_ochl(ax, opens  = self.ohcl["open"], 
                                      highs  = self.ohcl["high"],
                                      lows   = self.ohcl["low"], 
                                      closes = self.ohcl["close"], 
                                      width = 0.5, colorup = 'r', 
                                      colordown = 'g', alpha = 0.75)
        # ボリンジャーバンドを計算する
        series = pd.Series(self.ohcl["close"])
        base = series.rolling(window = self.sma_date).mean()
        base.plot(ax = ax, color = "yellow")
        #plt.plot(base, color="#1e8eff")
        sigma = series.rolling(window = self.sma_date).std(ddof = 0)
        upper_sigma  = base + sigma
        upper_sigma.plot(ax = ax, ls = "--", color = "yellow")
        upper2_sigma = base + sigma * 2
        upper2_sigma.plot(ax = ax, ls = "--", color = "yellow")
        upper3_sigma = base + sigma * 3
        upper3_sigma.plot(ax = ax, ls = "--", color = "yellow")
        lower_sigma  = base - sigma
        lower_sigma.plot(ax = ax, ls = "--", color = "yellow")
        lower2_sigma = base - sigma * 2
        lower2_sigma.plot(ax = ax, ls = "--", color = "yellow")
        lower3_sigma = base - sigma * 3
        lower3_sigma.plot(ax = ax, ls = "--", color = "yellow")
        
        # エンベロープを計算する
        base2 = series.rolling(window = 45).mean()
        base2.plot(ls = "--", color = 'k')
        upper_env = base2 * (1 + 0.12)
        upper_env.plot(color = 'k')
        upper_env2 = base2 * (1 + 0.11)
        upper_env2.plot(color = 'k')
        lower_env = base2 * (1 - 0.12)
        lower_env.plot(color = 'k')
        lower_env2 = base2 * (1 - 0.11)
        lower_env2.plot(color = 'k')
        
        # 一目均衡雲を表示する
        self.calc_cloud()
        x_data = [x for x in range(26, 26+len(self.span1))]
        plt.plot(x_data, self.span1, color = "red")
        plt.plot(x_data, self.span2, color = "blue")
        plt.fill_between(x_data, self.span1, self.span2, where=self.span1>self.span2, facecolor='red',alpha = 0.25)
        plt.fill_between(x_data, self.span1, self.span2, where=self.span1<self.span2, facecolor='blue', alpha = 0.25)
        
        
        plt.xlim([80, 138])
        plt.grid(True, linestyle='--', color='0.75')
              
        # 画像を保存する
        if is_savefig == True:
            #date = self.end_date.replace("-", "")
            #fig_name = date + "_" + self.code + ".png"
            fig_name = str(self.code) + ".png"
            plt.savefig(fig_name)
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
     
    def is_over_cloud(self):
        self.calc_cloud()
        current_span1 = self.span1[self.ohcl["close"].index(self.ohcl["close"][-1]) -26]
        current_span2 = self.span2[self.ohcl["close"].index(self.ohcl["close"][-1]) -26]
        if self.ohcl["close"][-1] > current_span1 and self.ohcl["close"][-1] > current_span2:
            return True
        else:
            return False

if __name__ == "__main__":
    today = datetime.date.today()
    stock_share = StockShare(9729, end_date = today.strftime("%Y-%m-%d"))
    stock_share.plt()
    ratio = stock_share.calc_change_in_price()
    print(ratio)
    rule4 = stock_share.is_high_value_for28days()
    print(rule4)
    print(stock_share.is_over_cloud())
        

