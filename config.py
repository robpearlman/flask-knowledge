#config.py 

import os

#get where folder sits

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'knowledge.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

#get full path for db

DATABASE_PATH = os.path.join(basedir, DATABASE)

#SQLAlchemy uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
