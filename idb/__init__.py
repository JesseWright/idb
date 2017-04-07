from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from idb.database_tools import build_db_connection_uri_string

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = False

# Setup DB from environment variables or defaults
app.config['SQLALCHEMY_DATABASE_URI'] = build_db_connection_uri_string(
    table='postgres'
          '?unix_socket=/cloudsql/'
          'cs373-project-345:us-central1:idb-artistree',
    address='localhost')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Setup routes for Flask
import idb.views
import idb.queries
