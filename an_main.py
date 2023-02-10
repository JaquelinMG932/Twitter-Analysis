import numpy
import pandas as pandas
from textblob import TextBlob

movieFileNames = ['AManCalledOtto-tweets.csv', 'AvatarTheWayOfWater-tweets.csv', 'BlackPanther_ Wakanda Forever-tweets.csv',
                  'BulletTrain-tweets.csv', 'Crush-tweets.csv', 'DeathOnTheNile-tweets.csv', 'DontWorryDarling-tweets.csv',
                  'ElvisMovie-tweets.csv', 'GlassOnionKnivesOut-tweets.csv', 'HalloweenEnds-tweets.csv',
                  'JurassicWorldDominion-tweets.csv', 'Minions-tweets.csv', 'MultiverseOfMadness-tweets.csv',
                  'MyPoliceman-tweets.csv', 'PinocchioMovie-tweets.csv', 'PussInBootsTheLastWish-tweets.csv',
                  'ScreamV-tweets.csv', 'SMILEMovie-tweets.csv', 'Spirited-tweets.csv', 'themenu-tweets.csv',
                  'TheBatman-tweets.csv', 'TheInvitation-tweets.csv', 'TicketToParadise-tweets.csv',
                  'TopGunMaverick-tweets.csv', 'WhereTheCrawdadsSing-tweets.csv']

movieProperNames = ['A Man Called Otto', 'Avatar: the Way of Water', 'Black Panther: Wakanda Forever', 'Bullet Train',
                    'Crush', 'Death on the Nile', 'Don\'t Worry Darling', 'Elvis', 'Glass Onion: A Knives Out Story',
                    'Halloween Ends', 'Jurassic World: Dominion', 'Minions: The Rise of Gru',
                    'Doctor Strange in the Multiverse of Madness', 'My Policeman', 'Pinocchio',
                    'Puss in Boots: The Last Wish', 'Scream V', 'Smile', 'Spirited', 'The Menu', 'The Batman',
                    'The Invitation', 'Ticket to Paradise', 'Top Gun: Maverick', 'Where the Crawdads Sing']


movieTweets = []
movies = []
scoreList = []


class MovieObject:
    def __init__(self, all_tweets):
        self.movieTweets = all_tweets
        self.total_subjectivity = 0
        self.total_polarity = 0
        self.num_tweets = len(all_tweets)
        # self.movieName =

    def getPolarity(self, movie_tweets):
        numTweets = self.num_tweets
        for tweet in movie_tweets:
            if (tweet.polarity == 0.0):
                numTweets -= 1
            polarity = self.total_polarity + tweet.polarity
        polarity = polarity/numTweets
        return ('% .2f' % polarity)

    def getSubjectivity(self, movie_tweets):
        numTweets = self.num_tweets
        for tweet in movie_tweets:
            if (tweet.subjectivity == 0.0):
                numTweets -= 1
            subjectivity = self.total_subjectivity + tweet.subjectivity
        subjectivity = subjectivity/numTweets
        return ('% .2f' % subjectivity)


class TweetObject:
    def __init__(self, tweet):
        self.tweet = TextBlob(tweet)
        self.polarity = self.tweet.polarity
        self.subjectivity = self.tweet.subjectivity


total = 0
# /Users/jaquelinmontes/Desktop/Twitter Sentiment Project/movie_list
selcols = ['text']
index = 0
for movie in movieFileNames:
    tweets = []
    tweetObjects = []
    with open('/Users/jaquelinmontes/Desktop/Twitter Sentiment Project/movie_list/' + movie, 'rb') as file:
        df = pandas.read_csv(file, usecols=selcols)
    df = df.values.tolist()
    for line in df:
        for line2 in line:
            tweets.append(line2)
            tweetObjects.append(TweetObject(line2))
    movie = MovieObject(tweets)
    movies.append(movie)
    tweetPolarities = []
    tweetSubjectivities = []
    for tweet in tweetObjects:
        tweetPolarities.append(tweet.polarity)
        tweetSubjectivities.append(tweet.subjectivity)
    polarityTotal = numpy.average(tweetPolarities)
    subjectivityTotal = numpy.average(tweetSubjectivities)
    scoreList.append(
        [movieProperNames[index], polarityTotal, subjectivityTotal])
    index += 1

movie = MovieObject(tweets)
print(scoreList)

#print('The total polarity of the movie is: ')

#print('The total subjectivity of the movie is: ')
