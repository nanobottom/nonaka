import requests
from bs4 import BeautifulSoup

proxies = {
    'http':'',
    'https':''
}
SITE_URL = ''
response = requests.get(SITE_URL, proxies=proxies)
soup = BeautifulSoup(response.content, "lxml")

