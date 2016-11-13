from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql9.freemysqlhosting.net/sql9144287'
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__= 'asl'
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)