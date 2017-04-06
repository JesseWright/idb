import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = False

# Set up DB from environment variables
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

_db_driver = os.environ.get('SWE_IDB_GPDB_DRVR') or 'psycopg2'
_db_username = os.environ.get('SWE_IDB_PGDB_UN') or 'postgres'
_db_password = os.environ.get('SWE_IDB_PGDB_PW') or ''
_db_address = os.environ.get('SWE_IDB_PGDB_ADDR') or 'localhost:5432'
_db_table = os.environ.get('SQE_IDB_PGDB_TABLE') or 'postgres'

# Suggested env. var. values for local testing with Cloud SQL proxy:
#   SWE_IDB_PGDB_PW:    <password for DB>
#   SWE_IDB_PGDB_ADDR:  'localhost:3306'

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql+%s://%s:%s@%s/%s'
                                         % (_db_driver,
                                            _db_username,
                                            _db_password,
                                            _db_address,
                                            _db_table))

db = SQLAlchemy(app)

# Setup routes for Flask
import idb.views
import idb.queries
