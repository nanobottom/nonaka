# -*- coding: utf-8 -*-
"""
@author :ryo
"""
__author__  = 'ryo'
__version__ = '1.0'
__date__    = '2018/11/20'


from stock_share import StockShare
from scraping import scraping_code_from_yahoo_finance
import datetime
import time
import winsound

def execute_timer():
    _stop = True
    print("プログラム実行中...")
    while(_stop):        
        time.sleep(30)       
        if datetime.datetime.now().strftime("%H:%M") == "15:01":
            _stop = False

def main():   
    _codes, _names = [], []
    for i in range(1, 10):
        if i == 1:
            _url_i = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&mk=1"
        else:
            _url_i = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=" + str(i)
        _codes_i, _names_i  = scraping_code_from_yahoo_finance(_url_i)
        _codes.extend(_codes_i)
        _names.extend(_names_i)

    # 銘柄コード毎にルール４が適用される、かつ現在の終値が一目均衡雲の上にあるグラフのみを出力する 
    for code, name in zip(_codes, _names):
        print(".", end = "")
        stock_share = StockShare(code, datetime.date.today().strftime("%Y-%m-%d"))
        stock_share.get_candle_data()
        if (stock_share.is_high_value_for28days() == True and 
            stock_share.is_over_cloud() == True):
            print("\n" + name)
            stock_share.plt()
            ratio = stock_share.calc_change_in_price()
            print("騰落率:" + str(round(ratio,2)) + "%")    

if __name__ == "__main__":
    
    # execute_timer()
    start_time = time.time()
    winsound.Beep(2000, 500)    
    main()
    elapsed_time = time.time() - start_time
    print("\nelapsed time:{0}[min]".format(round(elapsed_time/60, 2)))
    # ビープ音を鳴らす 
    winsound.Beep(2000, 2000)


