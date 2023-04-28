import requests

url = 'https://www.cnews.ru/'

req = requests.get(url)

import bs4

soup = bs4.BeautifulSoup(req.text, 'html.parser')

news_titles = soup.find_all('section', class_='newstoplist d-flex flex-column d-desktops test1')
news_urls = soup.find_all('li', class_='flex-grow-1')

#print(news_titles[0].find('ul').text)
#print(news_titles[0].find('li').text)


for i in range(len(news_titles)):
    print(news_titles[i].find('li').text.strip())
    print(news_urls[i].find('a').get('href'))
