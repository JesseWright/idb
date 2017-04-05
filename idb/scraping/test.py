from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey, PrimaryKeyConstraint
from sqlalchemy import Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, validates
from datetime import datetime
Base = declarative_base()
 
engine = create_engine('postgresql://postgres:pass@localhost:5432/testtest',
                       echo=True)
 
metadata = MetaData(bind=engine,reflect = True)
metadata.drop_all(checkfirst = False)

_artists_works_relationship = Table('artists_works_relationship',Base.metadata,
                                       Column('artist_id',
                                              Integer,
                                              ForeignKey('artist.id'),
                                              primary_key=True),
                                       Column('work_id', Integer,
                                              ForeignKey('work.id'),
                                              primary_key=True),
                                       PrimaryKeyConstraint('artist_id',
                                                               'work_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Work instances and vice versa.
"""

_artists_media_relationship = Table('_artists_media_relationship',Base.metadata,
                                       Column('artist_id', Integer,
                                              ForeignKey('artist.id'),
                                              primary_key=True),
                                       Column('medium_id', Integer,
                                              ForeignKey('medium.id'),
                                              primary_key=True),
                                       PrimaryKeyConstraint('artist_id',
                                                               'medium_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Medium instances and vice versa. """

_artists_eras_relationship = Table('_artists_eras_relationship',Base.metadata,
                                      Column('artist_id', Integer,
                                             ForeignKey('artist.id'),
                                             primary_key=True),
                                      Column('era_id', Integer,
                                             ForeignKey('era.id'),
                                             primary_key=True),
                                      PrimaryKeyConstraint('artist_id',
                                                              'era_id'))
""" A Table used to create a many-to-many database relationship
between Artist instances and Era instances and vice versa. """

_works_eras_relationship = Table('_works_eras_relationship',Base.metadata,
                                    Column('work_id', Integer,
                                           ForeignKey('work.id'),
                                           primary_key=True),
                                    Column('era_id', Integer,
                                           ForeignKey('era.id'),
                                           primary_key=True),
                                    PrimaryKeyConstraint('work_id',
                                                            'era_id'))
""" A Table used to create a many-to-many database relationship
between Work instances and Era instances and vice versa. """

_media_eras_relationship = Table('_media_eras_relationship',Base.metadata,
                                    Column('medium_id', Integer,
                                           ForeignKey('medium.id'),
                                           primary_key=True),
                                    Column('era_id', Integer,
                                           ForeignKey('era.id'),
                                           primary_key=True),
                                    PrimaryKeyConstraint('medium_id',
                                                            'era_id'))
""" A Table used to create a many-to-many database relationship
between Medium instances and Era instances and vice versa. """

_media_works_relationship = Table('_media_works_relationship',Base.metadata,
                                     Column('medium_id', Integer,
                                            ForeignKey('medium.id'),
                                            primary_key=True),
                                     Column('work_id', Integer,
                                            ForeignKey('work.id'),
                                            primary_key=True),
                                     PrimaryKeyConstraint('medium_id',
                                                             'work_id'))
""" A Table used to create a many-to-many database relationship
between Medium instances and Era instances and vice versa. """
class Artist(Base):
    __tablename__='artist'
    """ A Model that houses information on artists. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Artist. """

    name = Column(String(255), nullable=False)
    """ The unique name of a given Artist. Every Artist must have
    a non-empty name. """

    dob = Column(Date)
    """ The date of birth associated with a given Artist. """

    dod = Column(Date)
    """ The date of death associated with a given Artist. """

    nationality = Column(String(255))
    """ The nationality associated with a given Artist. """

    country = Column(String(255))
    """ The country associated with a given Artist. """

    image = Column(String(255))
    """ A URI for an image associated with a given Work. """

    bio = Column(String(255))
    """ A text entry containing biographical information for an Artist. """

    works = relationship('Work',
                            secondary=_artists_works_relationship,
                            lazy=True,
                            backref=backref('artists', lazy=True))
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
        works = [(work.id, work.title) for work in self.works]
        return "<Artist: {}> {} ({}:{}), {} [Country:{}, Image:{}, " \
               "Bio:{}, Works:{}]".format(self.id,
                                          self.name,
                                          self.dob,
                                          self.dod,
                                          self.nationality,
                                          self.country,
                                          self.image,
                                          self.bio,
                                          works)


class Work(Base):
    __tablename__='work'
    """ A Model that houses information on artworks. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Work. """

    title = Column(String(255), nullable=False)
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

    colors = Column(String(255))
    """ A String representation of a list of HTML-medium color
    representations associated with a Work. """

    image = Column(String(255))
    """ A URI for an image associated with a given Work. """

    motifs = Column(String(255))
    """ A String representation of a list of themes or items
    associated with or found in a given Work. """

    media = relationship('Medium', secondary=_media_works_relationship,
                            lazy=True,
                            backref=backref('works', lazy=True))
    """ A many-to-many database relationship linking Work instances
    to Medium instances and vice versa. """

    @validates('title', include_removes=True)
    def _validate_title(self, key, title, is_remove):
        """ Validate the Work.title attribute.
        Called by the ORM. """
        assert not is_remove \
               and title is not None \
               and not title == '', \
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
        # TODO: Assert types (since going into typed database)
        assert not dimension or dimension > 0, \
            "An artwork must have positive dimensions"
        return dimension

    def __repr__(self):
        """ Return a formatted String representation
        of a given Work. """
        media = [(medium.id, medium.name) for medium in self.media]
        return "<Work: {}> \"{}\", by {} ({}) [Colors:{}, Dimensions:[{}, {}" \
               "{}], Image:{}, Motifs:{}, Media:{}]".format(self.id,
                                                            self.title,
                                                            self.artists,
                                                            self.date,
                                                            self.colors,
                                                            self.height,
                                                            self.width,
                                                            self.depth,
                                                            self.image,
                                                            self.motifs,
                                                            media)


class Medium(Base):
    __tablename__='medium'
    """ A Model that houses information on artistic media. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for a Medium. """

    name = Column(String(255), unique=True, nullable=False)
    """ The unique name of a given Era. Every Era must have a non-empty
    name. """

    colors = Column(String(255))
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

    # TODO: Add avg_depth attribute

    images = Column(String(255))
    """ A String representation of a list of image URIs associated with a
    Medium. """

    countries = Column(String(255))
    """ A String representation of a list of countries associated with a 
    Medium. """

    artists = relationship(Artist,
                              secondary=_artists_media_relationship,
                              lazy=True,
                              backref=backref('media', lazy=True))
    """ A many-to-many database relationship linking Medium instances to
    Artist instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Medium.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and not name == '', \
            "A medium must have a name"
        return name

    @validates('average_age')
    def _validates_average_age(self, key, average_age):
        """ Validate the Medium.average_age attribute.
        Called by the ORM. """
        # TODO: Convert average age to update on updates via trigger
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
        artists = [(artist.id, artist.name) for artist in self.artists]
        return "<Medium: {}> {} [Colors:{}, Averages:[{}, {}, {}, {}], " \
               "Countries:{}, Images:{}, Artists:{}]".format(self.id,
                                                             self.name,
                                                             self.colors,
                                                             self.average_age,
                                                             self.avg_height,
                                                             self.avg_width,
                                                             self.avg_depth,
                                                             self.countries,
                                                             self.images,
                                                             artists)


class Era(Base):
    __tablename__='era'
    """ A Model that houses information on historical periods. """

    id = Column(Integer, primary_key=True)
    """ The unique identifier and primary key for an Era. """

    name = Column(String(255), nullable=False, unique=True)
    """ The unique name of a given Era.
    Every Era must have a non-empty name. """

    type = Column(String(255), nullable=False)
    """ The type description of an Era (e.g., "century").
    Every Era must have a non-empty type. """

    countries = Column(String(255))
    """ A String representation of a list of countries associated
    with an Era. """

    artists = relationship(Artist,
                              secondary=_artists_eras_relationship,
                              lazy=True,
                              backref=backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Artist instances and vice versa. """

    works = relationship(Work, secondary=_works_eras_relationship,
                            lazy=True,
                            backref=backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Work instances and vice versa. """

    media = relationship(Medium, secondary=_media_eras_relationship,
                            lazy=True,
                            backref=backref('eras', lazy=True))
    """ A many-to-many database relationship linking Era instances
    to Medium instances and vice versa. """

    @validates('name', include_removes=True)
    def _validates_name(self, key, name, is_remove):
        """ Validate the Era.name attribute.
        Called by the ORM. """
        assert not is_remove \
               and name is not None \
               and not name == '', \
            "An era must have a name"
        return name

    @validates('type', include_removes=True)
    def validate_type(self, key, type, is_remove):
        """ Validate the Era.type attribute.
        Called by the ORM. """
        # TODO: Make 'type' an Enum
        assert not is_remove \
               and type is not None \
               and not type == '', \
            "An era must have a type"
        return type

    def __repr__(self):
        """ Return a formatted String representation
        of a given Era. """
        artists = [(artist.id, artist.name) for artist in self.artists]
        works = [(work.id, work.title) for work in self.works]
        media = [(medium.id, medium.name) for medium in self.media]
        return "<Era: {}> {} ({}) [Countries:{}, Artists:{}, Works:{}, " \
               "Media:{}]".format(self.id,
                                  self.name,
                                  self.type,
                                  self.countries,
                                  artists,
                                  works,
                                  media)

# create tables in database
Base.metadata.create_all(engine)