from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Importando dependências
# >>> from biblioteca import db, Autor, Livro

## Inicializando Banco de Dados e Tabelas
# >>> db.create_all()

## Cadastrando Autor
# >>> autor_1 = Autor(nome='Gabriel', sobrenome='Felippe')
# >>> db.session.add(autor_1)
# >>> db.session.commit()

## Cadastrando Livro
# >>> livro_1 = Livro(titulo='Python Iluminado', sumario='Guia Basico de Python', autor_id=autor_1.id)
# >>> db.session.add(livro_1)
# >>> db.session.commit()

## Referenciando o autor do Livro
# >>> livro_1.autor

class Autor(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(20), nullable=False)
	sobrenome = db.Column(db.String(120), nullable=False)
	livros = db.relationship('Livro', backref='autor', lazy=True)

	def __repr__(self):
		return f'Autor("{self.nome}", "{self.sobrenome}")'

class Livro(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(100), nullable=False)
	sumario = db.Column(db.String(250), nullable=False)
	autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)

	def __repr__(self):
		return f'Livro("{self.titulo}")'

if __name__ == '__main__':
	app.run(debug=True)