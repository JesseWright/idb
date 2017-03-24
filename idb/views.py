# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

from flask import render_template
from idb import app

@app.route('/')
def index():
    return render_template('index.html')
