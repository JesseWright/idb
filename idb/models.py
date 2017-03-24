from idb import db
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import validates
from datetime import datetime

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
    name = Column(String(100), nullable=False)
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

    @validates('name', include_removes=True)
    def validates_name(self, key, name, is_remove):
        assert not is_remove \
               and name is not None \
               and not name == '', "An artist must have a name"

    @validates('dob', 'dod')
    def validates_dates(self, key, date):
        assert date <= datetime.now(), "A date cannot be in the future"

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Artist``
        """
        return "{} ({}:{}), {}".format(self.name, self.dob, self.dod, self.nationality)


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

    @validates('title', include_removes=True)
    def validate_title(self, key, title, is_remove):
        assert not is_remove \
               and title is not None \
               and not title == '', "An artwork must have a title"

    @validates('date')
    def validate_date(self, key, date):
        assert date <= datetime.now(), "An artwork cannot have a future date"

    @validates('height', 'width')
    def validates_height(self, key, dimension):
        # TODO: Assert types
        assert dimension > 0, "An artwork must have positive dimensions"

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Work``
        """
        return "\"{}\", by {} ({})".format(self.title, self.artists, self.date)


class Style(db.Model):
    """ A ``Model`` that houses information on artistic styles. """
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    colors = Column(String(100))
    average_age = Column(Float)
    avg_height = Column(Float)
    avg_width = Column(Float)
    images = Column(String(250))

    artists = db.relationship(Artist,
                              secondary=artists_styles_relationship,
                              lazy=True,
                              backref=db.backref('styles', lazy=True))

    @validates('name', include_removes=True)
    def validates_name(self, key, name, is_remove):
        assert not is_remove \
               and name is not None \
               and not name == '', "A style must have a name"

    @validates('average_age')
    def validates_average_age(self, key, average_age):
        # TODO: Convert average age to update on trigger
        assert average_age > 0, "A style must have a positive average age"

    @validates('avg_height', 'avg_width')
    def validates_dimensions(self, key, dimension):
        assert dimension > 0, "A style must have positive average dimensions"

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Style``
        """
        return "{}".format(self.name)


class Era(db.Model):
    """ A ``Model`` that houses information on historical periods. """
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    type = Column(String(50), nullable=False)
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

    @validates('name', include_removes=True)
    def validates_name(self, key, name, is_remove):
        assert not is_remove \
               and name is not None \
               and not name == '', "An era must have a name"

    @validates('type', include_removes=True)
    def validate_type(self, key, type, is_remove):
        # TODO: Make 'type' an Enum
        assert not is_remove \
               and type is not None \
               and not type == '', "An era must have a type"

    def __repr__(self):
        """
        :return: A formatted ``String`` representation of a given ``Era``
        """
        return "{} ({})".format(self.name, self.type)
