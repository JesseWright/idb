from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from idb.database_tools import build_db_connection_uri_string

app = Flask(__name__)
app.config['TESTING'] = False
app.config['DEBUG'] = True

# Setup DB from environment variables or defaults
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    build_db_connection_uri_string(use_env_vars=True,
                                   use_defaults=True)

import os
print('URI: ' + (app.config['SQLALCHEMY_DATABASE_URI'] or 'NONE'))
print('EV OPTS: ' + (os.environ.get('SWE_IDB_PGDB_OPTS') or 'NONE'))
print('EV ADDR: ' + (os.environ.get('SWE_IDB_PGDB_ADDR') or 'NONE'))
print('EV PW: ' + (os.environ.get('SWE_IDB_PGDB_PW') or 'NONE'))

db = SQLAlchemy(app)
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
