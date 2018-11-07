# -*- coding: utf-8 -*-
from stock_share import StockShare
from scraping import scraping_code_from_yahoo_finance
import datetime
# 値上がり率ランキング
URL1 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=1&tm=d&vl=a" 
URL2 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=2"
URL3 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=3"
# 年初来高値更新ランキング
URL4 = "https://info.finance.yahoo.co.jp/ranking/?kd=29&mk=1&tm=d&vl=a"
#　ランキングに載る銘柄コードを収集する
codes, names    = scraping_code_from_yahoo_finance(URL1)
codes2, names2  = scraping_code_from_yahoo_finance(URL2)
codes.extend(codes2)
names.extend(names2)
codes3, names3  = scraping_code_from_yahoo_finance(URL3)
codes.extend(codes3)
names.extend(names3)
codes4, names4  = scraping_code_from_yahoo_finance(URL4)
codes.extend(codes4)
names.extend(names4)

# 銘柄コード毎にルール４が適用されるグラフのみを出力する
today = datetime.date.today()
i = 0
for code in codes:
     print(".", end = "")
     name = names[i]
     i+= 1
     stock_share = StockShare(code, today.strftime("%Y-%m-%d"))
     if stock_share.is_high_value_for28days() == True:
         print("\n" + name)
         stock_share.plt()
         ratio = stock_share.calc_change_in_price()
         print("騰落率:" + str(ratio))
 
