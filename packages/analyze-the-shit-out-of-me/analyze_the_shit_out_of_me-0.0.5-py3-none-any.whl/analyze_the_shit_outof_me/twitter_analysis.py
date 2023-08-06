import re
import pandas as pd
from textblob import TextBlob


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


df = pd.read_csv("vaccination_tweets.csv")


def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'

    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def get_data_frame():
    return df


def full_work(df):
    for i in range(0, len(df["text"])):
        df["sentiment"][i] = get_tweet_sentiment(df["text"][i])


def percent_analysis(df):
    postweets = df[df.sentiment == 'positive']
    pnum = round((postweets.shape[0] / df.shape[0]) * 100, 2)
    negtweets = df[df.sentiment == 'negative']
    negnum = round((negtweets.shape[0] / df.shape[0]) * 100, 2)
    neuttweets = df[df.sentiment == 'neutral']
    neutnum = round((neuttweets.shape[0] / df.shape[0]) * 100, 2)

    print("The Percentage of Positive tweets: ", pnum)
    print("The Percentage of Neutral tweets: ", neutnum)
    print("The Percentage of Negative tweets: ", negnum)


full_work(df)
m = get_data_frame()
m.head(30)

percent_analysis(df)