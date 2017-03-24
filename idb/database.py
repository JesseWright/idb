# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = line-too-long

from datetime import date
from models import Work, Artist, Style, Era


def get_default_model_instances():
    """
    Generates a container of test instances of :class:`Model`s defined  in models.py.
    This method is only meant for testing purposes or to initialize a database for the first time.

    :return: An iterable container of :class:`Model` instances.
    """

    # Works
    milkmaid = Work(title='The Milkmaid',
                    date=date(1660, 1, 1),
                    medium='oil on canvas',
                    height=45.5,
                    width=41,
                    colors='#7E6E50,#E3E0CB,#B7AD89,#3C4C76,#7587A4,#201D20',
                    image='http://lh3.ggpht.com/XUw3NdeiA0MsT-mygp8NT1oPUd17GB3BK2nSRYvyTAY-N64KwsLO\
                           O5QU3muSDEk2AdMzonIVLgjge581mOobVqsQrA=s0')

    selfportrait = Work(title='Self Portrait',
                        date=date(1887, 1, 1),
                        medium='painting',
                        height=42,
                        width=34,
                        colors='#52686D,#50524C,#9CA097,#936D59,#C2C1B8,#6A84A2,#2F3031',
                        image='http://lh4.ggpht.com/RKAJ3z2mOcw83Ju0a7NIp71oUoJbVWJQzxwki5PSERissvWI\
                               rELCuxxGZ12U0PeAnf6WLkRCzpFdvjweUBjlcr2I4dl_=s0')

    nightwatch = Work(title='Nightwatch',
                      date=date(1642, 1, 1),
                      medium='oil on canvas',
                      height=379.5,
                      width=453.5,
                      colors='#261808,#5E3C14,#9C8238,#885617,#AF9F6B,#6C6238,#D7CB9E',
                      image='http://lh6.ggpht.com/ZYWwML8mVFonXzbmg2rQBulNuCSr3rAaf5ppNcUc2Id8qXqudD\
                             L1NSYxaqjEXyDLSbeNFzOHRu0H7rbIws0Js4d7s_M=s0')

    # Artists
    vanGogh = Artist(name='Vincent van Gogh',
                     dob=date(1606, 7, 15),
                     dod=date(1669, 10, 8),
                     nationality='Noord-Nederlands',
                     country='Netherlands')

    rembrandt = Artist(name='Rembrandt Harmensz. van Rijn',
                       dob=date(1853, 3, 30),
                       dod=date(1890, 7, 29),
                       nationality='Noord-Nederlands',
                       country='Dutch Republic')

    vermeer = Artist(name='Johannes Vermeer',
                     dob=date(1632, 10, 31),
                     dod=date(1675, 12, 15),
                     nationality='Noord-Nederlands',
                     country='Dutch Republic')

    # Relationships between artists and works (not accurate information yet!)
    vanGogh.works.append(milkmaid)
    rembrandt.works.append(selfportrait)
    vermeer.works.append(nightwatch)

    # Styles
    baroque = Style(name='Baroque',
                    colors='#261808,#5E3C14,#9C8238,#885617,#AF9F6B,#6C6238,#D7CB9E',
                    averageAge=312,
                    avgHeight=359.5,
                    avgWidth=253.5,
                    images='"http://lh6.ggpht.com/ZYWwML8mVFonXzbmg2rQBulNuCSr3rAaf5ppNcUc2Id8qXqudD\
                             L1NSYxaqjEXyDLSbeNFzOHRu0H7rbIws0Js4d7s_M=s0",\
                            "http://lh3.ggpht.com/XUw3NdeiA0MsT-mygp8NT1oPUd17GB3BK2nSRYvyTAY-N64Kws\
                             LOO5QU3muSDEk2AdMzonIVLgjge581mOobVqsQrA=s0"')

    impressionism = Style(name='Impressionism',
                          colors='#52686D,#50524C,#9CA097,#936D59,#C2C1B8,#6A84A2,#2F3031',
                          averageAge=112,
                          avgHeight=55.5,
                          avgWidth=30.5,
                          images='"http://lh4.ggpht.com/RKAJ3z2mOcw83Ju0a7NIp71oUoJbVWJQzxwki5PSERis\
                                   svWIrELCuxxGZ12U0PeAnf6WLkRCzpFdvjweUBjlcr2I4dl_=s0"')

    rococo = Style(name='Rococo',
                   colors='#CFC1A7,#B8AA91,#9E9078,#564D40,#796C59,#3B3732',
                   averageAge=140,
                   avgHeight=20,
                   avgWidth=14,
                   images='"http://lh5.ggpht.com/ohkR0_wbALcKpvNjORXyrhQj5Qb-6XnZcp29yKXR5oBU2UPb72u\
                            QyzWokxJ_R-ETxnFeYB339314O50we0QK5dNtwQ=s0"')

    # Relationships between styles and artists (not accurate information yet!)
    baroque.artists.append(rembrandt)
    impressionism.artists.append(vanGogh)
    rococo.artists.append(vermeer)

    # Eras
    seventeenth = Era(name='17th',
                      type='century',
                      countries='Dutch Republic,Italy',
                      media='oil on canvas, painting')

    # Relationships between eras and artists (not accurate information yet!)
    seventeenth.artists.append(rembrandt)
    seventeenth.artists.append(vanGogh)
    seventeenth.artists.append(vermeer)

    # Relationships between works and artists (not accurate information yet!)
    seventeenth.works.append(milkmaid)
    seventeenth.works.append(selfportrait)
    seventeenth.works.append(nightwatch)

    # Relationships between styles and artists (not accurate information yet!)
    seventeenth.styles.append(baroque)
    seventeenth.styles.append(impressionism)
    seventeenth.styles.append(rococo)

    eighteenth = Era(name='18th',
                     type='century',
                     countries='Netherlands,Japan',
                     media='')

    # Relationships between artists and artists (not accurate information yet!)
    eighteenth.artists.append(rembrandt)
    eighteenth.artists.append(vanGogh)
    eighteenth.artists.append(vermeer)

    # Relationships between works and artists (not accurate information yet!)
    eighteenth.works.append(milkmaid)
    eighteenth.works.append(selfportrait)
    eighteenth.works.append(nightwatch)

    # Relationships between styles and artists (not accurate information yet!)
    eighteenth.styles.append(baroque)
    eighteenth.styles.append(impressionism)
    eighteenth.styles.append(rococo)

    nineteenth = Era(name='19th',
                     type='century',
                     countries='',
                     media='')

    # Relationships between artists and artists (not accurate information yet!)
    nineteenth.artists.append(rembrandt)
    nineteenth.artists.append(vanGogh)
    nineteenth.artists.append(vermeer)

    # Relationships between works and artists (not accurate information yet!)
    nineteenth.works.append(milkmaid)
    nineteenth.works.append(selfportrait)
    nineteenth.works.append(nightwatch)

    # Relationships between styles and artists (not accurate information yet!)
    nineteenth.styles.append(baroque)
    nineteenth.styles.append(impressionism)
    nineteenth.styles.append(rococo)

    artists = (vanGogh, rembrandt, vermeer)
    eras = (seventeenth, eighteenth, nineteenth)
    works = (milkmaid, selfportrait, nightwatch)
    styles = (baroque, impressionism, rococo)

    return artists + eras + works + styles


def addInstances(db=None, instances=None):
    """
    Adds :class:`Model` instances to a database and commits them.
    If ``db`` is ``None``, the database from ``idb`` will be used.
    If ``instances`` is ``None``, a default set of instances will be generated with ``get_default_model_instances``.

    :param db: The database to which the instances will be added.
    :param instances: A container of :class:`Model` instances.
    """

    if db is None:
        from idb import db

    if instances is None:
        instances = get_default_model_instances()

    for instance in instances:
        db.session.add(instance)
    db.session.commit()
