from idb.models import Work, Artist, Medium, Era
from datetime import date, timedelta
import datetime
import random
import uuid

random.seed(datetime.datetime.now().microsecond)

_ultra_low_prob = 0.03
_very_low_prob = 0.1
_low_prob = 0.2
_mid_prob = 0.4
_high_prob = 0.8

_empty_options = [None, '']
_empty_list_options = _empty_options + ['[]']

_motif_selection = ['fish', 'boy', 'woman', 'dog', 'food', 'sun', 'sky',
                    'tree', 'people', 'umbrella']

_media_selection = ['oil on canvas', 'marble', 'watercolor on parchment',
                    'stone', 'wood', 'spray paint', 'painting']

_image_selection = ['http://lh3.ggpht.com/XUw3NdeiA0MsT-mygp8NT1oPUd17GB3BK'
                    '2nSRYvyTAY-N64KwsLOO5QU3muSDEk2AdMzonIVLgjge581mOobVqs'
                    'QrA=s0',
                    'http://lh4.ggpht.com/RKAJ3z2mOcw83Ju0a7NIp71oUoJbVWJQz'
                    'xwki5PSERissvWIrELCuxxGZ12U0PeAnf6WLkRCzpFdvjweUBjlcr2'
                    'I4dl_=s0',
                    'http://lh6.ggpht.com/ZYWwML8mVFonXzbmg2rQBulNuCSr3rAaf'
                    '5ppNcUc2Id8qXqudDL1NSYxaqjEXyDLSbeNFzOHRu0H7rbIws0Js4d'
                    '7s_M=s0',
                    'http://lh6.ggpht.com/ZYWwML8mVFonXzbmg2rQBulNuCSr3rAaf'
                    '5ppNcUc2Id8qXqudDL1NSYxaqjEXyDLSbeNFzOHRu0H7rbIws0Js4d'
                    '7s_M = s0']

_nationality_selection = ['Noord-Nederlands', 'American', 'German',
                          'Chinese', 'Brazilian', 'South African',
                          'Nigeria', 'British']

_country_selection = ['United States', 'Germany', 'China', 'Netherlands',
                      'Brazil', 'South Africa', 'Nigeria', 'Great Britain']

_era_type_selection = ['century', 'period', 'era', 'dynasty', 'movement',
                       'age']

_text_selection = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur',
                   'adipiscing', 'elit.', 'Etiam', 'tempor', 'fringilla',
                   'molestie.', 'Proin', 'condimentum', 'tristique', 'dictum.',
                   'Phasellus', 'luctus', 'consectetur', 'neque.', 'Etiam',
                   'nisi', 'augue,', 'convallis', 'vel', 'lacus', 'a,',
                   'mattis', 'dapibus', 'felis.', 'Curabitur', 'a', 'libero',
                   'a', 'turpis', 'porta', 'eleifend', 'vel', 'quis',
                   'mauris.', 'Sed', 'id', 'arcu', 'a', 'justo', 'ornare',
                   'sagittis', 'a', 'at', 'est.', 'Nullam', 'nec', 'eros',
                   'commodo,', 'interdum', 'elit', 'bibendum,', 'euismod',
                   'massa.', 'Donec', 'non', 'condimentum', 'orci,', 'egestas',
                   'tempor', 'leo.', 'Ut', 'consectetur', 'interdum', 'leo,',
                   'eu', 'fermentum', 'magna', 'commodo', 'non.',
                   'Pellentesque', 'eget', 'dolor', 'dui.', 'Pellentesque',
                   'habitant', 'morbi', 'tristique', 'senectus', 'et', 'netus',
                   'et', 'malesuada', 'fames', 'ac', 'turpis', 'egestas.',
                   'Quisque', 'et', 'nisl', 'neque.', 'Nullam', 'elit', 'sem,',
                   'consequat.']


def generate_random_date():
    return date(year=int(round(random.uniform(1000, 1930))),
                month=int(round(random.uniform(1, 12))),
                day=int(round(random.uniform(1, 28))))


def generate_random_color():
    color = "#"
    for i in range(0, 3):
        color += format(int(round(random.uniform(0, 255))), '02x')
    return color


def generate_random_colors(n):
    return [generate_random_color() for _ in range(1, n)]


def generate_random_work():
    motif_sample_k = int(random.uniform(0, len(_motif_selection)))

    title = 'test_work_' + str(uuid.uuid4())
    work_date = generate_random_date() \
        if random.random() >= _low_prob else None

    height = random.uniform(1, 250) if random.random() >= _low_prob else None
    width = random.uniform(1, 250) if random.random() >= _low_prob else None
    depth = random.uniform(1, 250) if random.random() >= _low_prob else None

    motifs = str(random.sample(_motif_selection, motif_sample_k)) \
        if (random.random() >= _low_prob) \
        else (None if random.random() > _mid_prob else '[]')

    colors = str(generate_random_colors(int(random.uniform(0, 10)))) \
        if random.random() >= _low_prob else random.choice(_empty_list_options)

    image = random.choice(_image_selection) \
        if random.random() >= _low_prob else random.choice(_empty_options)

    return Work(title=title,
                date=work_date,
                height=height,
                width=width,
                depth=depth,
                motifs=motifs,
                colors=colors,
                image=image)


