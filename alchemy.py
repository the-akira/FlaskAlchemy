from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Imports Básicos e inicialização do banco de dados
# >>> from alchemy import db
# >>> db.create_all()
# >>> from alchemy import User, Post

## Criando Entradas no Banco de Dados
# >>> user_1 = User(username='Gabriel', email='gabriel@gmail.com', password='senha')
# >>> db.session.add(user_1)
# >>> db.session.commit()
# >>> user_2 = User(username='akira', email='akira@gmail.com', password='senha')
# >>> db.session.add(user_2)
# >>> db.session.commit()

## Executando consultas no banco de dados
# >>> User.query.all()
# >>> User.query.first()
# >>> User.query.filter_by(username='Gabriel').all()
# >>> User.query.filter_by(username='Gabriel').first()
# >>> user = User.query.filter_by(username='Gabriel').first()
# >>> user.id
# >>> user = User.query.get(1)
# >>> user.posts
# >>> post_1 = Post(title='Titulo', content='Conteudo', user_id=user.id)
# >>> post_2 = Post(title='Titulo 2', content='Conteudo 2', user_id=user.id)
# >>> db.session.add(post_1)
# >>> db.session.add(post_2)
# >>> db.session.commit()
# >>> user.posts
# >>> post = Post.query.first()
# >>> post.user_id
# >>> post.author

## Excluindo o banco de dados
# >>> db.drop_all()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f'User("{self.username}", "{self.email}", "{self.image_file}")'

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f'User("{self.title}", "{self.date_posted}")'

if __name__ == '__main__':
	app.run(debug=True)