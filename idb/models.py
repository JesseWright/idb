from idb import db
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table


class Artist(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    dob = Column(Date)
    dod = Column(Date)
    nationality = Column(String(100))
    image = Column(String(100))
    works = db.relationship('Work', backref='artist', lazy=True)


class Work(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    date = Column(Date)
    medium = Column(String(100))
    height = Column(Integer)
    width = Column(Integer)
    colors = Column(String(100))
    image = Column(String(100))
    artist = Column(Integer, ForeignKey('artist.id'))


class Style(db.Model):
    id = Column(Integer, primary_key=True)
    colors = Column(String(100))
    averageAge = Column(Integer)
    avgHeight = Column(Integer)
    avgWidth = Column(Integer)
    images = Column(String(250))

    # Allows for many-to-many relationships - see http://flask-sqlalchemy.pocoo.org/2.2/models/
    # # Many-to-many relationship between artists and styles
    artistsTable = Table('artists',
                         Column('artist_id', Integer,
                                ForeignKey('artist.id'), primary_key=True),
                         Column('style_id', Integer,
                                ForeignKey('style.id'), primary_key=True)
                         )
    artists = db.relationship('Artist', secondary=artistsTable, lazy=True,
                              backref=db.backref('styles', lazy=True))


class Era(db.Model):
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    countries = Column(String(250))
    media = Column(String(250))

    # Many-to-many relationship between artists and eras
    artistsTable = Table('artists',
                         Column('artist_id', Integer,
                                ForeignKey('artist.id'), primary_key=True),
                         Column('era_id', Integer,
                                ForeignKey('era.id'), primary_key=True)
                         )
    artists = db.relationship('Artist', secondary=artistsTable, lazy=True,
                              backref=db.backref('eras', lazy=True))

    # Many-to-many relationship between works and eras
    worksTable = Table('works',
                       Column('work_id', Integer,
                              ForeignKey('work.id'), primary_key=True),
                       Column('era_id', Integer,
                              ForeignKey('era.id'), primary_key=True)
                       )
    works = db.relationship('Work', secondary=worksTable, lazy=True,
                            backref=db.backref('eras', lazy=True))

    # Many-to-many relationship between styles and eras
    stylesTable = Table('styles',
                        Column('style_id', Integer,
                               ForeignKey('style.id'), primary_key=True),
                        Column('era_id', Integer,
                               ForeignKey('era.id'), primary_key=True)
                        )
    styles = db.relationship('Style', secondary=stylesTable, lazy=True,
                             backref=db.backref('eras', lazy=True))
