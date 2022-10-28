
from fastapi import APIRouter
from config.db import conn
from models.tweet import tweet as tw







tweet = APIRouter()

@tweet.get('/')
def tweets():
    return conn.execute(tw.select()).fetchall()



    
        