def generate_random_artist():
    name = 'test_artist_' + str(uuid.uuid4())
    dob = generate_random_date() if random.random() >= _low_prob else None
    dod = ((dob + timedelta(days=random.uniform(5000, 365 * 80)))
           if random.random() >= _low_prob else None) if dob \
        else (generate_random_date() if random.random() >= _low_prob
              else None)

    image = str(random.choice(_image_selection)) \
        if random.random() >= _low_prob else random.choice(_empty_options)

    bio = " ".join(random.sample(_text_selection,
                                 int(random.uniform(10, 100)))) \
        if random.random() >= _mid_prob else random.choice(_empty_options)

    if bio and len(bio) > 250:
        bio = bio[0:250]

    nationality = random.choice(_nationality_selection) \
        if random.random() > _very_low_prob else random.choice(_empty_options)

    country = random.choice(_country_selection) \
        if random.random() > _low_prob else random.choice(_empty_options)

    return Artist(name=name,
                  dob=dob,
                  dod=dod,
                  image=image,
                  bio=bio,
                  nationality=nationality,
                  country=country)


def generate_random_era(name=None):
    countries_sample_k = int(random.uniform(0, len(_country_selection)))
    era_name = (name if name else 'test_era') + '_' + str(uuid.uuid4())
    era_type = random.choice(_era_type_selection)
    countries = str(random.sample(_country_selection, countries_sample_k)) \
        if random.random() > _low_prob else random.choice(_empty_options)

    return Era(name=era_name,
               type=era_type,
               countries=countries)


def generate_random_medium(name=None):
    images_sample_k = int(random.uniform(0, len(_image_selection)))

    medium_name = name if name else ('test_medium_' + str(uuid.uuid4()))
    average_age = random.uniform(1, 1000)

    avg_height = random.uniform(1, 250) \
        if random.random() >= _low_prob else None
    avg_width = random.uniform(1, 250) \
        if random.random() >= _low_prob else None
    avg_depth = random.uniform(1, 250) \
        if random.random() >= _low_prob else None

    colors = str(generate_random_colors(int(random.uniform(0, 10)))) \
        if random.random() >= _low_prob else random.choice(_empty_list_options)
    images = str(random.sample(_image_selection, images_sample_k)) \
        if random.random() >= _low_prob else random.choice(_empty_list_options)

    return Medium(name=medium_name,
                  colors=colors,
                  average_age=average_age,
                  avg_height=avg_height,
                  avg_width=avg_width,
                  avg_depth=avg_depth,
                  images=images)



def get_random_model_instances(count=1000, spread=0.3):
    """ Generate a container of test instances of :class:`Model`s
    defined in models.py.

    This method is only meant for testing purposes or to initialize a
    database for the first time.

    Return an iterable container of Model instances.

    """

    if not count: return []

    count = int(count)
    assert count > 0, \
        "Count must be a positive integer."
    assert 0.0 <= spread <= 1, \
        "Spread must be non-negative and less than 1."

    ####################################
    # Generate instances of each Model #
    ####################################

    works = []
    fuzz = int(round(spread * count))
    for _ in range(0, count + int(random.uniform(-fuzz, fuzz))):
        works.append(generate_random_work())

    artists = []
    count = int(count / 2)
    fuzz = int(round(spread * count))
    for _ in range(0, count + int(random.uniform(-fuzz, fuzz))):
        artists.append(generate_random_artist())

    media = []
    for medium in _media_selection:
        media.append(generate_random_medium(medium))

    eras = []
    count = 3
    fuzz = 2
    for era in _era_type_selection:
        for _ in range(0, count + int(random.uniform(-fuzz, fuzz))):
            eras.append(generate_random_era(era))

    #################################################
    # Relationships between instances of each Model #
    #################################################

    for artist in artists:
        for work in works:
            if random.random() <= _ultra_low_prob:
                artist.works.append(work)

    for work in works:
        for medium in media:
            work.media.append(medium)

    for medium in media:
        for artist in artists:
            if random.random() <= _ultra_low_prob:
                medium.artists.append(artist)

    for era in eras:
        for artist in artists:
            if random.random() <= _ultra_low_prob:
                era.artists.append(artist)
        for work in works:
            if random.random() <= _ultra_low_prob:
                era.works.append(work)
        for medium in media:
            if random.random() <= _ultra_low_prob:
                era.media.append(medium)

    return artists + eras + works + media


def add_instances(db=None, instances=None):
    """ Add :class:`Model` instances to a database and commits them.

    If ``db`` is ``None``, the database from ``idb`` will be used.
    If ``instances`` is ``None``, a default set of instances will be
    generated with ``get_default_model_instances``.

    :param db: The database to which the instances will be added.
    :param instances: A container of :class:`Model` instances.
    """

    if db is None:
        from idb import db

    if instances is None:
        instances = get_random_model_instances()

    for instance in instances:
        db.session.add(instance)
    db.session.commit()
