import requests
import json
from urllib.request import urlopen
from selenium import webdriver
import json
import os
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, validates,sessionmaker
from sqlalchemy.sql import select
from test import Artist, Work
from datetime import datetime

Base = declarative_base()
 
engine = create_engine('postgresql://postgres:pass@localhost:5432/testtest',
                       echo=False)
conn= engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)
browser = webdriver.Firefox()
def getArtist(name):
    #s = select([artists]).where(artists.c.name == name)
    #result = conn.execute(s)
    #if(result.fetchone() is not None):
    #    return True
    #else:
    #    return False
    q = session.query(Artist).filter_by(name = name)
    return q
def googleSearch(title,artist):

    searchterm =  title+' '+artist # will also be the name of the folder
    searchterm = searchterm.replace(' ','+')
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0

    x = browser.find_elements_by_xpath("//div[@class='rg_meta']")[0]

    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    imgUrl = json.loads(x.get_attribute('innerHTML'))["ou"]
    return imgUrl



def insertArtist(artobject):
    principalMaker = artobject['principalMakers'][0]
    name = principalMaker['name']
    try:
        dob = datetime.strptime(principalMaker['dateOfBirth'], '%Y-%m-%d').date()
    except:
        dob = None
    try:
        dod = datetime.strptime(principalMaker['dateOfDeath'], '%Y-%m-%d').date()
    except:
        dod = None
    try:
        nationality = principalMaker['nationality']
    except:
        nationality = None
    try:
        image = googleSearch('person',name)
    except:
        image = None
        print('NOOOIMAGEEEEE')

    artist = Artist(name = name, dob = dob, dod = dod, nationality = nationality,
        image = image)
    session.add(artist)
    session.commit()



def insertWork(artobject):
    title = artobject['title']
    try:
        date = datetime.strptime(str(artobject['dating']['year']),'%Y').date()
    except:
        date = None
    try:
        height = None
        width = None
        depth = None
        for dimension in artobject['dimensions']:
            if(dimension['type'] == 'height'):
                height = int(dimension['value'])
                if(dimension['unit'] == 'mm'):
                    height = height/100
            elif(dimension['type'] == 'width'):
                width = int(dimension['value'])
                if(dimension['unit'] == 'mm'):
                    width = width/100
            elif(dimension['type'] == 'depth'):
                depth = int(dimension['value'])
                if(dimension['unit'] == 'mm'):
                    depth = depth/100
    except:
        pass
    try:
        colors = artobject['colors']
    except:
        colors = None
    try:
        if w["webImage"]:
            image =  w["webImage"]["url"]
        else:
            image = googleSearch(w["title"],w['principalMaker'])
    except:
        image = None
        print('NOOOIMAGEEEEE')

    work = Work(date = date, title = title, height = height, width = width,
        depth = depth, colors = colors, image = image)
    session.add(work)
    session.commit()
def getArtistWiki(name):
    pass
url = "https://www.rijksmuseum.nl/api/en/collection"

page = 1

while page<2:
    r = requests.get(url, {'key': 'KRvsD9GG', 'format': 'json', 'ps': 10, 'p': page})
    r.encoding = 'utf-8-sig'
    data = r.json()
   
    #reached end of pages
    if not data['artObjects']:
        break
        
    print("PAGE: " + str(page))

    for artObject in data["artObjects"]:
        a = requests.get(url + "/"  + artObject["objectNumber"], {'key': 'KRvsD9GG', 'format': 'json'})
        a.encoding = 'utf-8-sig'
        print(a.url)
        w = a.json()["artObject"]
        
        print("artist: " + w["principalMaker"])
        print("title: " + w["title"])
        print("medium: " + w["physicalMedium"])
        print("year: " + str(w["dating"]["year"]))
        print("style: " + "TODO")
        print("size: " + str(w["dimensions"]))
        print("colors: " + str(w["colors"]))
        print("dob" + str(w['principalMakers'][0]['dateOfBirth']))
        if w["webImage"]:
            print("image: " + w["webImage"]["url"])
        else:
            print("image: " + googleSearch(w["title"],w['principalMaker']))
        print("content: " + str(w["classification"]["iconClassDescription"]))
        print("")
        artist = getArtist(w['principalMaker']).first()
        if(artist is None):
            insertArtist(w)
        insertWork(w)
    page += 1
conn.close()
session.close()
browser.quit()