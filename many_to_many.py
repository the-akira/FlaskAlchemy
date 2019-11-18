from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Usuários vs Canais de Youtube
## Muitos para Muitos

# Tabela de Conexão
subs = db.Table('subs', 
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('channel_id', db.Integer, db.ForeignKey('channel.channel_id'))
)

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	subscriptions = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

class Channel(db.Model):
	channel_id = db.Column(db.Integer, primary_key=True)
	channel_name = db.Column(db.String(50))

## Inicializando o Banco de Dados
# from many_to_many import *
# db.create_all()

## Adicionando Usuários
# user1 = User(name='Gabriel')
# user2 = User(name='Rafael')
# user3 = User(name='Miguel')
# user4 = User(name='Ariel')
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# db.session.add(user4)
# db.session.commit()

## Adicionando Canais do Youtube
# channel1 = Channel(channel_name='Corey')
# channel2 = Channel(channel_name='Traversy')
# db.session.add(channel1)
# db.session.add(channel2)
# db.session.commit()

## Adicionado Usuários aos Canais
# channel1.subscribers.append(user1)
# channel1.subscribers.append(user2)
# channel1.subscribers.append(user3)
# channel2.subscribers.append(user4)
# channel2.subscribers.append(user2)
# db.session.commit()

## Selecionando os inscritos do Canal 1
# for user in channel1.subscribers:
#     print(user.name)

## Selecionando os inscritos do Canal 2
# for user in channel2.subscribers:
#     print(user.name)