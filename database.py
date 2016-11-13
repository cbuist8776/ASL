from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9144287'
app.config['MYSQL_USER'] = '43xVXD1ZYm'
app.config['MYSQL_DB'] = 'asl'
mysql = MySQL(app)

@app.route('/')
def index():
 	cur = mysql.connection.cursor()
 	cur.execute('''SELECT data FROM example WHERE id = 1''')
 	rv = cur.fetchall()
 	return str(rv)

if __name__ == '__main__':
	app.run(debug=True)