from flask_wtf import Form
from wtforms import TextField, IntegerField, DateField
from wtforms.validators import DataRequired

class AddItemForm(Form):
	item_id = IntegerField('Item ID')
	name = TextField('Item Name', validators=[DataRequired()])
	item_details = TextField('Item Details', validators=[DataRequired()])
	created_date = DateField('Date Due (mm/dd/yyyy)')