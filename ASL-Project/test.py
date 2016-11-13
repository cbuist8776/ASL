from flask import Flask
import mysql.connector
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['DEBUG']=True



# you will need create update and delete routes and methods here
# this is how you use this framework
# you will also need api and login functionalities here

@app.route("/list")
def list():
	cn = mysql.connector.connect(user='root', password='root', host='127.0.0.1',port='8889', database='ASL')
	cursor = cn.cursor()
	cursor.execute("select * from test")
	data = cursor.fetchall()
	
	return render_template("list.html",data =data)
	
	cursor.close()
	cn.close()

if __name__ == "__main__":
	app.run()
