# Coins bot
Currently this bot twitt the next parameters
- The price of the crypto of your choice
- The percentage with respect to 1 hour
- The percentage over 1 week

*Screenshot from my [Twitter](https://twitter.com/GamesCoinsPrice)

![Games coins twitter](tw.png)
## Requerimientos
-  Dev account in [twitter](https://developer.twitter.com/en/portal/dashboard "twitter")
	- CONSUMER_KEY
	- CONSUMER_SECRET
- Account in [Coin market cap pro](https://pro.coinmarketcap.com/account "coinmarketcap") (It's free)
	- ACCESS_TOKEN
	- ACCESS_TOKEN_SECRET

# Let's start

`$ pip install Tweppy`

`$ pip install Schedule`

`$ pip install time`

### Add yours API


## MAIN


You have 2 option, add a .env document or delete all the code that comes after = and add yours API

![Main API](api_main.png)
or
![Your api](code.png)

## api_request
And the same in api_request
![](api_req.png)
You have to add your coin api from coin market cap


## Change at your cryto 
![crypto](param.png)
In api_request your have to change SLP with the crypto of your choice. For example if you want to twitt Bitcoin use BTC or Ethereum you hava to use ETH, you can read the documentation [here](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest).