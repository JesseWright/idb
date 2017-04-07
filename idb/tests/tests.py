import os
import unittest
import datetime
from idb import app, db
import idb.models as models
from idb.database_tools import build_db_connection_uri_string

_test_string = 'test'

_db_username_test = os.environ.get('SWE_IDB_PGDB_UN_TEST')
_db_password_test = os.environ.get('SWE_IDB_PGDB_PW_TEST')

# !-- These variables below should NEVER connect to the production DB --! #
# !-----    If they do, they could drop all of its tables!         -----! #
_db_address_test = os.environ.get('SWE_IDB_PGDB_ADDR_TEST')
_db_table_test = os.environ.get('SQE_IDB_PGDB_TABLE_TEST')


class TestApp(unittest.TestCase):
    """" A base ``TestCase`` class to handle setup and tear down
    of app tests. """
    future_date = datetime.datetime.now() + datetime.timedelta(days=2)

    def setUp(self):
        """ Set up and configures the application
        as a test client and create an empty testing database. """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            build_db_connection_uri_string(username=_db_username_test,
                                           password=_db_username_test,
                                           address=_db_address_test,
                                           name=_db_table_test,
                                           use_env_vars=False)

        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """ Reset the testing database. """
        db.drop_all()


class TestArtistModel(TestApp):
    """ A test suite to verify ``Artist`` models. """

    def test_null_name(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=None)

    def test_empty_name(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name='')

    def test_assign_name_null(self):
        models.Artist(name=_test_string)
        with self.assertRaises(Exception):
            models.Artist.name = ''

    def test_update_name_null(self):
        test_artist = models.Artist(name=_test_string)
        db.session.add(test_artist)
        db.session.commit()
        with self.assertRaises(Exception):
            models.Artist.query.get(test_artist.id).update(dict(name=''))

    def test_future_dob(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=_test_string,
                          dob=self.future_date)

    def test_future_dod(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=_test_string,
                          dod=self.future_date)


class TestWorkModel(TestApp):
    """ A test suite to verify ``Work`` models """

    def test_null_title(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=None)

    def test_empty_title(self):
        self.assertRaises(Exception,
                          models.Work,
                          title='')

    def test_assign_title_null(self):
        models.Work(title=_test_string)
        with self.assertRaises(Exception):
            models.Work.title = ''

    def test_update_title_null(self):
        test_work = models.Work(title=_test_string)
        db.session.add(test_work)
        db.session.commit()
        with self.assertRaises(Exception):
            models.Artist.query.get(test_work.id).update(dict(title=''))

    def test_future_date(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=_test_string,
                          date=self.future_date)

    def test_zero_height(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=_test_string,
                          height=0)

    def test_negative_height(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=_test_string,
                          height=-1)

    def test_zero_width(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=_test_string,
                          width=0)

    def test_negative_width(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=_test_string,
                          width=-1)


# TODO: Fix issue with validation of name attributes on Model creation
# TODO: Test for expected successes as well
# TODO: Finish tests for remaining two models

if __name__ == '__main__':
    unittest.main()
