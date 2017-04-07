import os

_db_driver_default = 'psycopg2'
_db_uname_default = 'postgres'
_db_pwrd_default = ''
_db_addr_default = 'localhost:5432'
_db_table_default = 'postgres'


def build_db_connection_uri_string(driver=None, username=None,
                                   password=None, address=None,
                                   table=None, use_env_vars=True,
                                   use_defaults=True):
    """ Generates a URI to the database according to the parameters given, 
    using environment variables for any parameters given as None if 
    use_env_vars is True. If use_defaults is True, parameters that are 
    supplied as None and do not have an environment variable set will be 
    given a default value.
    
    Any parameter that is None when the URI is being constructed will
    be represented by an ampty string.
    
    Suggested env. var. values for local testing with Cloud SQL proxy:
        - SWE_IDB_PGDB_PW:    <password for DB>
        - SWE_IDB_PGDB_ADDR:  'localhost:3306'
    """
    db_driver = driver
    db_username = username
    db_password = password
    db_address = address
    db_table = table

    if use_env_vars:
        db_driver = db_driver or os.environ.get('SWE_IDB_GPDB_DRVR')
        db_username = db_username or os.environ.get('SWE_IDB_PGDB_UN')
        db_password = db_password or os.environ.get('SWE_IDB_PGDB_PW')
        db_address = db_address or os.environ.get('SWE_IDB_PGDB_ADDR')
        db_table = db_table or os.environ.get('SQE_IDB_PGDB_TABLE')

    if use_defaults:
        db_driver = db_driver or _db_driver_default
        db_username = db_username or _db_uname_default
        db_password = db_password or _db_pwrd_default
        db_address = db_address or _db_addr_default
        db_table = db_table or _db_table_default

    db_driver = db_driver or ''
    db_username = db_username or ''
    db_password = db_password or ''
    db_address = db_address or ''
    db_table = db_table or ''

    _db_uri_format_str = 'postgresql+%s://%s:%s@%s/%s'
    return (_db_uri_format_str % (db_driver,
                                  db_username,
                                  db_password,
                                  db_address,
                                  db_table))
