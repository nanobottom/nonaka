# -*- coding: utf-8 -*-
"""
@author :ryo
"""
__author__  = 'ryo'
__version__ = '1.0'
__date__    = '2018/11/20'


from stock_share import StockShare
#from stock_share_weekly import StockShareWeekly
from scraping import scraping_code_from_yahoo_finance
import datetime
import time
#import winsound

def execute_timer():
    _stop = True
    print("プログラム実行中...")
    while(_stop):        
        time.sleep(30)
        _weekday = datetime.date.today().weekday()
        if datetime.datetime.now().strftime("%H:%M") == "16:00":
            # 今日が土日以外の場合
            if _weekday in range(0, 5): 
                _stop = False

def main():
    start_time = time.time()
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆START!!☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    #winsound.Beep(2000, 500)
    
    _codes, _names = [], []
    for i in range(1, 4):
    #for i in range(5, 10):
    # 東証1部銘柄で探す
        if i == 1:
            _url_i = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&mk=3"
        else:
            _url_i = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=3&p=" + str(i) 
        _codes_i, _names_i  = scraping_code_from_yahoo_finance(_url_i)
        _codes.extend(_codes_i)
        _names.extend(_names_i)

    # 銘柄コード毎にルール４が適用される、かつ現在の終値が一目均衡雲の上にあるグラフのみを出力する 
    for code, name in zip(_codes, _names):
        print(code + ",", end="")
        stock_share = StockShare(code, datetime.date.today().strftime("%Y-%m-%d"))      
        stock_share.get_candle_data()
        if stock_share.is_exist_code == True:
            # 週足のローソク足を表示する
            #ss_weekly = StockShareWeekly(code, datetime.date.today().strftime("%Y-%m-%d"))
            #ss_weekly.get_candle_data()
            if (stock_share.is_high_value_for28days() == True):
                #stock_share.is_over_cloud() == True):
                #ss_weekly.is_over_cloud() == True):
                print("\n" + name)
                stock_share.plt() 
                #ss_weekly.plt()
                ratio = stock_share.calc_change_in_price()
                print("騰落率:" + str(round(ratio,2)) + "%")
            
    elapsed_time = time.time() - start_time
    print("\nelapsed time:{0}[min]".format(round(elapsed_time/60, 2)))
    # ビープ音を鳴らす 
    #winsound.Beep(2000, 2000)

if __name__ == "__main__":
    """
    while True:
        execute_timer()           
        main()
   """
    main()
        
        


