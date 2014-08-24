#views.py

#################
#### imports ####
#################
from flask import Flask, flash, redirect, render_template, session, url_for, request, make_response
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from forms import AddItemForm, LoginForm, RegisterForm
from functools import wraps

import pdb

################
#### config ####
################

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from models import Item, User

################
#### routes ####
################

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'error')

@app.route('/') #, methods=['GET'] # redundant
def holding():
    return redirect(url_for('login'))

@app.route('/register/', methods=['GET', 'POST'])
def register():
    #pdb.set_trace()
    error = None
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        new_user = User(username=form.name.data)
        new_user.hash_password(form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
        except IntegrityError:
            error = 'Oh no! That username already exists. Please try again.'
            return render_template('register.html', form=form, error=error)
    else:
        return render_template('register.html', form=form, error=error)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    #pdb.set_trace()
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            error = 'Invalid username or password.'
            return render_template(
                "login.html",
                form=form,
                error=error
            )
        elif user.verify_password(form.password.data):
            session['logged_in'] = True
            session['username'] = user.username
            flash('You are logged in. Go Crazy.')
            return redirect(url_for('items'))
    if request.method == 'GET':
        return render_template('login.html', form=form)

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('You are logged out. Bye. :(')
    return redirect (url_for('login'))

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

####################
#### Item views ####
####################

# all my item views require a login.
# however my API views are wide open!!


@app.route('/delete/<int:item_id>/')
@login_required
def delete_item(item_id):
    delete_id = item_id
    db.session.query(Item).filter_by(item_id=delete_id).delete()
    db.session.commit()
    flash('The item was deleted.')
    return redirect(url_for('items'))

@app.route('/modify/<int:item_id>/')
@login_required
def modify_item(item_id):
    form = AddItemForm(request.form)
    modify_id = item_id
    result = db.session.query(Item).filter_by(item_id=item_id).first()
    form.name.data = result.name
    form.item_details.data = result.item_details
    form.item_id.data = result.item_id
    return render_template('items.html', form=form, modify_item = modify_item)

@app.route('/items/')
@login_required
def items():
    error = None
    form = AddItemForm(request.form)
    all_items = db.session.query(Item).all()
    if request.method == 'GET':
        return render_template('items.html', form=form, all_items = all_items)

@app.route('/add/', methods=['GET', 'POST'])
@login_required
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
@login_required
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

#####################
#### Error Views ####
#####################

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

################
#### apis   ####
################

import api



