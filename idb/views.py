from flask import render_template
from idb import app
from idb.models import *
from idb.queries import *
import subprocess


@app.route('/')
def index():
    """Default route that renders the homepage using
    the template 'index.html'
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """Route to render our about page."""
    return render_template('about.html')


@app.route('/report')
def report():
    """Route to render the report page, although the actual report HTML
    is in 'report_text.html' and is rendered in an iFrame.
    """
    return render_template('report.html')


@app.route('/artists')
def artists():
    artists = Artist.query.all()
    first_page = artists[0:16]
    return render_template('artists.html', artists=first_page)


@app.route('/works')
def works():
    works = Work.query.all()
    first_page = works[0:16]
    return render_template('works.html', works=first_page)


@app.route('/eras')
def eras():
    images = []
    eras = Era.query.all()
    for era in eras:
        if era.works:
            images.append(era.works[0])
        else:
            images.append(None)
            # images = [if era.works: era.works[0].image for era in eras]
    return render_template('eras.html', eras=eras, images=images)


@app.route('/media')
def media():
    media = Medium.query.all()
    first_page = media[0:16]
    return render_template('media.html', media=first_page)


@app.route('/artist/<int:id>')
def artist(id):
    artist = Artist.query.filter_by(id=id).first()

    works = []
    media = []
    for i in range(len(artist.works)):
        if i > 5:
            break
        works.append(artist.works[i])
    for j in range(len(artist.media)):
        if j > 5:
            break
        media.append(artist.media[j])

    return render_template('artist_instance.html', artist=artist, works=works,
                           media=media)


@app.route('/work/<int:id>')
def work(id):
    work = Work.query.filter_by(id=id).first()
    if work.colors:
        colors = work.colors.replace("{", "") \
            .replace("}", "").replace("'", "").split(",")
    else:
        colors = None
    artists = []
    for i in range(min(5, len(work.artists))):
        artists.append(work.artists[i])
    len_dict = {}
    if colors:
        len_dict['colors'] = len(colors)
    else:
        len_dict['colors'] = 1
    len_dict['media'] = len(work.media)
    if work.image:
        work._image = work.image.replace("{", "") \
            .replace("}", "").replace("'", "").split(",")[0]
    else:
        work._image = None
    return render_template('work_instance.html', work=work, artists=artists,
                           colors=colors, lendict=len_dict)


@app.route('/eras/<int:id>')
def era(id):
    era = Era.query.filter_by(id=id).first()
    if era.countries:
        countries = era.countries \
            .replace("{", "").replace("}", "").replace("'", "").split(",")
    else:
        countries = None
    works = []
    media = []
    artists = []
    for i in range(len(era.works)):
        if i > 5:
            break
        works.append(era.works[i])
    for j in range(len(era.media)):
        if j > 5:
            break
        media.append(era.media[j])
    for k in range(len(era.artists)):
        if k > 5:
            break
        artists.append(era.artists[k])
    return render_template('era_instance.html', era=era, countries=countries,
                           works=works, media=media, artists=artists)


@app.route('/media/<int:id>')
def medium(id):
    medium = Medium.query.filter_by(id=id).first()
    medium._image = medium.images.replace("{", "") \
        .replace("}", "").replace("'", "")

    if len(medium.colors) > 6:
        colors = medium.colors \
            .replace("{", "").replace("}", "").replace("'", "").split(",")
    else:
        colors = None

    return render_template('medium_instance.html', medium=medium,
                           colors=colors)

@app.route('/search/')
def search():
    args = request.args.to_dict()

def search_json(model, terms):
    for model in models:
        pass


@app.route('/report_text')
def report_text():
    return render_template('report_text.html')


@app.route('/getResults/tests/')
def tests():
    sb = subprocess.check_output(['python', '-m', 'unittest', 'idb.models'],
                                 stderr=subprocess.STDOUT).decode("utf-8")
    print(sb)
    return sb
