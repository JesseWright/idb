import os

_db_driver_default = 'psycopg2'
_db_uname_default = 'postgres'
_db_pwrd_default = 'uB6b5eFnexydPnm1'
_db_addr_default = 'localhost:3306'
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
        if db_driver is None: db_driver = os.environ.get('SWE_IDB_GPDB_DRVR')
        if db_username is None: db_username = os.environ.get('SWE_IDB_PGDB_UN')
        if db_password is None: db_password = os.environ.get('SWE_IDB_PGDB_PW')
        if db_address is None: db_address = os.environ.get('SWE_IDB_PGDB_ADDR')
        if db_table is None: db_table = os.environ.get('SQE_IDB_PGDB_TABLE')

    if use_defaults:
        if db_driver is None: db_driver = _db_driver_default
        if db_username is None: db_username = _db_uname_default
        if db_password is None: db_password = _db_pwrd_default
        if db_address is None: db_address = _db_addr_default
        if db_table is None: db_table = _db_table_default

    if db_driver is None: db_driver = ''
    if db_username is None: db_username = ''
    if db_password is None: db_password = ''
    if db_address is None: db_address = ''
    if db_table is None: db_table = ''

    return ('postgresql+%s://%s:%s@%s/%s'
            % (db_driver,
               db_username,
               db_password,
               db_address,
               db_table))
