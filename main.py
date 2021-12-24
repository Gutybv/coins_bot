import tweepy
import schedule
import os
from dotenv import load_dotenv
from api_request import slp
import time

load_dotenv() 
# create a .env file to keep the security of yours Twitter API KEYS
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
# You can find these tokens in this link https://developer.twitter.com/en/portal/dashboard


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
# Authentication 



# Def to twitt
def twitt_price():
    twitt_price = slp()
    api.update_status(twitt_price)
    



# Use time to twitt every x hours
def main():
    schedule.every().hour.do(twitt_price)
    # schedule.every(10).minutes.do(twitt_price)
    while True:
        try:
            schedule.run_pending()
            time.sleep(2)
        except tweepy.TweepError as e:
            raise e
    

if __name__ == '__main__':
    main()