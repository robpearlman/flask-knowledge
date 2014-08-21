import os 
import unittest

from config import  basedir
from models import ItemTable 
from views import app, db

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    # executed after to each test
    def tearDown(self):
        db.drop_all()

    ###############
    #### tests ####
    ###############

	# each test should start with 'test'
	def test_can_add_item(self): 
		new_item = ItemTable("An item", "A bunch of details about the item")
		db.session.add(new_item)
		db.item.commit()
		test = db.session.query(ItemTable).all()
		for t in test:
			t.name
		assert t.name == "An item"


if __name__ == '__main__': 
	unittest.main()