import requests

import bs4

url = 'https://www.binance.com/ru/price/ethereum'

req = requests.get(url)

soup = bs4.BeautifulSoup(req.text, 'html.parser')

btc_prieces = soup.find_all('div', class_='css-12ujz79')

print(btc_prieces[0].text)

