
from asyncio.log import logger

from fastapi import APIRouter
from config.db import conn
from models.tweet import tweet as tw
import logging
logging.basicConfig(level=logging.INFO)

tweet = APIRouter()


@tweet.get('/')
def tweets(limit: int = 10):
    """_summary_

    Args:
        limit (int, optional): _description_. Defaults to 10.

    Returns:
        list: list tweet
    """
    try:
        
        return conn.execute(tw.select().order_by(tw.c.id.desc())).fetchmany(limit)
    except Exception as e:
        logger.error(e)


@tweet.get("/{id:int}")
def one_tweets(id):
    """_summary_

    Args:
        id (int): parameter to search for a tweet

    Returns:
        object: tweet
    """
    try:
        return conn.execute(tw.select().where(tw.c.id == id)).first()
    except Exception as e:
        logger.error(e)


@tweet.get("/{user:str}")
def search_user_tweet(user: str):
    """_summary_

    Args:
        user (str): _description_

    Returns:
        _type_: _description_
    """
    try:
        return conn.execute(tw.select().where(tw.c.user.like(f"{user}%"))).all()
    except Exception as e:
        logger.error(e)
