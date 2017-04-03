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

@app.route('/report_text')
def report_text():
	return render_template('report_text.html')
