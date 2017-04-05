import re
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

mediums = session.query(Medium).first()

print(mediums.name)

colors = [(0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255),
          (255,255,0), (0,255,255), (255,0,255), (192,192,192),
          (128,128,128), (128,0,0), (128,128,0), (0,128,0),
          (128,0,128), (0,128,128), (0,0,128)]

results = []
#loop through every color
for color in colors:
    total = 0
    for work in mediums.works:
        for s in work.colors.split("#"):
            fixed = re.sub('\W', '', s)
            if fixed:
                rgb = tuple(int(fixed[i:i+2], 16) for i in (0, 2 ,4))
                diff = (color[0] - rgb[0])**2 + (color[1] - rgb[1])**2 + (color[1] - rgb[1])**2
                total += diff
    results.append(total)
        
print(results)

ix = 0
m = results[0]
for i in range(len(results)):
    if results[i] < m:
        ix = i
        
print(colors[ix])
        
    
    
                            

conn.close()
session.close()
