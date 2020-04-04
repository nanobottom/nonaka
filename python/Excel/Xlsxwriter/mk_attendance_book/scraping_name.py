import requests
from bs4 import BeautifulSoup

SITE_URL = ''
response = requests.get(SITE_URL)
soup = BeautifulSoup(response.content, "lxml")

