from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from flask_sql_alchemy import db
# db.create_all()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	location = db.Column(db.String(50))
	date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/<name>/<location>')
def index(name, location):
	user = User(name=name, location=location)
	db.session.add(user)
	db.session.commit()

	return '<h1>Usuário Adicionado</h1>'

@app.route('/<name>')
def get_user(name):
	user = User.query.filter_by(name=name).first()
	return f'The {user.name} is located in {user.location}'

if __name__ == '__main__':
	app.run(debug=True)