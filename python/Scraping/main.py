import requests
from bs4 import BeautifulSoup
URL = 'https://coinmarketcap.com/'
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')
count = 0
for tr in soup.find_all('tr'):
    name = tr.find("a", {"class": "currency-name-container link-secondary"})
    price = tr.find("a", {"class": "price"})
    volume = tr.find("a", {"class": "volume"})
    if 0 < count < 10:
        print('name   : {}'.format(name.string))
        print('price  : {}'.format(price.string))
        print('volume : {}'.format(volume.string))
    count += 1
