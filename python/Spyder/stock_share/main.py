# -*- coding: utf-8 -*-
from stock_share import StockShare
from scraping import scraping_code_from_yahoo_finance
import datetime, time, winsound

start_time = time.time()
winsound.Beep(2000, 500)
#　値上がり率のランキングに載る銘柄コードを収集する
url = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&mk=1"
codes, names = scraping_code_from_yahoo_finance(url)
for i in range(2, 5):
    url_i = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=" + str(i)
    codes_i, names_i  = scraping_code_from_yahoo_finance(url_i)
    codes.extend(codes_i)
    names.extend(names_i)

# 銘柄コード毎にルール４が適用される、かつ現在の終値が一目均衡雲の上にあるグラフのみを出力する 
today = datetime.date.today()
for code, name in zip(codes, names):
    print(".", end = "")
    stock_share = StockShare(code, today.strftime("%Y-%m-%d"))
    if stock_share.is_high_value_for28days() == True and stock_share.is_over_cloud == True:
        print("\n" + name)
        stock_share.plt()
        ratio = stock_share.calc_change_in_price()
        print("騰落率:" + str(round(ratio,2)) + "%")
 
elapsed_time = time.time() - start_time
print("\n elapsed time:{0} [min]".format(round(elapsed_time/60, 2)))
# ビープ音を鳴らす 
winsound.Beep(2000, 2000)


