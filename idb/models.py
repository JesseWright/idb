# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long
# pylint: disable = no-init



from idb import db
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table, UniqueConstraint, Float



# These below allow for many-to-many relationships - see http://flask-sqlalchemy.pocoo.org/2.2/models/

# Many-to-many relationship between artists and works
artists_works_relationship = db.Table('artists_works_relationship',
                                      Column('artist_id', Integer, ForeignKey('artist.id'), primary_key=True),
                                      Column('work_id', Integer, ForeignKey('work.id'), primary_key=True),
                                      db.PrimaryKeyConstraint('artist_id', 'work_id'))

# Many-to-many relationship between artists and styles
artists_styles_relationship = db.Table('artists_styles_relationship',
                                       Column('artist_id', Integer, ForeignKey('artist.id'), primary_key=True),
                                       Column('style_id', Integer, ForeignKey('style.id'), primary_key=True),
                                       db.PrimaryKeyConstraint('artist_id', 'style_id'))

# Many-to-many relationship between artists and eras
artists_eras_relationship = db.Table('artists_eras_relationship',
                                     Column('artist_id', Integer, ForeignKey('artist.id'), primary_key=True),
                                     Column('era_id', Integer, ForeignKey('era.id'), primary_key=True),
                                     db.PrimaryKeyConstraint('artist_id', 'era_id'))

# Many-to-many relationship between works and eras
works_eras_relationship = db.Table('works_eras_relationship',
                                   Column('work_id', Integer, ForeignKey('work.id'), primary_key=True),
                                   Column('era_id', Integer, ForeignKey('era.id'), primary_key=True),
                                   db.PrimaryKeyConstraint('work_id', 'era_id'))

# Many-to-many relationship between styles and eras
styles_eras_relationship = db.Table('styles_eras_relationship',
                                    Column('style_id', Integer, ForeignKey('style.id'), primary_key=True),
                                    Column('era_id', Integer, ForeignKey('era.id'), primary_key=True),
                                    db.PrimaryKeyConstraint('style_id', 'era_id'))


class Artist(db.Model):
    """ A ``Model`` that houses information on artists. """
    # TODO: Update data types to reflect actual content (e.g., lists, URIs, etc.)
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    dob = Column(Date)
    dod = Column(Date)
    nationality = Column(String(100))
    country = Column(String(50))
    image = Column(String(100))

    # TODO: Look into query/tables w.r.t. speed and efficiency and con
    works = db.relationship('Work',
                            secondary=artists_works_relationship,
                            lazy=True,
                            backref=db.backref('artists', lazy=True))

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Artist``
        """
        return "{} ({}-{}), {}".format(self.name, self.dob, self.dod, self.nationality)


class Work(db.Model):
    """ A ``Model`` that houses information on artworks. """
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    date = Column(Date)
    medium = Column(String(100))
    height = Column(Float)
    width = Column(Float)
    colors = Column(String(100))
    image = Column(String(100))

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Work``
        """
        return "\"{}\", by {} ({})".format(self.title, self.artist.name, self.date)


class Style(db.Model):
    """ A ``Model`` that houses information on artistic styles. """
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    colors = Column(String(100))
    averageAge = Column(Float)
    avgHeight = Column(Float)
    avgWidth = Column(Float)
    images = Column(String(250))

    artists = db.relationship(Artist,
                              secondary=artists_styles_relationship,
                              lazy=True,
                              backref=db.backref('styles', lazy=True))

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Style``
        """
        return "{}".format(self.name)


class Era(db.Model):
    """ A ``Model`` that houses information on historical periods. """
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(String(50))
    countries = Column(String(250))
    media = Column(String(250))

    artists = db.relationship(Artist,
                              secondary=artists_eras_relationship,
                              lazy=True,
                              backref=db.backref('eras', lazy=True))
    works = db.relationship(Work, secondary=works_eras_relationship,
                            lazy=True,
                            backref=db.backref('eras', lazy=True))
    styles = db.relationship(Style, secondary=styles_eras_relationship,
                             lazy=True,
                             backref=db.backref('eras', lazy=True))

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Era``
        """
        return "{} ({})".format(self.name, self.type)
