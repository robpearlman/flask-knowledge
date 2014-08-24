from views import db
from passlib.apps import custom_app_context as pwd_context

class Item(db.Model):
	import datetime

	"""docstring for ItemTable"""
	__tablename__ = "items"
	item_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	item_details = db.Column(db.String, nullable=True)
	posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())

	def __init__(self, name, item_details, posted_date):
		self.name = name
		self.item_details = item_details
		self.posted_date = posted_date

	def __repr__(self):
		return '<name %r' % (self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True, unique=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)