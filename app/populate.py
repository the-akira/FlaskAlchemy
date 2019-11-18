from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#Let’s import our Book and Base classes from our database_setup.py file
from database_setup import Book, Base

engine = create_engine('sqlite:///books-collection.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

## Criando Primeira entrada no Banco de Dados
# bookOne = Book(title="The Bell Jar", author="Sylvia Pla", genre="roman à clef")
# session.add(bookOne)
# session.commit()

## Editando a Primeira entrada do Banco de Dados
# editedBook = session.query(Book).filter_by(id=1).one()
# editedBook.author = "Sylvia Plath"
# session.add(editedBook)
# session.commit()

## Deletando uma entrada do Banco de Dados
bookToDelete = session.query(Book).filter_by(title='The Bell Jar').one()
session.delete(bookToDelete)
session.commit()

session.close()