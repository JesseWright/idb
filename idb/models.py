from idb import db
from sqlalchemy import Column, String, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import validates
from datetime import datetime

# These below allow for many-to-many relationships.
# See http://flask-sqlalchemy.pocoo.org/2.2/models/ for reference.

_artists_works_relationship = db.Table('artists_works_relationship',
                                       Column('artist_id',
                                              Integer,
                                              ForeignKey('artist.id'),
                                              primary_key=True),
                                       Column('work_id', Integer,
                                              ForeignKey('work.id'),
                                              primary_key=True),
                                       db.PrimaryKeyConstraint('artist_id',
                                                               'work_id'))
"""
A Table used to create a many-to-many database relationship
between Artist instances and Work instances and vice versa.
"""

_artists_styles_relationship = db.Table('_artists_styles_relationship',
                                        Column('artist_id', Integer,
                                               ForeignKey('artist.id'),
                                               primary_key=True),
                                        Column('style_id', Integer,
                                               ForeignKey('style.id'),
                                               primary_key=True),
                                        db.PrimaryKeyConstraint('artist_id',
                                                                'style_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Style instances and vice versa. """

_artists_eras_relationship = db.Table('_artists_eras_relationship',
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

works_eras_relationship = db.Table('works_eras_relationship',
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

styles_eras_relationship = db.Table('styles_eras_relationship',
                                    Column('style_id', Integer,
                                           ForeignKey('style.id'),
                                           primary_key=True),
                                    Column('era_id', Integer,
                                           ForeignKey('era.id'),
                                           primary_key=True),
                                    db.PrimaryKeyConstraint('style_id',
                                                            'era_id'))
""" A Table used to create a many-to-many database relationship
between Style instances and Era instances and vice versa. """


class Artist(db.Model):
    """ A Model that houses information on artists. """

    # TODO: Update data types to reflect actual content
    # (e.g., lists, URIs, etc.)

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Artist. """

    name = Column(String(100), nullable=False)
    """ The unique name of a given Artist. Every Artist must have
    a non-empty name. """

    dob = Column(Date)
    """ The date of birth associated with a given Artist. """

    dod = Column(Date)
    """ The date of death associated with a given Artist. """

    nationality = Column(String(100))
    """ The nationality associated with a given Artist. """

    country = Column(String(50))
    """ The country associated with a given Artist. """

    image = Column(String(100))
    """ A URI for an image associated with a given Work. """

    # TODO: Look into query/tables w.r.t. speed and efficiency and con
    works = db.relationship('Work',
                            secondary=_artists_works_relationship,
                            lazy=True,
                            backref=db.backref('artists', lazy=True))
    """ A many-to-many database relationship linking Artist instances
    to Work instances and vice versa. """

    @validates('name', include_removes=True)
    def __validates_name(self, key, name, is_remove):
        """ Validate the Artist.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and not name == '', \
            "An artist must have a name"

    @validates('dob', 'dod')
    def _validates_dates(self, key, date):
        """ Validate the Artist.dob and Artist.dod attributes.
        Called by the ORM. """
        assert date <= datetime.now(), \
            "A date cannot be in the future"

    def __repr__(self):
        """ Return a formatted String representation
        of a given Artist. """
        return "{} ({}:{}), {}".format(self.name, self.dob, self.dod,
                                       self.nationality)


class Work(db.Model):
    """ A Model that houses information on artworks. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Work. """

    title = Column(String(100), nullable=False)
    """ The unique name of a given Work.
    Every Work must have a non-empty title.
    """

    date = Column(Date)
    """ The date associated with a given Work. """

    medium = Column(String(100))
    """ The primary type of medium associated with a given ork. """

    height = Column(Float)
    """ The height in centimeters of artwork of a given Work. """

    width = Column(Float)
    """ The width in centimeters of artwork for a given Work. """

    colors = Column(String(100))
    """ A String representation of a list of HTML-style color
    representations associated with a Work. """

    image = Column(String(100))
    """ A URI for an image associated with a given Work. """

    @validates('title', include_removes=True)
    def _validate_title(self, key, title, is_remove):
        """ Validate the Work.title attribute.
        Called by the ORM. """
        assert not is_remove \
               and title is not None \
               and not title == '', \
            "An artwork must have a title"

    @validates('date')
    def _validate_date(self, key, date):
        """ Validate the Work.date attribute.
        Called by the ORM. """
        assert date <= datetime.now(), \
            "An artwork cannot have a future date"

    @validates('height', 'width')
    def _validates_height(self, key, dimension):
        """ Validate the Work.height and Work.width attributes.
        Called by the ORM. """
        # TODO: Assert types (since going into typed database)
        assert dimension > 0, \
            "An artwork must have positive dimensions"

    def __repr__(self):
        """ Return a formatted String representation
        of a given Work. """
        return "\"{}\", by {} ({})".format(self.title, self.artists, self.date)


class Style(db.Model):
    """ A Model that houses information on artistic styles. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Style. """

    name = Column(String(50), unique=True, nullable=False)
    """ The unique name of a given Era. Every Era must have a non-empty
    name. """

    colors = Column(String(100))
    """ A String representation of a list of HTML-style color
    representations associated with a Style. """

    average_age = Column(Float)
    """ The average age in years of artwork for a given Style. """

    avg_height = Column(Float)
    """ The average height in centimeters of artwork for a given Style. """

    avg_width = Column(Float)
    """ The average width in centimeters of artwork for a given Style. """

    images = Column(String(250))
    """ A String representation of a list of image URIs associated with a
    Style. """

    artists = db.relationship(Artist,
                              secondary=_artists_styles_relationship,
                              lazy=True,
                              backref=db.backref('styles', lazy=True))
    """ A many-to-many database relationship linking Style instances to
    Artist instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Style.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and not name == '', \
            "A style must have a name"

    @validates('average_age')
    def _validates_average_age(self, key, average_age):
        """ Validate the Style.average_age attribute.
        Called by the ORM. """
        # TODO: Convert average age to update on trigger
        assert average_age > 0, \
            "A style must have a positive average age"

    @validates('avg_height', 'avg_width')
    def _validates_dimensions(self, key, dimension):
        """ Validate the Style.avg_height and Style.avg_width
        attributes. Called by the ORM. """
        assert dimension > 0, \
            "A style must have positive average dimensions"

    def __repr__(self):
        """
        :return: A formatted String representation of a given Style
        """
        return "{}".format(self.name)


class Era(db.Model):
    """ A Model that houses information on historical periods. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Era. """

    name = Column(String(50), nullable=False, unique=True)
    """ The unique name of a given Era.
    Every Era must have a non-empty name. """

    type = Column(String(50), nullable=False)
    """ The type description of an Era (e.g., "century").
    Every Era must have a non-empty type. """

    countries = Column(String(250))
    """ A String representation of a list of countries associated
    with an Era. """

    media = Column(String(250))
    """ A String representation of a list of different types
    of art media associated with an Era. """

    artists = db.relationship(Artist,
                              secondary=_artists_eras_relationship,
                              lazy=True,
                              backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Artist instances and vice versa. """

    works = db.relationship(Work, secondary=works_eras_relationship,
                            lazy=True,
                            backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Work instances and vice versa. """

    styles = db.relationship(Style, secondary=styles_eras_relationship,
                             lazy=True,
                             backref=db.backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Style instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Era.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and not name == '', \
            "An era must have a name"

    @validates('type', include_removes=True)
    def validate_type(self, key, type, is_remove):
        """ Validate the Era.type attribute.
        Called by the ORM. """
        # TODO: Make 'type' an Enum
        assert not is_remove \
               and type is not None \
               and not type == '', \
            "An era must have a type"

    def __repr__(self):
        """ Return a formatted String representation
        of a given Era. """
        return "{} ({})".format(self.name, self.type)
