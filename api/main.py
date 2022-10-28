from datetime import date
from tweepy import OAuth1UserHandler, API
import pandas as pd
from decouple import config
from models.tweet import tweet
from config.db import conn


today = date.today()

CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_TOKEN = config("ACCESS_TOKEN")
TOKEN_SECRET = config("TOKEN_SECRET")


def extract():
    auth = OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
    api = API(auth)
    public_tweets = api.home_timeline()

    data = []

    for tweet in public_tweets:

        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
    return data


def transform(data):

    columns_twitter = ["time", "user", "tweet"]

    twitter_df = pd.DataFrame(data=data, columns=columns_twitter)
    return twitter_df


def load(data):
    for i ,r in data.iterrows():
        conn.execute(tweet.insert().values(r))


if __name__ == "__main__":
    data = extract()
    df = transform(data)
    load(df)



    # df.to_csv(f"tweets-{today}.csv")
