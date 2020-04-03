# -*- coding: utf-8 -*-
import python_bitbankcc, datetime
import pandas as pd
import matplotlib.pyplot as plt
import mpl_finance as finance

class CryptoCurrencyCandle:

    def __init__(self, coin_type, end_date = None, term = 150):
        self.coin_type = coin_type
        self.end_date = end_date
        self.term = term
        # 移動平均線（SMA）で平均する日付パラメータ
        self.sma_date = 25
        year, month, day = end_date.split('-')
        self.end = datetime.date(int(year),int(month), 
                                 int(day))
        self.start = self.end - datetime.timedelta(days = term)
        self.ohcl = {}
        self.span1 = None
        self.span2 = None
        
    def __get_candle_from_bitbank(self, year):
        # public API classのオブジェクトを取得
        pub = python_bitbankcc.public()
        value = pub.get_candlestick(self.coin_type, '1day', year)
        ohcl = {}
        candle = value['candlestick'][0]
        ohcl["open"]   = [data[0] for data in candle["ohlcv"]]
        ohcl["high"]   = [data[1] for data in candle["ohlcv"]]
        ohcl["low"]    = [data[2] for data in candle["ohlcv"]]
        ohcl["close"]  = [data[3] for data in candle["ohlcv"]]
        ohcl["volume"] = [data[4] for data in candle["ohlcv"]]
        ohcl["date"]   = [datetime.datetime.fromtimestamp(data[5]/1000).strftime("%Y-%m-%d") for data in candle["ohlcv"]]
        return ohcl
        
    def get_candle_data(self):
        # 前年度、今年度の日足データを統合してデータベースを作成する
        year = self.end.strftime("%Y")
        end_date = self.end.strftime("%Y-%m-%d")
        ohcl_DB = self.__get_candle_from_bitbank(str(int(year) - 1))
        ohcl2 = self.__get_candle_from_bitbank(year)
        ohcl_DB["open"].extend(ohcl2["open"])
        ohcl_DB["high"].extend(ohcl2["high"])
        ohcl_DB["low"].extend(ohcl2["low"])
        ohcl_DB["close"].extend(ohcl2["close"])
        ohcl_DB["volume"].extend(ohcl2["volume"])
        ohcl_DB["date"].extend(ohcl2["date"])
        end_date_pos = ohcl_DB["date"].index(end_date)

        # DBから指定した期間の日足データを取り出す
        self.ohcl["open"] = ohcl_DB["open"][end_date_pos - self.term: end_date_pos + 1]
        self.ohcl["high"] = ohcl_DB["high"][end_date_pos - self.term: end_date_pos + 1]
        self.ohcl["low"] = ohcl_DB["low"][end_date_pos - self.term: end_date_pos + 1]
        self.ohcl["close"] = ohcl_DB["close"][end_date_pos - self.term: end_date_pos + 1]
        self.ohcl["volume"] = ohcl_DB["volume"][end_date_pos - self.term: end_date_pos + 1]
        self.ohcl["date"] = ohcl_DB["date"][end_date_pos - self.term: end_date_pos + 1]
    
    def __calc_cloud(self):
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
        plt.clf()
        fig = plt.figure(figsize = (10, 7.5))
        ax = fig.add_subplot(111)
        ax.set_title('type:' + str(self.coin_type), loc = 'center', fontsize = 20)
        ax.set_xlabel('day')
        ax.set_ylabel('price')
        ax.autoscale_view()
        ax.patch.set_facecolor('black')# 背景色
        ax.patch.set_alpha(0.6)# 透明度
        # ローソク足を上側75%に収める
        #bottom, top = ax.get_ylim()
        #ax.set_ylim(bottom - (top - bottom) / 4, top)
        
        finance.candlestick2_ochl(ax, opens  = self.ohcl["open"], 
                                      highs  = self.ohcl["high"],
                                      lows   = self.ohcl["low"], 
                                      closes = self.ohcl["close"], 
                                      width = 0.5, colorup = 'r', 
                                      colordown = 'g', alpha = 0.75)
        # ボリンジャーバンドを計算する
        series = pd.Series(self.ohcl["close"])
        base = series.rolling(window = self.sma_date).mean()
        base.plot(ax = ax, color = "y",alpha = 0.75)
        #plt.plot(base, color="#1e8eff")
        sigma = series.rolling(window = self.sma_date).std(ddof = 0)
        upper_sigma  = base + sigma
        upper_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        upper2_sigma = base + sigma * 2
        upper2_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        upper3_sigma = base + sigma * 3
        upper3_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        lower_sigma  = base - sigma
        lower_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        lower2_sigma = base - sigma * 2
        lower2_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        lower3_sigma = base - sigma * 3
        lower3_sigma.plot(ax = ax, ls = "--", color = "y",alpha = 0.75)
        
        # 上昇時のサポートラインとして13日ボリンジャーバンド1シグマを表示する
        base13 = series.rolling(window = 13).mean()
        sigma13 = series.rolling(window = 13).std(ddof = 0)
        upper13_sigma  = base13 + sigma13
        upper13_sigma.plot(ax = ax, ls = "--",  color = "w")
        
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
        self.__calc_cloud()
        x_data = [x for x in range(26, 26+len(self.span1))]
        plt.plot(x_data, self.span1, color = "red",alpha = 0.5)
        plt.plot(x_data, self.span2, color = "blue",alpha = 0.5)
        plt.fill_between(x_data, self.span1, self.span2, where=self.span1>self.span2, facecolor='red',alpha = 0.25)
        plt.fill_between(x_data, self.span1, self.span2, where=self.span1<self.span2, facecolor='blue', alpha = 0.25)
        
        # GMMAを表示する
        series = pd.Series(self.ohcl["close"])
        short_windows = [3,5,8,10,12,15]
        for window in short_windows:
            base = series.rolling(window = window).mean()
            base.plot(ax = ax, color = "c", alpha = 0.5)
            
        long_windows = [30,35,40,45,50,60]
        for window in long_windows:
            base = series.rolling(window = window).mean()
            base.plot(ax = ax, color = "m", alpha = 0.5)
        """
        # 出来高を表示する
        ax2 = ax.twinx()
        ax2.set_ylim([0, max(self.ohcl["volume"]) * 4])
        ax2.set_ylabel("volume")
        finance.volume_overlay(ax2, self.ohcl["open"], self.ohcl["close"], self.ohcl["volume"], colorup='r', colordown='g', width=0.5, alpha=0.5)
        #ax2.set_ylim([0, self.ohcl["volume"].max() * 0.5])
        """
        plt.xlim([90, 151])
        plt.grid(True, linestyle='--', color='0.75')
              
        # 画像を保存する
        if is_savefig == True:
            #date = self.end_date.replace("-", "")
            #fig_name = date + "_" + self.code + ".png"
            fig_name = str(self.coin_type) + ".png"
            plt.savefig(fig_name)
        plt.show()
    def calc_change_in_price(self):
        # 騰落率を計算する
        return (self.ohcl["close"][-1] - self.ohcl["close"][-2]) / self.ohcl["close"][-2] * 100
    
if __name__ == "__main__":
    #date = datetime.date.today().strftime("%Y-%m-%d")
    date = "2018-01-01"
    crypto_candle = CryptoCurrencyCandle("xrp_jpy",date)
    crypto_candle.get_candle_data()
    crypto_candle.plt()