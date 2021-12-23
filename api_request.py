from requests import Request, Session
import json
import pprint
from dotenv import load_dotenv
import os

# IMPORTANT key yours api keys in secret
load_dotenv() 

# Import our API KEY from https://pro.coinmarketcap.com/account
COIN_API = os.getenv('COIN_API')

# from coin market cap, we use the free API
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'



        
parameters = {
    'symbol' : 'SLP',
    'convert' : 'USD'
    }

headers = {
    
    'Accepts' : 'application/json',
    'X-CMC_PRO_API_KEY' : COIN_API    
        }

seccion = Session()
seccion.headers.update(headers)
response = seccion.get(url, params=parameters)
price_slp = (json.loads(response.text)['data']['SLP']['quote']['USD']['price'])
percent_1h_slp = (json.loads(response.text)['data']['SLP']['quote']['USD']['percent_change_1h'])
# pprint.pprint(json.loads(response.text)['data']['SLP']['quote']['USD']['price'])
# pprint.pprint(json.loads(response.text)['data']['SLP']['quote']['USD']['percent_change_1h'])
    
print(price_slp,percent_1h_slp)