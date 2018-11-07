import requests, re
from bs4 import BeautifulSoup

def scraping_code_from_yahoo_finance(URL):
    codes, names = [], []
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    for code_tag in soup.find_all(href = re.compile("https://stocks.finance.yahoo.co.jp/stocks/detail/")):
        codes.append(code_tag.string)
    
    for name_tag in soup.find_all(class_ = "normal yjSt"):
        names.append(name_tag.string)
    return codes, names
    

if __name__ == "__main__":

    URL1 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=1&tm=d&vl=a" 
    URL2 = "https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&vl=a&mk=1&p=2" 
    codes = scraping_code_from_yahoo_finance(URL1)
    codes2 = scraping_code_from_yahoo_finance(URL2)
    codes.extend(codes2)
    print(codes)

        
