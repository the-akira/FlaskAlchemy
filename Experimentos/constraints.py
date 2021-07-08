from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///constraints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Define chave-primária
    unique_col = db.Column(db.String(50), unique=True) # Define um valor único
    notnull = db.Column(db.String(20), nullable=False) # Define uma coluna que não pode ser nula
    default = db.Column(db.Integer, server_default='10')

## Inicializando o Banco de Dados
# from constraints import db
# from constraints import MyTable
# db.create_all()

## Adicionando valores para o Banco de Dados
# row = MyTable(unique_col='Gabriel',notnull='valor')
# db.session.add(row)
# db.session.commit()
# row2 = MyTable(unique_col='Felippe',notnull='valor',default=20)
# db.session.add(row2)
# db.session.commit()