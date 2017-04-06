import wikipedia
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, validates,sessionmaker
from sqlalchemy.sql import select
from test import Artist, Work, Medium

Base = declarative_base()
 
engine = create_engine('postgresql://postgres:pass@localhost:5432/test',
                       echo=False)
conn= engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)

artists = session.query(Artist).all()

for artist in artists:
    try:
        bio = wikipedia.summary(artist.name, sentences=2)
        print(bio, end="\n\n")
    except Exception:
        pass
