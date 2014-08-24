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

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

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

@app.route('/modify/', methods=['GET', 'POST'])
def save_modify():
    error = None
    form = AddItemForm(request.form)
    if request.method == 'POST':
        print form.item_id.data
        if form.validate_on_submit():
            db.session.query(Item).filter_by(item_id=form.item_id.data).update({
                "name":form.name.data, 
                "item_details":form.item_details.data
                })
            db.session.commit()
            flash('Item was updated')
            return redirect(url_for('items'))
        else:
            return render_template('items.html', form=form, error=error)
    else:
        return redirect(url_for('items'))

@app.route('/delete/<int:item_id>/')
def delete_item(item_id):
    delete_id = item_id
    db.session.query(Item).filter_by(item_id=delete_id).delete()
    db.session.commit()
    flash('The item was deleted.')
    return redirect(url_for('items'))

@app.route('/modify/<int:item_id>/')
def modify_item(item_id):
    form = AddItemForm(request.form)
    modify_id = item_id
    result = db.session.query(Item).filter_by(item_id=item_id).first()
    form.name.data = result.name
    form.item_details.data = result.item_details
    form.item_id.data = result.item_id
    return render_template('items.html', form=form, modify_item = modify_item)



################
#### apis   ####
################

import api



