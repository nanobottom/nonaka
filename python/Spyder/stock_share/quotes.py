import datetime
import requests
from bs4 import BeautifulSoup
#siteurl = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=4689.T"
class Quotes:

    SITE_URL = "https://info.finance.yahoo.co.jp/history/?code=%(ccode)s.T&sy=%(syear)s&sm=%(smon)s&sd=%(sday)s&ey=%(eyear)s&em=%(emon)s&ed=%(eday)s&tm=%(range_type)s&p=%(page)s"
    COLUMN_LABEL = ('date', 'open', 'high', 'low', 'close', 'volume', 'adj_close')

    def __init__(self, ccode, start_date, end_date):
        self.ccode = ccode
        self.start_date = start_date
        self.end_date = end_date
        self.date = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []
        self.adj_close = []
        self.soup = None
        self.page_num = 0
        # 日足、週足、月足を選択する
        self.range_type = 'd'
        
    def get_page(self, page):
        site_url = self.SITE_URL % {'syear': self.start_date.year, 'smon': self.start_date.month,
                               'sday': self.start_date.day, 'eyear': self.end_date.year, 
                               'emon': self.end_date.month, 'eday': self.end_date.day,
                               'page': page, 'range_type':self.range_type, 'ccode':self.ccode}
        response = requests.get(site_url)
        self.soup = BeautifulSoup(response.content, "lxml")

    def count_max_page(self):
        # 全ページをカウントする
        pages = self.soup.find_all('ul', class_ = 'ymuiPagingBottom clearFix')
        for page in pages:
            a_list = page.find_all('a')
        self.page_num = len(a_list)
        # 1ページのみの場合はリンクが存在しないため0になるのでpage_numを1にする
        if self.page_num == 0:
            self.page_num = 1
    
    def get_stock_data(self):
        self.get_page(1)
        self.count_max_page()
        for current_page in range(self.page_num):
            self.get_page(current_page + 1)
            # 時系列データの表から各値を取り出す
            table = self.soup.find_all('table', class_ = 'boardFin yjSt marB6')[0]
            rows = table.find_all('td')
            for i, row in enumerate(rows):
                # date
                if i % len(self.COLUMN_LABEL) == 0:
                    self.date.append(row.string.replace('年', '-').replace('月', '-').replace('日', ''))
                # open
                elif i % len(self.COLUMN_LABEL) == 1:
                    self.open.append(float(row.string.replace(',', '')))
                # high
                elif i % len(self.COLUMN_LABEL) == 2:
                    self.high.append(float(row.string.replace(',', '')))
                # low
                elif i % len(self.COLUMN_LABEL) == 3:
                    self.low.append(float(row.string.replace(',', '')))
                # close
                elif i % len(self.COLUMN_LABEL) == 4:
                    self.close.append(float(row.string.replace(',', '')))
                # volume
                elif i % len(self.COLUMN_LABEL) == 5:
                    self.volume.append(float(row.string.replace(',', '')))
                # adj_close
                elif i % len(self.COLUMN_LABEL) == 6:
                    self.adj_close.append(float(row.string.replace(',', '')))

if __name__ == '__main__':
    jsm = Quotes(8411, datetime.date(2019, 1, 1), datetime.date(2019, 2, 1))
    jsm.get_stock_data()
    print(jsm.date)



