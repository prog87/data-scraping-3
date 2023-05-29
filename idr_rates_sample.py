import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.6780690958188e-05, 'date': 'Mon, 29 May 2023 11:55:01 GMT', 'inverseRate': 14974.388339679},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 6.2213212774234e-05, 'date': 'Mon, 29 May 2023 11:55:01 GMT', 'inverseRate': 16073.755966098}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
