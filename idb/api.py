from flask import render_template
from idb import app
from idb.models import *
from idb.queries import *

from subprocess import call


@app.route('/api/artists/all')
def artist_all():
    artists = Artist.query.all()
    return response(200, [artist.serialize() for artist in artists], 1)


@app.route('/api/artists/<int:id>')
def artist_one(id):
    artist = Artist.query.filter_by(id=id).first()
    return response(200, artist.serialize(), 1)


@app.route('/api/works/all')
def work_all():
    works = Work.query.all()
    return response(200, [work.serialize() for work in works], 1)


@app.route('/api/works/<int:id>')
def work_one(id):
    work = Work.query.filter_by(id=id).first()
    return response(200, work.serialize(), 1)


@app.route('/api/media/all')
def media_all():
    media = Medium.query.all()
    return response(200, [medium.serialize() for medium in media], 1)


@app.route('/api/media/<int:id>')
def media_one(id):
    medium = Medium.query.filter_by(id=id).first()
    return response(200, medium.serialize(), 1)


@app.route('/api/eras/all')
def era_all():
    eras = Era.query.all()
    return response(200, [era.serialize() for era in eras], 1)


@app.route('/api/eras/<int:id>')
def era_one(id):
    era = Era.query.filter_by(id=id).first()
    return response(200, era.serialize(), 1)
