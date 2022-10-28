from sqlalchemy import create_engine,MetaData
from decouple import config

DB = config("URL_DB")

engine = create_engine(DB)
meta = MetaData()

conn = engine.connect()