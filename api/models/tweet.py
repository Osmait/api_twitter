
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, Date, String, Text
from config.db import meta,engine

tweet = Table("tweets", meta,
              Column("id", Integer, primary_key=True),
              Column("time", Date),
              Column("user", String(255)),
              Column("tweet", Text))
meta.create_all(engine)