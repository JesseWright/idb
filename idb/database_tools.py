import os

# Define environment variables' keys used
db_envvar_key_prefix = 'SWE_IDB_PGDB_'
db_driver_evkey = db_envvar_key_prefix + 'DRVR'
db_username_evkey = db_envvar_key_prefix + 'UN'
db_password_evkey = db_envvar_key_prefix + 'PW'
db_address_evkey = db_envvar_key_prefix + 'ADDR'
db_name_evkey = db_envvar_key_prefix + 'NAME'
db_options_evkey = db_envvar_key_prefix + 'OPTS'

# Define internal defaults
_db_driver_default = 'psycopg2'
_db_uname_default = 'postgres'
_db_pwrd_default = ''
_db_addr_default = 'localhost:3306'
_db_name_default = 'postgres'
_db_opts_default = ''


def build_db_connection_uri_string(driver=None, username=None,
                                   password=None, address=None,
                                   name=None, options=None,
                                   use_env_vars=False, use_defaults=False):
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
    
    Do not commit passwords to source control!
    
    Return string in the form of 
        'postgresql+{driver}://
            {username}:{password}@{address}/{name}{/options}'.
    """
    db_driver = driver
    db_username = username
    db_password = password
    db_address = address
    db_name = name
    db_options = options

    if use_env_vars:
        # Overwrite any None-types with environment variables
        if db_driver is None: db_driver = os.environ.get(db_driver_evkey)
        if db_username is None: db_username = os.environ.get(db_username_evkey)
        if db_password is None: db_password = os.environ.get(db_password_evkey)
        if db_address is None: db_address = os.environ.get(db_address_evkey)
        if db_name is None: db_name = os.environ.get(db_name_evkey)
        if db_options is None: db_options = \
            os.environ.get(db_options_evkey)

    if use_defaults:
        # Overwrite any None-types with defaults
        if db_driver is None: db_driver = _db_driver_default
        if db_username is None: db_username = _db_uname_default
        if db_password is None: db_password = _db_pwrd_default
        if db_address is None: db_address = _db_addr_default
        if db_name is None: db_name = _db_name_default
        if db_options is None: db_options = \
            _db_opts_default

    # Convert any None types to empty strings
    if db_driver is None: db_driver = ''
    if db_username is None: db_username = ''
    if db_password is None: db_password = ''
    if db_address is None: db_address = ''
    if db_name is None: db_name = ''
    if db_options is None: db_options = ''

    return ('postgresql+%s://%s:%s@%s/%s%s'
            % (db_driver,
               db_username,
               db_password,
               db_address,
               db_name,
               db_options))
