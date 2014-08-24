# test.py
import os 
import unittest
from views import app, db 
from models import Item 
from config import basedir

TEST_DB = 'test.db'

class Users(unittest.TestCase):
# this is a special method that is executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True 
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB) 
        self.app = app.test_client() 
        db.create_all()

    # this is a special method that is executed after each test
    def tearDown(self): 
        db.drop_all()

    # each test should start with 'test'
    def test_item_setup(self):
        import datetime
        new_item = Item("name field", "info field",
        datetime.datetime.utcnow()) 
        db.session.add(new_item) 
        db.session.commit() # post the example item
        items = db.session.query(Item).all() 
        for item in items:
            item.name
        assert item.name == "name field" # make sure it matches


if __name__ == "__main__": 
    unittest.main()

