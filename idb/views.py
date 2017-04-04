# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from flask import render_template
from idb import app
from idb.models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/artists')
def artists():
    artists = Artist.query.all()
    return render_template('artists.html', artists=artists)

@app.route('/works')
def works():
    works = Work.query.all()
    return render_template('works.html', works=works)

@app.route('/eras')
def eras():
    eras = Era.query.all()
    images = [era.works[0].image for era in eras]
    return render_template('eras.html', eras=eras, images=images)

@app.route('/media')
def media():
    media = Medium.query.all()
    images = [medium.images[0] for medium in media]
    return render_template('media.html', media=media, images=images)


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
    return render_template('artist_instance.html', artist=artist, works=works, media=media)

@app.route('/work/<int:id>')
def work(id):
    work = Work.query.filter_by(id=id).first()
    if work.colors:
        colors = work.colors.replace("[","").replace("]","").replace("'","").split(",")
    else:
        colors = None
    artists = []
    for i in range(5):
        artists.append(work.artists[i])
    len_dict = {}
    if colors:
        len_dict['colors'] = len(colors)
    else:
        len_dict['colors'] = 1
    len_dict['media'] = len(work.media)
    return render_template('work_instance.html', work=work, artists=artists,colors=colors,lendict=len_dict)

@app.route('/eras/<int:id>')
def era(id):
    era = Era.query.filter_by(id=id).first()
    return render_template('era_instance.html',era=era)

@app.route('/report_text')
def report_text():
	return render_template('report_text.html')
