# -*- coding: utf-8 -*-
"""
@author :ryo
"""
__author__  = 'ryo'
__version__ = '1.0'
__date__    = '2018/11/20'

import datetime
import requests
import matplotlib.pyplot as plt
#import matplotlib.finance as finance
import mpl_finance as finance
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from quotes import Quotes

class StockShare:
    """
    株価を取得し、インジケータを使用したローソク足の表示ができる。
    
    ルール１「１シグマより上で買う」
    ルール２「ボリンジャーサイクルの初期で買う」
    ルール３「ボラティリティの低いものは買わない」
    ルール４「28日間の終値最良日で買う」
    end_date : yyyy-mm-dd形式で記述する
    """
    def __init__(self, code, end_date = '2019-01-01', term = 100):
        self.code = code
        self.end_date = end_date        
        year, month, day = end_date.split('-')
        year, month, day = int(year), int(month), int(day)
        self.end = datetime.date(year, month, day)
        self.start = self.end - datetime.timedelta(days=term)
        self.ohcl = {}
        # ボリンジャーバンドに用いる移動平均線(SMA)の窓
        self.bolinger_window = 25
        self._span1 = None
        self._span2 = None
        
        self.is_exist_code = True
    
    def get_candle_data(self):
        """株価データ（始値、高値、安値、終値、出来高、日付）を取得する"""
        quotes = Quotes(self.code, self.start, self.end)
        try:
            quotes.get_stock_data()
        except:
            print("存在しないコードです。")
            self.is_exist_code = False
            return
        
        # 株価情報をリスト形式に変換する
        """
        date = [data.date.strftime("%Y-%m-%d") for data in target]
        open = [data.open for data in target]
        close = [data.close for data in target]
        high = [data.high for data in target]
        low = [data.low for data in target]
        volume = [data.volume for data in target]
        """
        # 日付が古い順に並べ替える
        self.ohcl["date"] = quotes.date[::-1]
        self.ohcl["open"] = quotes.open[::-1]
        self.ohcl["close"] = quotes.close[::-1]
        self.ohcl["high"] = quotes.high[::-1]
        self.ohcl["low"] = quotes.low[::-1]
        self.ohcl["volume"] = quotes.volume[::-1]
        
        #self.__get_current_candle_data()

    def plt(self, savefig=False):
        # 動作が重くならないようにクリアする
        plt.clf()
        #fig = plt.figure(figsize=(10, 6))
        fig, (ax, ax2) = plt.subplots(2,1, gridspec_kw = {'height_ratios':[3, 1]}, figsize=(10, 6))
        #ax = fig.add_subplot(111)
        ax.set_title('code:' + str(self.code) + "\n[rule]buy in 5 candle from GC at MACD", loc='center', fontsize=20)
        ax.set_xlabel('day')
        ax.set_ylabel('price')
        ax.autoscale_view()
        ax.patch.set_facecolor('k')  # 背景色
        ax.patch.set_alpha(0.6)  # 透明度
 
        finance.candlestick2_ochl(ax, opens=self.ohcl["open"],\
                                      highs=self.ohcl["high"],\
                                      lows=self.ohcl["low"],\
                                      closes=self.ohcl["close"],\
                                      width=0.5, colorup='r',\
                                      colordown='g', alpha=0.75) 
                 
        # 一目均衡雲をプロットする
        """
        self.__calc_leading_span()
        x_data = [x for x in range(26, 26 + len(self._span1))]
        plt.plot(x_data, self._span1, color="r",alpha=0.5)
        plt.plot(x_data, self._span2, color="b",alpha=0.5)
        plt.fill_between(x_data, self._span1, self._span2, 
                         where=self._span1>self._span2, 
                         facecolor='r',alpha=0.25)
        plt.fill_between(x_data, self._span1, self._span2,
                         where=self._span1<self._span2, 
                         facecolor='b', alpha=0.25)
        """
        self.__plt_bolinger_band(ax)
        self.__plt_envelope(ax)
        self.__plt_upper_support_line(ax)
        self.__plt_GMMA(ax)
        self.__plt_volume(ax)
        #self.__plt_RSI(ax2)
        #self.__plt_RCI(ax2)
        self.__plt_MACD(ax2)
        
        #plt.xlim([0, 105])
        
        plt.grid(True, linestyle='--', color='0.75')
              
        # 画像を保存する
        if savefig == True:
            fig_name = str(self.code) + ".png"
            plt.savefig(fig_name)
            
        fig.tight_layout()
        plt.show()
        
    def calc_change_in_price(self):
        """騰落率を計算する"""
        return (self.ohcl["close"][-1]-self.ohcl["close"][-2])/self.ohcl["close"][-2]*100
    
    def is_high_value_for28days(self):
        """ルール４「28日間の終値最良日で買う」
        28日間のうち直近5日で最良日があるか判定するよう基準を緩める
        """
        x = self.ohcl["close"][-28:]
        max_index = x.index(max(x))
        if (max_index+1) in range(23, 29):
            return True
        else:
            return False
     
    def is_over_cloud(self):
        self.__calc_leading_span()
        if (self.ohcl["close"].index(self.ohcl["close"][-1]) < 26 or
            self.ohcl["close"].index(self.ohcl["close"][-1]) < 26):
            return True
        current_span1 = self._span1[self.ohcl["close"].index(self.ohcl["close"][-1]) -26]
        current_span2 = self._span2[self.ohcl["close"].index(self.ohcl["close"][-1]) -26]
        if (self.ohcl["close"][-1] > current_span1 and
            self.ohcl["close"][-1] > current_span2):
            return True
        else:
            return False
    
            
    def __get_current_candle_data(self):
        """最新のローソク足のデータを取得する（jsmでは現在値を取得することができないため）"""
        _quotes = Quotes()
        # 過去のデータではなく、最新の日付をend_dateに指定した場合の処理を以下に示す
        if  self.end_date == datetime.date.today().strftime("%Y-%m-%d"):
            # 日本経済新聞のページから現在値（当日の終値）　を取得する
            # ※get_priceメソッドで取得したデータの終値が前日の終値のままになっていたため
            _res = requests.get("https://www.nikkei.com/nkd/company/?scode=" + str(self.code))
            _soup = BeautifulSoup(_res.content, 'html.parser')
            _tags = _soup.find(attrs={"class": "m-stockPriceElm_value now"})
            _target = _quotes.get_price(self.code)
            
            if _tags != None:  
                for i, _stock_price_tag in enumerate(_tags):
                    # 2番目の文字は「円」のため、無視する
                    if i == 0:
                        _current_price = float(_stock_price_tag.string.replace(",", ""))
            else:
                # 日経新聞のページから現在の終値を取得できなかった場合はやむを得ずget_priceメソッドの値を採用する
                _current_price = _target.close
            
            # 当日の日足の更新時間が不明なため、前日の値と比較して動作を変える
            # 書き方が汚いため、改善する必要あり
            if (self.ohcl["high"][-1] == _target.high and
               self.ohcl["low"][-1] == _target.low and
               self.ohcl["open"][-1] == _target.open):
                   
                self.ohcl["close"][-1] = _current_price
            
            else:
                self.ohcl["date"].append(_target.date)
                self.ohcl["open"].append(_target.open)
                self.ohcl["high"].append(_target.high)
                self.ohcl["low"].append(_target.low)
                self.ohcl["volume"].append(_target.volume)
                self.ohcl["close"].append(_current_price)
                
        
    def __plt_bolinger_band(self, ax):
        _series = pd.Series(self.ohcl["close"])
        # 移動平均線
        base = _series.rolling(window = self.bolinger_window).mean()
        base.plot(ax=ax, color="y", alpha=0.75)
        # シグマ
        _sigma = _series.rolling(window = self.bolinger_window).std(ddof = 0)
        _SIGMA_RATES = [1, 2, 3, -1, -2, -3]
        for _rate in _SIGMA_RATES:
            sigma_line  = base + _sigma * _rate
            sigma_line.plot(ax=ax, ls="--", color="y",alpha=0.75)
            
    def __plt_envelope(self, ax):
        _series = pd.Series(self.ohcl["close"])
        base = _series.rolling(window=45).mean()
        base.plot(ax=ax, ls="--", color='k')
        _ENVELOPE_RATES = [1.11, 1.12, 0.89, 0.88]
        for _rate in _ENVELOPE_RATES:
            env = base * _rate
            env.plot(ax=ax, color='k')
    
    def __plt_upper_support_line(self, ax):
        """上昇時のサポートラインとして13日ボリンジャーバンド1シグマを表示する"""
        _series = pd.Series(self.ohcl["close"])
        _base13 = _series.rolling(window=13).mean()
        _sigma13 = _series.rolling(window=13).std(ddof=0)
        upper13_sigma  = _base13 + _sigma13
        upper13_sigma.plot(ax=ax, ls="--",  color="w")
        
    def __plt_GMMA(self, ax):
        _series = pd.Series(self.ohcl["close"])
        _SHORT_WINDOWS = [3, 5, 8, 10, 12, 15]
        for window in _SHORT_WINDOWS:
            base = _series.rolling(window=window).mean()
            base.plot(ax=ax, color="c", alpha=0.5)            
        _LONG_WINDOWS = [30, 35, 40, 45, 50, 60]
        for window in _LONG_WINDOWS:
            base = _series.rolling(window=window).mean()
            base.plot(ax=ax, color="m", alpha=0.5)
            
    def __plt_volume(self, ax):
        ax2 = ax.twinx()
        ax2.set_ylim([0, max(self.ohcl["volume"])*4])
        ax2.set_ylabel("volume")
        finance.volume_overlay(ax2, self.ohcl["open"], 
                               self.ohcl["close"],
                               self.ohcl["volume"],
                               colorup='r', colordown='g',
                               width=0.5, alpha=0.5)
        
    def __plt_RSI(self, ax):
        data = pd.Series(self.ohcl["close"])
        ##差分を計算する
        diff = data.diff()

        #最初の数値がNanで欠損してしまうので削除する
        diff_data = diff[1:]

        ## 値上がり幅、値下がり幅をシリーズへ切り分け
        up, down = diff_data.copy(), diff_data.copy()
        up[up < 0] = 0
        down[down > 0] = 0

        # 値上がり幅/値下がり幅の単純移動平均（14)を処理
        up_sma_14 = up.rolling(window=14, center=False).mean()
        down_sma_14 = down.abs().rolling(window=14, center=False).mean()

        # RSIの計算
        RS = up_sma_14 / down_sma_14
        RSI = 100.0 - (100.0 / (1.0 + RS))
        RSI.plot(ax=ax, color="c", alpha=0.5)
        ax.set(ylim = (0,100))
        ax.grid(True)
        
    def __plt_MACD(self, ax):
        ewm_short = pd.Series(self.ohcl["close"]).ewm(span=12).mean()
        ewm_long = pd.Series(self.ohcl["close"]).ewm(span=24).mean()
        macd = ewm_short - ewm_long
        signal = macd.rolling(9).mean()
        macd.plot(ax=ax, color="g", alpha=0.5)
        signal.plot(ax=ax, color="r", alpha=0.5)
        ax.hlines([0], 0, 65, "blue", linestyles='dashed')
        ax.bar(range(len(macd - signal)), macd - signal)
        #ax.hlines([50], 0, 65, "blue", linestyles='dashed')
        ax.grid(True)
        
    def __plt_RCI(self,ax,timeperiod = 9):
        rci = []
        for j in range(len(self.ohcl["close"])):
            if j < timeperiod:
                rci.append(np.nan)    
            else:
                data = pd.DataFrame()
                data['close'] = list(self.ohcl["close"][j-timeperiod:j])
                data = data.reset_index()
                data = data.rename(columns = {'index':'original_index'}) #最初のindex情報を残しておきます
                data = data.sort_values('close',ascending=False).reset_index(drop = True) #closeの値が高い順に並べ替えます
                data = data.reset_index() #indexをresetします
                data['index'] = [i+1 for i in data['index']] #resetしたindexは0〜8なので、1〜9の順位に変換するために1を足します
                data = data.rename(columns = {'index':'price_rank'}) #closeの高い順に並べたindexをprice rankという列名にします
                data = data.set_index('original_index') #元のindexに戻します
                data = data.sort_index() #元のindexに戻します
                data['date_rank'] = np.arange(timeperiod,0,-1) #元のindexに日付順位をつけます
                data['delta'] = [(data.loc[ii,'price_rank']-data.loc[ii,'date_rank'])**2 for ii in range(len(data))] #dの値を計算します
                d = data['delta'].sum() #dの値を計算します
                value = (1-(6*d)/(timeperiod**3-timeperiod))*100 #rciを計算します
                rci.append(value)
        rci = pd.Series(rci)
        rci.plot(ax=ax, color="g", alpha=0.5)     
        ax.grid(True)
        ax.set(ylim = (-100,100))
        
    def __calc_leading_span(self):
        """一目均衡雲に用いる先行スパンを計算する"""
        # 転換線
        _high_series = pd.Series(self.ohcl["high"])
        _low_series = pd.Series(self.ohcl["low"])
        _high9 = _high_series.rolling(window=9,center=False).max()
        _low9  = _low_series.rolling(window=9,center=False).min()
        _change_line = (_high9+_low9)/2
        # 基準線
        _high26 = _high_series.rolling(window=26,center=False).max()
        _low26  = _low_series.rolling(window=26,center=False).min()
        _standart_line = (_high26+_low26)/2
        # 先行スパン1
        self._span1 = (_change_line+_standart_line)/2
        # 先行スパン2
        _high52 = _high_series.rolling(window=52,center=False).max()
        _low52  = _low_series.rolling(window=52,center=False).min()
        self._span2 = (_high52+_low52)/2
            
if __name__ == "__main__":
    today = datetime.date.today()
    stock_share = StockShare(9501, end_date = today.strftime("%Y-%m-%d"))
    #stock_share = StockShare(9501, end_date = "2017-01-06")
    stock_share.get_candle_data()
    stock_share.plt()
    ratio = stock_share.calc_change_in_price()
    print(ratio)
    rule4 = stock_share.is_high_value_for28days()
    print(rule4)
    print(stock_share.is_over_cloud())
        

