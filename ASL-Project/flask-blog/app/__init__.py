from flask import Flask
fro flask.ext.sqlalchemy import SQLALchemy

#Create an Instance of Flask

app = Flask(__name__)

#Include config from config.py

app.config.from_object('config')
app.secret_key = 'some_secret'

#Create an instance of SQLAclhemy

db = SQLAlchemy(app)
from app import views, models
(venv)[leo@flask-blog]$ vim flask-blog/config.py

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/

#Add your connection string
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/