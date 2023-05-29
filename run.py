import requests
from bs4 import BeautifulSoup
# jangan di ketik from flask import flask
from flask import *

app = Flask(__name__)
@app.route('/')
def home():
    # return 'Test'
    return render_template('base.html')
# masuk ke terminal dan jalankan python run.py
# untuk return 'Test' ketika sudah masuk local host maka akan muncul Test
# kemudian dirubah menjadi return render_template('index.html')
# Buat direktori template
# setelah itu buat file baru index.html

# kita gunakan bootsrap4
# masuk ke navbar brand/logo
# copy dan masuk ke index.html

# Buat route dan fungsi
@app.route('/news-popular')
def news_popular():
    html_doc = requests.get('https://www.detik.com/search/searchall?', params={
        'query': 'detik terpopuler',
        'siteid': '2'
    })
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    news_populer = soup.find(attrs={'class': 'list media_rows list-berita'})

    titles = news_populer.find_all(attrs={'class': 'title'})
    images = news_populer.find_all(attrs={'class': 'ratiobox box_thumb'})

    return render_template('detik-scraper.html', images=images)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())




if __name__ == '__main__':
    app.run(debug=True)
