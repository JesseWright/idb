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
    return render_template('artist_instance.html', artist=artist)

@app.route('/work/<int:id>')
def work(id):
    work = Work.query.filter_by(id=id).first()
    colors = work.colors.replace("[","").replace("]","").replace("'","").split(",")
    artists = []
    for i in range(5):
        artists.append(work.artists[i])
    len_dict = {}
    len_dict['colors'] = len(colors)
    len_dict['media'] = len(work.media)
    return render_template('work_instance.html', work=work, artists=artists,colors=colors,lendict=len_dict)

@app.route('/eras/<int:id>')
def era(id):
    era = Era.query.filter_by(id=id).first()
    return render_template('era_instance.html',era=era)

@app.route('/report_text')
def report_text():
	return render_template('report_text.html')
