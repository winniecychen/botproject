#bot.py

import tweepy
#import Tkinter
import datetime
import time
#from secrets import *

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 

auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
 #Construct the API instance
api = tweepy.API(auth) # create an API object

search = 'China'
phrase = 'do you mean the rebels who are TEMPORARILY occupying the legal territories of the republic of china?'


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

while True:  
    print("Starting twitter scraping at " + str(datetime.datetime.now()))
    for tweet in tweepy.Cursor(api.home_timeline).items(100):
        try:
            if tweet.user.screen_name is not 'winniecychen': 
                text = tweet.text
                if search in text: 
                    user_displayname = tweet.user.screen_name
                    tweet_id = tweet.id
                    url = 'https://twitter.com/' + str(user_displayname) + '/status/' + str(tweet_id)
                    api.update_status(phrase + '\n' + url)    
                    print ("Replied with " + phrase)
        except tweepy.RateLimitError as e:
            print(e.reason)
            time.sleep(900)
        except tweepy.TweepError as e:
            print(e.reason)
            if (e.message[0]['code'] != 187):
               time.sleep(900)
        except StopIteration:
            break
    print("Finished going through 100 tweets in timeline. Beginning sleep for 15 minutes")
    time.sleep(900)
    
        



    
