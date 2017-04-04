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

@app.route('/media/<int:id>')
def medium(id):
    medium = Medium.query.filter_by(id=id).first()
    if medium.images:
        images = medium.images.replace("[","").replace("]","").replace("'","").split(",")
    else:
        images = None
    return render_template('medium_instance.html',medium=medium,images = images)

@app.route('/report_text')
def report_text():
	return render_template('report_text.html')
