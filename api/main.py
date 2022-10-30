from asyncio.log import logger
from datetime import datetime
from tweepy import OAuth1UserHandler, API
import pandas as pd
from decouple import config
from models.tweet import tweet
from config.db import conn
import logging

logging.basicConfig(level=logging.INFO)


today = datetime.now()

CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_TOKEN = config("ACCESS_TOKEN")
TOKEN_SECRET = config("TOKEN_SECRET")


def extract():
    try:
        logger.info("Search tweet...")
        auth = OAuth1UserHandler(
            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, TOKEN_SECRET)
        api = API(auth)
    except Exception as e:
        logger.error(e)

    public_tweets = api.home_timeline()

    data = []

    for tweet in public_tweets:

        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])
    return data


def transform(data):
    logger.info("Trasform...")

    columns_twitter = ["time", "user", "tweet"]

    twitter_df = pd.DataFrame(data=data, columns=columns_twitter)
    return twitter_df


def load(data):

    for i, r in data.iterrows():

        try:
            tw_database = conn.execute(
                tweet.select().where(tweet.c.tweet == r.tweet)).all()
        except Exception as e:
            logger.info(e)

        if tw_database != []:
            logger.info("this tweet exists in DataBase")
        else:
            try:
                conn.execute(tweet.insert().values(r))
            except Exception as e:
                logger.error(e)

            logger.info(f"loading: {r.user}")
    logger.info(f"All Ready--{today}")


def main():
    data = extract()
    df = transform(data)
    load(df)


if __name__ == "__main__":
    main()
