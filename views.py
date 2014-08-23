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

from models import Item

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
    all_items = db.session.query(Item).all()
    if request.method == 'GET':
        return render_template('items.html', form=form, all_items = all_items)

@app.route('/add/', methods=['GET', 'POST'])
def add_item():
    import datetime
    error = None
    form = AddItemForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_item = Item(
                form.name.data,
                form.item_details.data,
                datetime.datetime.utcnow(),
            )
            db.session.add(new_item)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('items'))
        else:
            return render_template('items.html', form=form, error=error)
    else:
        return redirect(url_for('items'))



