# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from flask import render_template
from idb import app
from idb.models import *

from subprocess import call


@app.route('api/artists/all')
def artist_all():
    artists = Artist.query.all()
    response(200, artist, 1)

@app.route('api/artists/<int:id>')
def artist_one(id):
    artist = Artist.query.filter_by(id=id).first()
    return response(200, artist, 1)

@app.route('api/works/all')
def work_all():
    works = Work.query.all()
    response(200, work, 1)

@app.route('api/works/<int:id>')
def work_one(id):
    work = Work.query.filter_by(id=id).first()
    return response(200, work, 1)

@app.route('api/media/all')
def work_all():
    works = Medium.query.all()
    response(200, work, 1)

@app.route('api/media/<int:id>')
def work_one(id):
    work = Medium.query.filter_by(id=id).first()
    return response(200, work, 1)

@app.route('api/eras/all')
def era_all():
    eras = Era.query.all()
    response(200, era, 1)

@app.route('api/eras/<int:id>')
def era_one(id):
    era = Era.query.filter_by(id=id).first()
    return response(200, era, 1)
