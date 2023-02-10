# Not working proberly
import pandas as pd
from pathlib import Path
import os
import csv
from textblob import TextBlob


class MovieObject:
    def __init__(self, all_tweets):
        self.movieTweets = all_tweets
        self.total_subjectivity = 0
        self.total_polarity = 0
        self.num_tweets = len(all_tweets)

    def getPolarity(self):
        numTweets = self.num_tweets
        for tweet in self.movieTweets:
            if (tweet.polarity == 0.0):
                numTweets -= 13
            polarity = self.total_polarity + tweet.polarity
        polarity = polarity/numTweets
        return (polarity)

    def getSubjectivity(self):
        try:
            numTweets = self.num_tweets
            for tweet in self.movieTweets:
                if (tweet.subjectivity == 0.0):
                    numTweets -= 1
                subjectivity = self.total_subjectivity + tweet.subjectivity
            subjectivity = subjectivity/numTweets
            return (subjectivity)
        except ZeroDivisionError:
            pass


class TweetObject:
    def __init__(self, tweet):
        self.tweet = TextBlob(tweet)
        self.polarity = self.tweet.polarity
        self.subjectivity = self.tweet.subjectivity


paths = []
p = Path('/Users/jaquelinmontes/Desktop/Twitter Sentiment Project/movie_list')
l = p.iterdir()
for item in l:
    paths.append(os.path.basename(item))

all_values = []

for i in paths:

    file = "movie_list/" + i + ''
    # print(file)
    data = []

    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            data.append(row)

    col = ['num', 'text', 'history', 'created_at', 'context_annotations', 'id']
    data_frame = pd.DataFrame(data, columns=col)
# print(data_frame.head)
    tweet = data_frame['text']
    print(tweet)
    twit_tweets = []
    for item in tweet:
        twit_tweets.append(TweetObject(item))

    movie = MovieObject(twit_tweets)
    movie_name = i.replace('-tweets.csv', '')
    #movie_name = movie_name.replace('-tweets.csv', '')
    values_list = [movie_name, movie.getPolarity(),
                   movie.getSubjectivity()]
    all_values.append(values_list)


# print(all_values)
# print(len(all_values))
