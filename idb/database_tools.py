import os

_db_driver_default = 'psycopg2'
_db_uname_default = 'postgres'
_db_pwrd_default = ''
_db_addr_default = 'localhost:5432'
_db_name_default = 'postgres'
_db_socket_file_default = '/cloudsql/'
_db_cloudsql_instance_default = 'cs373-project-345:us-central1:idb-artistree'


def build_db_connection_uri_string(driver=None, username=None,
                                   password=None, address=None,
                                   name=None, socket_file=None,
                                   cloudsql_instance=None,
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
    
    Return string in the form of 
        'postgresql+{driver}://
            {username}:{password}@
            {address}/{name}{?host=socket_file}{cloudsql_instance}'.
    """
    db_driver = driver
    db_username = username
    db_password = password
    db_address = address
    db_name = name
    db_socket_file = socket_file
    db_cloudsql_instance = cloudsql_instance

    if use_env_vars:
        # Overwrite any None-types with environment variables
        if db_driver is None: db_driver = os.environ.get('SWE_IDB_GPDB_DRVR')
        if db_username is None: db_username = os.environ.get('SWE_IDB_PGDB_UN')
        if db_password is None: db_password = os.environ.get('SWE_IDB_PGDB_PW')
        if db_address is None: db_address = os.environ.get('SWE_IDB_PGDB_ADDR')
        if db_name is None: db_name = os.environ.get('SWE_IDB_PGDB_NAME')
        if db_socket_file is None: db_socket_file = os.environ.get('SWE_IDB_PGDB_SOCKET')
        if db_cloudsql_instance is None: db_cloudsql_instance = \
            os.environ.get('SWE_IDB_PGDB_CLOUDSQL_INSTANCE')

    if use_defaults:
        # Overwrite any None-types with defaults
        if db_driver is None: db_driver = _db_driver_default
        if db_username is None: db_username = _db_uname_default
        if db_password is None: db_password = _db_pwrd_default
        if db_address is None: db_address = _db_addr_default
        if db_name is None: db_name = _db_name_default
        if db_socket_file is None: db_socket_file = _db_socket_file_default
        if db_cloudsql_instance is None: db_cloudsql_instance = \
            _db_cloudsql_instance_default

    # Convert any None types to empty strings
    if db_driver is None: db_driver = ''
    if db_username is None: db_username = ''
    if db_password is None: db_password = ''
    if db_address is None: db_address = ''
    if db_name is None: db_name = ''
    if db_socket_file is None: db_socket_file = ''
    if db_cloudsql_instance is None: db_cloudsql_instance = ''

    socket_prefix = '?host='
    # Sockets start with a single question mark
    if db_socket_file: # and not db_socket_file.startswith(socket_prefix):
        db_socket_file = socket_prefix + db_socket_file

    return ('postgresql+%s://%s:%s@%s/%s%s%s'
            % (db_driver,
               db_username,
               db_password,
               db_address,
               db_name,
               db_socket_file,
               db_cloudsql_instance))
