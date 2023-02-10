from textblob import TextBlob
import pandas as pd
from pathlib import Path
import os
import csv

list = ['I absolutely loved this movie', 'this movie is great', 'This movie was so unbelievably good',
        'The acting was amazing', 'I want to see this movie again', 'I want to see this movie again',
        'The casting was perfect', 'I like this actor', 'Nothing can compare to this movie',
        'This movie was great', 'This movie was shit!']
tweets = []
movieTweets = []

single_tweet = 'I absolutely loved this movie'


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
                numTweets -= 1
            polarity = self.total_polarity + tweet.polarity
        polarity = polarity/numTweets
        return ('% .2f' % polarity)

    def getSubjectivity(self):
        numTweets = self.num_tweets
        for tweet in self.movieTweets:
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


list = []
p = Path('/Users/jaquelinmontes/Desktop/Twitter Sentiment Project/movie_list')
l = p.iterdir()
for item in l:
    list.append(os.path.basename(item))

# print(list)
file = "movie_list/" + list[0] + ''

with open(file) as f:
    reader = csv.reader(f)
    count = 0

    for row in reader:
        print(row)
        if count > 5:
            break
        count += 1


""" total = 0
for line in list:
    tweets.append(TweetObject(line))

movie = MovieObject(tweets)

pol = movie.getPolarity()
subj = movie.getSubjectivity()
print('The total polarity of the movie is: ')
print(pol)

print('The total subjectivity of the movie is: ')
print(subj) """
