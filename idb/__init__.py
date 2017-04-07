from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from idb.database_tools import build_db_connection_uri_string

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True

# Setup DB from environment variables or defaults

app.config['SQLALCHEMY_DATABASE_URI'] = build_db_connection_uri_string()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    build_db_connection_uri_string(address='',
                                   use_env_vars=True,
                                   use_defaults=True)

print('DB URI used: ' + str(app.config['SQLALCHEMY_DATABASE_URI']))

db = SQLAlchemy(app)

# Setup routes for Flask
import idb.views
import idb.queries
