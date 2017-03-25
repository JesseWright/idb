# pylint: disable = bad-whitespace
# pylint: disable = missing-docstring

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/phase1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Setup routes for Flask
import idb.views

# Setup models for SQLAlchemy
# import idb.models
# TODO: Resolve circular imports and dependencies (namely idb and mdoels)