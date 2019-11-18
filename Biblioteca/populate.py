from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from biblioteca_sqlalchemy import Autor, Livro, Base

engine = create_engine('sqlite:///livros_sqlalchemy.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object.
session = DBSession()

## Criando Primeira entrada no Banco de Dados
autor_1 = Autor(nome='Gabriel')
session.add(autor_1)
session.commit()

livro_1 = Livro(titulo='Python Iluminado', sumario='Guia Básico de Python', autor=autor_1)
session.add(livro_1)
session.commit()

session.close()