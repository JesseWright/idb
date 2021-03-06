from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from idb.database_tools import build_db_connection_uri_string
import os

app = Flask(__name__)
CORS(app)
app.config['TESTING'] = False
app.config['DEBUG'] = True

# Setup DB from environment variables or defaults
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    build_db_connection_uri_string(use_env_vars=True,
                                   use_defaults=True)

print('URI: ' + (app.config['SQLALCHEMY_DATABASE_URI'] or 'NONE'))
print('EV OPTS: ' + (os.environ.get('SWE_IDB_PGDB_OPTS') or 'NONE'))
print('EV ADDR: ' + (os.environ.get('SWE_IDB_PGDB_ADDR') or 'NONE'))
print('EV PW: ' + (os.environ.get('SWE_IDB_PGDB_PW') or 'NONE'))

db = SQLAlchemy(app)
db_query_count = 0

#### Jinja2 templating functions ###
def getYear(date, justYear = False):
    if(date != None):
        if(justYear):
            return date.year

        else:
            return date.strftime("%b %d, %Y")
    else:
        return "Year Unknown"
def strNumFormatter(num):
    if(num != None):
        return '%0.2f' % float(num)
    else:
        return "Unavailable"

app.jinja_env.globals.update(getYear=getYear)
app.jinja_env.globals.update(strNumFormatter=strNumFormatter)
# Setup routes for Flask
import idb.views
import idb.queries
import idb.api
