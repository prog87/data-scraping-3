import requests
from bs4 import BeautifulSoup

from flask import *

app = Flask(__name__)
@app.route('/')
def home():
    return 'Test'






if __name__ == '__main__':
    app.run(debug=True)
