from flask import Flask 
from flask_mysqldb import MySQL 

# Create your account: https://www.freemysqlhosting.net
# Configs
app = Flask(__name__)
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql10306376'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Routes
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')
    cur.execute('''INSERT INTO example VALUES (1, 'Gabriel')''')
    cur.execute('''INSERT INTO example VALUES (2, 'Rafael')''')
    mysql.connection.commit()
    cur.execute('''SELECT * FROM example''')
    results = cur.fetchall()
    print(results)
    return 'Done'

if __name__ == '__main__':
    app.run(debug=True)