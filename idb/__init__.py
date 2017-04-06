import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = False

# Set up DB from environment variables
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

_db_driver = os.environ.get('SWE_IDB_GPDB_DRVR') if not None else 'psycopg2'
_db_username = os.environ.get('SWE_IDB_PGDB_UN') if not None else 'postgres'
_db_password = os.environ.get('SWE_IDB_PGDB_PW') if not None else ''
_db_address = os.environ.get('SWE_IDB_PGDB_ADDR') if not None else ''
_db_table = os.environ.get('SQE_IDB_PGDB_TABLE') if not None else 'postgres'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+%s://%s:%s@/%s/%s' \
    % (_db_driver, _db_username, _db_password, _db_table, _db_address)


db = SQLAlchemy(app)

from idb import views