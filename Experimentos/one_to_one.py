from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///one-to-one.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    child = db.relationship('Child', backref='parent', uselist=False)

class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'), unique=True)

# from one_to_one import db
# db.create_all()
# from one_to_one import Parent, Child
# parent = Parent(name='Gabriel')
# child = Child(name='Crianca', parent=parent)
# db.session.add(parent)
# db.session.add(child)
# db.session.commit()