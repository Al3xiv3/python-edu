import requests

url = 'https://auto.drom.ru/audi/a5/page7/'

req = requests.get(url)

import bs4

soup = bs4.BeautifulSoup(req.text, 'html.parser')

cars = soup.find_all('div', class_='css-l1wt7n e3f4v4l2')

#print(cars[0].find('span').text)

prices = soup.find_all('div', class_='css-1dv8s3l eyvqki91')
#print(prices[0].find('span').text)

vol = soup.find_all('div', class_='css-1fe6w6s e162wx9x0')

f = open('drom_parsing.txt', 'a', encoding="utf8")

for i in range(len(cars)):
    print(cars[i].find('span').text)
    print(vol[i].find('span').text)
    print(prices[i].find('span').text)
    f.write(f"{cars[i].find('span').text}, {vol[i].find('span').text} {prices[i].find('span').text}\n")


f.close()





