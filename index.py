from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'testdb'
mysql = MySQL()
mysql = MySQL(app)

@app.route('/')
def index():
	cur = mysql.get_db().cursor()
	cur.execute('''SELECT data FROM mytable WHERE id = 1''')
	rv = cur.fetchall()
	return str(rv)

if __name__ == '__main__':
	app.run(debug=True)
