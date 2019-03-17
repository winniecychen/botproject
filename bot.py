#bot.py

import tweepy
import Tkinter
from secrets import *
from time import sleep

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)
 #Construct the API instance
api = tweepy.API(auth) # create an API object

search = 'Chinese'
phrase = 'do you mean the rebels who are TEMPORARILY occuying the legal territories of the republic of china?'


#for tweet in tweepy.Cursor(api.search, search).items(500):
#    try:
#        text = tweet.text
#        if 'Taiwan' in text: 
#            user_displayname = tweet.user.screen_name
#            tweet_id = tweet.id
#            url = 'https://twitter.com/' + str(user_displayname) + '/status/' + str(tweet_id)
#            api.update_status(phrase + '\n' + url)    
#            print ("Replied with " + phrase)
#    except tweepy.TweepError as e:
#        print(e.reason)
#    except StopIteration:
#        break

interval = 30
 
while True:  
    for tweet in tweepy.Cursor(api.home_timeline).items(50):
        try:
            if tweet.user.screen_name is not 'winniecychen': 
                text = tweet.text
                if search in text: 
                    user_displayname = tweet.user.screen_name
                    tweet_id = tweet.id
                    url = 'https://twitter.com/' + str(user_displayname) + '/status/' + str(tweet_id)
                    api.update_status(phrase + '\n' + url)    
                    print ("Replied with " + phrase)
                    time.sleep(interval)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    



    
