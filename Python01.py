import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carwale.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
data = soup.find_all('div')
