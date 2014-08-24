from flask_wtf import Form
from wtforms import TextField, IntegerField, DateField
from wtforms.validators import DataRequired
#from wysiwyg import WysiwygField

class AddItemForm(Form):
    item_id = IntegerField('Item ID') #dont really see why i need this?
    name = TextField('Item Name', default="", validators=[DataRequired()])
    item_details = TextField('Item Details', default="", validators=[DataRequired()])
	# posted_date = DateField('Date Due (mm/dd/yyyy)') not using
        #item_details = WysiwygField('Item Details', validators=[DataRequired()])