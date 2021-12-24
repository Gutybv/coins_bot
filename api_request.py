from requests import Request, Session
import json
import pprint
from dotenv import load_dotenv
import os



def slp():
    # IMPORTANT key yours api keys in secret
    load_dotenv() 

    # Import our API KEY from https://pro.coinmarketcap.com/account
    COIN_API = os.getenv('COIN_API')

    # from coin market cap, we use the free API
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'



    # Chose your fav cripto and convert to your fav fiat money https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
    parameters = {
        'symbol' : 'SLP',
        'convert' : 'USD'
        }

    headers = {
        
        'Accepts' : 'application/json',
        'X-CMC_PRO_API_KEY' : COIN_API    #Use your API KEY
            }

    seccion = Session()
    seccion.headers.update(headers)
    response = seccion.get(url, params=parameters)
    price_slp = (json.loads(response.text)['data']['SLP']['quote']['USD']['price'])
    percent_1h_slp = (json.loads(response.text)['data']['SLP']['quote']['USD']['percent_change_1h'])
    percent_7d_slp = (json.loads(response.text)['data']['SLP']['quote']['USD']['percent_change_7d'])
    
    
    price_slp = round(price_slp,3)
    percent_1h_slp = round(percent_1h_slp,2)
    percent_7d_slp = round(percent_7d_slp,2)
    
    if percent_1h_slp < 0 and percent_7d_slp < 0:
        return(f'The $SLP from @AxieInfinity is now at ${price_slp} \n\U0001F4C9 Is down {percent_1h_slp}% compare to 1 hour ago\n\U0001F4C9 And is down {percent_7d_slp}% compare to 1 week ago\n #BTC #ETH #SLP')
    elif percent_1h_slp > 0 and percent_7d_slp > 0: 
        return(f'The $SLP from @AxieInfinity is now at ${price_slp} \n\U0001F4C8 Is up {percent_1h_slp}% compare to 1 hour ago\n\U0001F4C8 and is up {percent_7d_slp}% compare to 1 week ago\n #BTC #ETH #SLP')
    elif percent_1h_slp < 0 and percent_7d_slp > 0: 
        return(f'The $SLP from @AxieInfinity is now at ${price_slp} \n\U0001F4C9 Is up {percent_1h_slp}% compare to 1 hour ago\n\U0001F4C8 and is up {percent_7d_slp}% compare to 1 week ago\n #BTC #ETH #SLP')
    elif percent_1h_slp > 0 and percent_7d_slp < 0:
        return(f'The $SLP from @AxieInfinity is now at ${price_slp} \n\U0001F4C8 Is up {percent_1h_slp}% compare to 1 hour ago\n\U0001F4C9 and is up {percent_7d_slp}% compare to 1 week ago\n #BTC #ETH #SLP')
    else:
        print()
   
slp()


