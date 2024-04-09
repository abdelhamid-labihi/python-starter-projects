import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for article in soup.find_all('article'):
    title = article.h3.a.attrs['title']
    rating = article.p.attrs['class'][1]
    price = article.select('.price_color')[0].get_text()
    print(f'\nTitle: {title} | Rating: {rating} | Price: {price}')