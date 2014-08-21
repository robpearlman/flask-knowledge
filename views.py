#views.py

#################
#### imports ####
#################
from flask import Flask, flash, redirect, render_template, session, url_for, request, jsonify, make_response
from flask.ext.sqlalchemy import SQLAlchemy
from forms import AddItemForm


################
#### config ####
################

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import ItemTable

################
#### routes ####
################

@app.route('/') #, methods=['GET'] # redundant
def holding():
	return redirect(url_for('items'))

@app.route('/items/')
def items():
	error = None
	form = AddItemForm(request.form)
	all_tasks = db.session.query(ItemTable).all()
	if request.method == 'GET':
		return render_template('items.html', form=form, all_tasks = all_tasks)





