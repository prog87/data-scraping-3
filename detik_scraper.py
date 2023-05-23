import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/search/searchall?', params = {
     'query': 'detik terpopuler',
    'siteid': '2'
})
soup = BeautifulSoup(html_doc.text, 'html.parser')

news_populer = soup.find(attrs={'class':'list media_rows list-berita'})

titles = news_populer.find_all(attrs={'class': 'title'})
images = news_populer.find_all(attrs={'class': 'ratiobox box_thumb'})

for image in images:
    print(image.find('span').find('img')['title'])

# print(titles)