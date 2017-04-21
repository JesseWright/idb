"""Contains the definitions of each SQLAlchemy Model used in IDB."""

from datetime import datetime
from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import validates
from idb import db

# pylint warnings disabled because they conflict
#  with proper usage of SQLAlchemy and declarative Models:
# pylint: disable=W0612,W0613,R0201,R0903,C0103, W0622

# The tables below allow for many-to-many relationships.
# See http://flask-sqlalchemy.pocoo.org/2.2/models/ for reference.

_ARTISTS_WORKS_RELATIONSHIP = db.Table('artists_works_relationship',
                                       Column('artist_id',
                                              Integer,
                                              ForeignKey('artist.id'),
                                              primary_key=True),
                                       Column('work_id', Integer,
                                              ForeignKey('work.id'),
                                              primary_key=True),
                                       db.PrimaryKeyConstraint('artist_id',
                                                               'work_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Work instances and vice versa.
"""

_ARTISTS_MEDIA_RELATIONSHIP = db.Table('_artists_media_relationship',
                                       Column('artist_id', Integer,
                                              ForeignKey('artist.id'),
                                              primary_key=True),
                                       Column('medium_id', Integer,
                                              ForeignKey('medium.id'),
                                              primary_key=True),
                                       db.PrimaryKeyConstraint('artist_id',
                                                               'medium_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Medium instances and vice versa. """

_ARTISTS_ERAS_RELATIONSHIP = db.Table('_artists_eras_relationship',
                                      Column('artist_id', Integer,
                                             ForeignKey('artist.id'),
                                             primary_key=True),
                                      Column('era_id', Integer,
                                             ForeignKey('era.id'),
                                             primary_key=True),
                                      db.PrimaryKeyConstraint('artist_id',
                                                              'era_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Era instances and vice versa. """

_WORKS_ERAS_RELATIONSHIP = db.Table('_works_eras_relationship',
                                    Column('work_id', Integer,
                                           ForeignKey('work.id'),
                                           primary_key=True),
                                    Column('era_id', Integer,
                                           ForeignKey('era.id'),
                                           primary_key=True),
                                    db.PrimaryKeyConstraint('work_id',
                                                            'era_id'))
""" A Table used to create a many-to-many database relationship
between Work instances and Era instances and vice versa. """

_MEDIA_ERAS_RELATIONSHIP = db.Table('_media_eras_relationship',
                                    Column('medium_id', Integer,
                                           ForeignKey('medium.id'),
                                           primary_key=True),
                                    Column('era_id', Integer,
                                           ForeignKey('era.id'),
                                           primary_key=True),
                                    db.PrimaryKeyConstraint('medium_id',
                                                            'era_id'))
""" A Table used to create a many-to-many database relationship
between Medium instances and Era instances and vice versa. """

_MEDIA_WORKS_RELATIONSHIP = db.Table('_media_works_relationship',
                                     Column('medium_id', Integer,
                                            ForeignKey('medium.id'),
                                            primary_key=True),
                                     Column('work_id', Integer,
                                            ForeignKey('work.id'),
                                            primary_key=True),
                                     db.PrimaryKeyConstraint('medium_id',
                                                             'work_id'))
""" A Table used to create a many-to-many database relationship
between Medium instances and Era instances and vice versa. """


class Artist(db.Model):
    """ A Model that houses information on artists. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Artist. """

    name = Column(TEXT, nullable=False)
    """ The unique name of a given Artist. Every Artist must have
    a non-empty name. """

    dob = Column(Date)
    """ The date of birth associated with a given Artist. """

    dod = Column(Date)
    """ The date of death associated with a given Artist. """

    nationality = Column(TEXT)
    """ The nationality associated with a given Artist. """

    country = Column(TEXT)
    """ The country associated with a given Artist. """

    image = Column(TEXT)
    """ A URI for an image associated with a given Work. """

    bio = Column(TEXT)
    """ A text entry containing biographical information for an Artist. """

    works = db.relationship('Work',
                            secondary=_ARTISTS_WORKS_RELATIONSHIP,
                            lazy=True,
                            backref=db.backref('artists', lazy=True))
    """ A many-to-many database relationship linking Artist instances
    to Work instances and vice versa. """
    media = None
    """ A many-to-many database relationship linking Artist instances
    to Medium instances and vice versa. """
    eras = None
    """ A many-to-many database relationship linking Artist instances
    to era instances and vice versa. """

    @validates('name', include_removes=True)
    def __validates_name(self, key, name, is_remove):
        """ Validate the Artist.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and name != '', \
            "An artist must have a name"
        return name

    @validates('dob', 'dod')
    def _validates_dates(self, key, date):
        """ Validate the Artist.dob and Artist.dod attributes.
        Called by the ORM. """
        assert not date or date <= datetime.now().date(), \
            "A date cannot be in the future"
        return date

    def __repr__(self):
        """ Return a formatted String representation
        of a given Artist. """
        return "<Artist: {}> {} ({}:{}), {} [Country:{}, Image:{}, " \
               "Bio:{}]".format(self.id,
                                self.name,
                                self.dob,
                                self.dod,
                                self.nationality,
                                self.country,
                                self.image,
                                self.bio)

    def serialize(self):
        """ Return JSON representation of artist. """
        return {
            "id": self.id,
            "name": self.name,
            "dob": self.dob,
            "dod": self.dod,
            "nationality": self.nationality,
            "country": self.country,
            "image": self.image,
            "bio": self.bio
        }

    def relevance(self, search_terms):
        """ Return (integer) relevancy of artist to search terms"""
        NAME_WEIGHT = 5
        PROP_WEIGHT = 3
        BIO_WEIGHT  = 1
        #WORK_WEIGHT = 2
        #works_str = " ".join([work.title for work in self.works])

        score = 0
        for term in search_terms:
            term = term.lower()
            if self.name:
                score += NAME_WEIGHT * self.name.lower().count(term) /\
                    len(self.name.split(" "))
            if self.nationality:
                score += PROP_WEIGHT * self.nationality.lower().count(term) /\
                    len(self.nationality.split(" "))
            if self.country:
                score += PROP_WEIGHT * self.country.lower().count(term) /\
                    len(self.country.split(" "))
            if self.bio:
                score += BIO_WEIGHT  * self.bio.lower().count(term) /\
                    len(self.bio.split(" "))
            #score += WORK_WEIGHT * works_str.lower().count(term)
        return score

class Work(db.Model):
    """ A Model that houses information on artworks. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Work. """

    title = Column(TEXT, nullable=False)
    """ The unique name of a given Work.
    Every Work must have a non-empty title.
    """

    date = Column(Date)
    """ The date associated with a given Work. """

    height = Column(Numeric)
    """ The height in centimeters of artwork of a given Work. """

    width = Column(Numeric)
    """ The width in centimeters of artwork for a given Work. """

    depth = Column(Numeric)
    """ The depth in centimeters of an artwork for a given Work. """

    colors = Column(TEXT)
    """ A String representation of a list of HTML-medium color
    representations associated with a Work. """

    image = Column(TEXT)
    """ A URI for an image associated with a given Work. """

    motifs = Column(TEXT)
    """ A String representation of a list of themes or items
    associated with or found in a given Work. """

    media = db.relationship('Medium', secondary=_MEDIA_WORKS_RELATIONSHIP,
                            lazy=True,
                            backref=db.backref('works', lazy=True))
    """ A many-to-many database relationship linking Work instances
    to Medium instances and vice versa. """

    artists = None
    """ A many-to-many database relationship linking Work instances
    to Artist instances and vice versa. """

    eras = None
    """ A many-to-many database relationship linking Work instances
    to Era instances and vice versa. """

    @validates('title', include_removes=True)
    def _validate_title(self, key, title, is_remove):
        """ Validate the Work.title attribute.
        Called by the ORM. """
        assert not is_remove \
               and title is not None \
               and title, \
            "An artwork must have a title"
        return title

    @validates('date')
    def _validate_date(self, key, date):
        """ Validate the Work.date attribute.
        Called by the ORM. """
        assert not date or date <= datetime.now().date(), \
            "An artwork cannot have a future date"
        return date

    @validates('height', 'width')
    def _validates_height(self, key, dimension):
        """ Validate the Work.height and Work.width attributes.
        Called by the ORM. """
        assert not dimension or dimension > 0, \
            "An artwork must have positive dimensions"
        return dimension

    def __repr__(self):
        """ Return a formatted String representation
        of a given Work. """
        return "<Work: {}> \"{}\", by {} ({}) [Colors:{}, Dimensions:[{}, {}" \
               "{}], Image:{}, Motifs:{}]".format(self.id,
                                                  self.title,
                                                  self.artists,
                                                  self.date,
                                                  self.colors,
                                                  self.height,
                                                  self.width,
                                                  self.depth,
                                                  self.image,
                                                  self.motifs)

    def serialize(self):
        """ Return JSON representation of work. """
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "colors": self.colors,
            "height": float(self.height) if self.height else None,
            "width": float(self.width) if self.width else None,
            "depth": float(self.depth) if self.depth else None,
            "image": self.image,
            "motifs": self.motifs
        }

    def relevance(self, search_terms):
        """ Return (integer) relevancy of artist to search terms"""
        TITLE_WEIGHT = 5
        MOTIF_WEIGHT = 3
        #MEDIA_WEIGHT = 1
        #media_str = " ".join([medium.name for medium in self.media])

        score = 0
        for term in search_terms:
            term = term.lower()
            if self.title:
                score += TITLE_WEIGHT * self.title.lower().count(term) /\
                    len(self.title.split(" "))
            if self.motifs:
                score += MOTIF_WEIGHT * self.motifs.lower().count(term) /\
                    len(self.motifs.split(" "))
            #score += MEDIA_WEIGHT * media_str.lower().count(term)
        return score


class Medium(db.Model):
    """ A Model that houses information on artistic media. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Medium. """

    name = Column(TEXT, unique=True, nullable=False)
    """ The unique name of a given Era. Every Era must have a non-empty
    name. """

    colors = Column(TEXT)
    """ A String representation of a list of HTML-medium color
    representations associated with a Medium. """

    average_age = Column(Numeric)
    """ The average age in years of artwork for a given Medium. """

    avg_height = Column(Numeric)
    """ The average height in centimeters of artwork for a given Medium. """

    avg_width = Column(Numeric)
    """ The average width in centimeters of artwork for a given Medium. """

    avg_depth = Column(Numeric)
    """ The average depth in centimeters of artwork for a given Medium. """

    images = Column(TEXT)
    """ A String representation of a list of image URIs associated with a
    Medium. """

    countries = Column(TEXT)
    """ A String representation of a list of countries associated with a
    Medium. """

    artists = db.relationship(Artist,
                              secondary=_ARTISTS_MEDIA_RELATIONSHIP,
                              lazy=True,
                              backref=db.backref('media', lazy=True))
    """ A many-to-many database relationship linking Medium instances to
    Artist instances and vice versa. """

    works = None
    """ A many-to-many database relationship linking Medium instances
    to Artist instances and vice versa. """

    eras = None
    """ A many-to-many database relationship linking Medium instances
    to Era instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Medium.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name, \
            "A medium must have a name"
        return name

    @validates('average_age')
    def _validates_average_age(self, key, average_age):
        """ Validate the Medium.average_age attribute.
        Called by the ORM. """
        assert not average_age or average_age > 0, \
            "A medium must have a positive average age"
        return average_age

    @validates('avg_height', 'avg_width', 'avg_depth')
    def _validates_dimensions(self, key, dimension):
        """ Validate the Medium.avg_height and Medium.avg_width
        attributes. Called by the ORM. """
        assert not dimension or dimension > 0, \
            "A medium must have positive average dimensions"
        return dimension

    def __repr__(self):
        """
        :return: A formatted String representation of a given Medium
        """
        return "<Medium: {}> {} [Colors:{}, Averages:[{}, {}, {}, {}], " \
               "Countries:{}, Images:{}]".format(self.id,
                                                 self.name,
                                                 self.colors,
                                                 self.average_age,
                                                 self.avg_height,
                                                 self.avg_width,
                                                 self.avg_depth,
                                                 self.countries,
                                                 self.images)

    def serialize(self):
        """ Return JSON representation of medium. """
        return {
            "id": self.id,
            "name": self.name,
            "colors": self.colors,
            "average_age": float(self.average_age) if self.average_age \
                else None,
            "avg_height": float(self.avg_height) if self.avg_height else None,
            "avg_width":  float(self.avg_width) if self.avg_width else None,
            "avg_depth": float(self.avg_depth) if self.avg_depth else None,
            "countries": self.countries,
            "images" : self.images
        }

    def relevance(self, search_terms):
        """ Return (integer) relevancy of artist to search terms"""
        NAME_WEIGHT = 5
        COUNTRIES_WEIGHT = 2
        #ARTIST_WEIGHT = 1
        #artists_str = " ".join([artist.name for artist in self.artists])

        score = 0
        for term in search_terms:
            term = term.lower()
            if self.name:
                score += NAME_WEIGHT      * self.name.lower().count(term) /\
                    len(self.name.split(" "))
            if self.countries:
                score += COUNTRIES_WEIGHT * self.countries.lower().count(term) /\
                    len(self.countries.split(" "))
            #score += ARTIST_WEIGHT  * artists_str.lower().count(term)
        return score


class Era(db.Model):
    """ A Model that houses information on historical periods. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Era. """

    name = Column(TEXT, nullable=False, unique=True)
    """ The unique name of a given Era.
    Every Era must have a non-empty name. """

    type = Column(TEXT, nullable=False)
    """ The type description of an Era (e.g., "century").
    Every Era must have a non-empty type. """

    countries = Column(TEXT)
    """ A String representation of a list of countries associated
    with an Era. """

    artists = db.relationship(Artist,
                              secondary=_ARTISTS_ERAS_RELATIONSHIP,
                              lazy=True,
                              backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Artist instances and vice versa. """

    works = db.relationship(Work, secondary=_WORKS_ERAS_RELATIONSHIP,
                            lazy=True,
                            backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Work instances and vice versa. """

    media = db.relationship(Medium, secondary=_MEDIA_ERAS_RELATIONSHIP,
                            lazy=True,
                            backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Medium instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Era.name attribute.
        Called by the ORM. """
        assert not is_remove and name, \
            "An era must have a name"
        return name

    @validates('type', include_removes=True)
    def validate_type(self, key, type, is_remove):
        """ Validate the Era.type attribute.
        Called by the ORM. """
        assert not is_remove and type, \
            "An era must have a type"
        return type

    def __repr__(self):
        """ Return a formatted String representation
        of a given Era. """
        return "<Era: {}> {} ({}) [Countries:{}]".format(self.id,
                                                         self.name,
                                                         self.type,
                                                         self.countries)

    def serialize(self):
        """ Return JSON representation of era. """
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "countries": self.countries
        }


    def relevance(self, search_terms):
        """ Return (integer) relevancy of artist to search terms"""
        NAME_WEIGHT = 5
        COUNTRIES_WEIGHT = 2

        score = 0
        for term in search_terms:
            term = term.lower()
            if self.name:
                score += NAME_WEIGHT      * self.name.lower().count(
                    term) / len(self.name.split(" "))
            if self.countries:
                score += COUNTRIES_WEIGHT * self.countries.lower().count(
                    term) / len(self.countries.split(" "))
        return score
