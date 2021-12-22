import tweepy
import schedule
import os
from dotenv import load_dotenv
load_dotenv() 


CONSUKEY = os.getenv('CONSUKEY')
CONSUSEC = os.getenv('CONSUSEC')
KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')



auth = tweepy.OAuthHandler(CONSUKEY, CONSUSEC)
auth.set_access_token(KEY,SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True)


def twitt_price():
    api.update_status('hola')



# def main():
#     schedule.every.hours(3).do(twitt_price)
#     while True:
#         try:
#             schedule.run_pending()
#         except tweepy.TweepError as e:
#             raise e
        
        
        
if __name__ == '__main__':
    twitt_price()