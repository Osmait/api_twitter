from datetime import date
from tweepy import OAuth1UserHandler, API
import pandas as pd
from decouple import config

today = date.today()

CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_TOKEN = config("ACCESS_TOKEN")
TOKEN_SECRET = config("TOKEN_SECRET")


def load():
    auth = OAuth1UserHandler(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, TOKEN_SECRET
    )
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


if __name__ == "__main__":
    data = load()
    print(transform(data))
