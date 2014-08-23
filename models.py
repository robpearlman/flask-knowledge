from views import db

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
