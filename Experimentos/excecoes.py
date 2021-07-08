from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///excecoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	uniq = db.Column(db.String(50), unique=True)

## Inicializando Banco de Dados
# from excecoes import *
# db.create_all()

@app.route('/')
def index():
	exists = Member.query.filter_by(uniq='Felippe').first()
	if exists:
		return '<p>This member already exists</p>'
	felippe = Member(uniq='Felippe')
	db.session.add(felippe)
	db.session.commit()

	return '<p>Database entry added!</p>'

@app.route('/teste')
def teste():
	try:
		miguel = Member(uniq='Miguel')
		db.session.add(miguel)
		db.session.commit()
		return '<p>Database entry added!</p>'
	except IntegrityError:
		db.session.rollback()
		return '<p>This member already exists!</p>'

if __name__ == '__main__':
	app.run(debug=True)