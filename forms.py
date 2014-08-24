from flask_wtf import Form
#from flask.ext import wtf
from wtforms import TextField, IntegerField, DateField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from cktext import CKTextAreaField


class AddItemForm(Form):
    item_id = IntegerField('Item ID') #dont really see why i need this?
    name = TextField('Item Name', default="", validators=[DataRequired()])
    item_details = CKTextAreaField('Item Details', default="", validators=[DataRequired()])
    #item_details = TextField('Item Details', default="", validators=[DataRequired()])
	# posted_date = DateField('Date Due (mm/dd/yyyy)') not using
        #item_details = WysiwygField('Item Details', validators=[DataRequired()])

class RegisterForm(Form):
    name = TextField('Username', validators=[DataRequired(), Length(min=2, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=40)])
    confirm = PasswordField('Repeat Password',[DataRequired(), EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    name = TextField('Username', validators=[DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired()])
        