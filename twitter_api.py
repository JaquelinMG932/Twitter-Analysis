import tweepy
import configparser
import pandas as pd

# create an instance of config Parser
config = configparser.ConfigParser()
# read keys from config file
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# print(api_key)

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
"""
# make an API instance which gives us access to twitter
api = tweepy.API(auth)
query = '#TheMenuFilm'
tweets = api.search_tweets(
    q=query, lang='en', result_type='recent', count=100, tweet_mode='extended')
columns = ['Users', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

data_frame = pd.DataFrame(data, columns=columns)

data_frame.to_csv("movie-tweets.csv", index=None) """

movie_list = {'Puss In Boots: The Last Wish': '#PussInBootsTheLastWish',
              'Glass Oinion A Knives Out Mystery': '#GlassOnionKnivesOut',
              'The Invitation': '#TheInvitationNetflix',
              'Don\'t Worry Darling': '#DontWorryDarling',
              'Spirited':'#SpiritedMovie',
              'Ticket To Paradise': '#TicketToParadise',
              'Top Gun: Maverick' : '#TopGunMaverick',
              'Bullet Train': '#BulletTrainMob'
              }
