import unittest, models, os, datetime
from idb import app, db

test_string = 'test'
test_db = 'test.db'


class TestApp(unittest.TestCase):
    future_date = datetime.datetime.now() + datetime.timedelta(days=2)

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + test_db
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()


class TestArtistModel(TestApp):
    def test_null_name(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=None)

    def test_empty_name(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name='')

    def test_assign_name_null(self):
        models.Artist(name=test_string)
        with self.assertRaises(Exception):
            models.Artist.name = ''

    def test_update_name_null(self):
        test_artist = models.Artist(name=test_string)
        db.session.add(test_artist)
        db.session.commit()
        with self.assertRaises(Exception):
            models.Artist.query.get(test_artist.id).update(dict(name=''))

    def test_future_dob(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=test_string,
                          dob=self.future_date)

    def test_future_dod(self):
        self.assertRaises(Exception,
                          models.Artist,
                          name=test_string,
                          dod=self.future_date)


class TestWorkModel(TestApp):
    def test_null_title(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=None)

    def test_empty_title(self):
        self.assertRaises(Exception,
                          models.Work,
                          title='')

    def test_assign_title_null(self):
        models.Work(title=test_string)
        with self.assertRaises(Exception):
            models.Work.title = ''

    def test_update_title_null(self):
        test_work = models.Work(title=test_string)
        db.session.add(test_work)
        db.session.commit()
        with self.assertRaises(Exception):
            models.Artist.query.get(test_work.id).update(dict(title=''))

    def test_future_date(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=test_string,
                          date=self.future_date)

    def test_zero_height(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=test_string,
                          height=0)

    def test_negative_height(self):
        self.assertRaises(Exception,
                          models.Work,
                          title=test_string,
                          height=-1)

# TODO: Finish tests for remaining two models

if __name__ == '__main__':
    unittest.main()
