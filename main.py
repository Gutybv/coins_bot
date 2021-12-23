import tweepy
import schedule
import os
from dotenv import load_dotenv


load_dotenv() 
# create a .env file to keep the security of yours Twitter API KEYS
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
# You can find these tokens in this link https://developer.twitter.com/en/portal/dashboard


# Authentication 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Def to twitt
def twitt_price():
    api.update_status('hola mundo')



# Use time to twitt every x hours
def main():
    schedule.every.hours(3).do(twitt_price)
    while True:
        try:
            schedule.run_pending()
        except tweepy.TweepError as e:
            raise e
        

if __name__ == '__main__':
    twitt_price()