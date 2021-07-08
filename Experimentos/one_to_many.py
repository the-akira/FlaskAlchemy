from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///one-to-many.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

## Inicializando o Banco de Dados
# from one_to_many import db
# db.create_all()
# from one_to_many import Person, Pet

## Criando uma Pessoa
# gabriel = Person(name='Gabriel')
# db.session.add(gabriel)
# db.session.commit()

## Criando um Pet
# pepe = Pet(name='Pepe', owner=gabriel)
# db.session.add(pepe)
# db.session.commit()

## Selecionando um Dono de Pet
# dono = Person.query.filter_by(name='Gabriel').first()

## Acessando os Dados
# dono.id
# dono.name
# dono.pets
# dono.pets[0].name

## Selecionando um Pet
# pepe = Pet.query.filter_by(name='Pepe').first()
# pepe.name
# pepe.owner.name
# pepe.owner_id

## Adicionando um novo Pet
# Dickie = Pet(name='Dickie', owner=dono)
# db.session.add(Dickie)
# db.session.commit()