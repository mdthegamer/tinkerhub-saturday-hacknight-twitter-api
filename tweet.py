import tweepy
import os
import config
# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.API_KEY,config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN,config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
def send_tweet(message):
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    
    response=api.update_status_with_media(message,'temp.jpg')
    os.remove('temp.jpg')
    print(response)
    return response

def send_tweet_fake(tweet):
    print('______TWITTER.COM___________')
    print(tweet)
    print('____________________________')