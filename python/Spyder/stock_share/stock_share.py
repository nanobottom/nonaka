# -*- coding: utf-8 -*-
import jsm, datetime
import matplotlib.pyplot as plt
import matplotlib.finance as finance
import pandas as pd

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
        end_list = end_date.split('-')
        self.end = datetime.date(int(end_list[0]),int(end_list[1]), 
                                 int(end_list[2]))
        self.start = self.end - datetime.timedelta(days = term)
        # 株価データを取得する
        q = jsm.Quotes()
        target = q.get_historical_prices(code, jsm.DAILY, self.start, self.end)
        self.ohcl = {}
        date  = [data.date  for data in target]
        open  = [data.open  for data in target]
        close = [data.close for data in target]
        high  = [data.high  for data in target]
        low   = [data.low   for data in target]
        # 日付が古い順に並べ替える
        self.ohcl["date"]  = date[::-1]
        self.ohcl["open"]  = open[::-1]
        self.ohcl["close"] = close[::-1]
        self.ohcl["high"]  = high[::-1]
        self.ohcl["low"]   = low[::-1]   

    def plt(self):
        fig = plt.figure(figsize = (10, 5))
        ax = fig.add_subplot(111)
        ax.set_title('code:' + str(self.code), loc = 'center')
        #ax.invert_xaxis()
        # subplotの背景色を黒色にする
        #ax.patch.set_facecolor('black')
        ax.grid()
        ax.set_xlabel('day')
        ax.set_ylabel('value')
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
        plt.show()
        
    def calc_change_in_price(self):
        # 騰落率を計算する
        return (self.ohcl["close"][-1] - self.ohcl["close"][-2]) / self.ohcl["close"][-2] * 100
    
    def is_high_value_for28days(self):
        # ルール４「28日間の終値最良日で買う」
        x = self.ohcl["close"][-29:-1]
        max_index = x.index(max(x))
        if (max_index + 1 == 28) or (max_index + 1 == 27):
            return True
        else:
            return False
            

if __name__ == "__main__":
    today = datetime.date.today()
    stock_share = StockShare(6701, end_date = today.strftime("%Y-%m-%d"))
    stock_share.plt()
    ratio = stock_share.calc_change_in_price()
    print(ratio)
    rule4 = stock_share.is_high_value_for28days()
    print(rule4)
        

