from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from biblioteca_sqlalchemy import Autor, Livro, Base

engine = create_engine('sqlite:///biblioteca.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

## Editando a Primeira entrada do Banco de Dados
livro = session.query(Livro).filter_by(id=1).one()
print(livro)
print(dir(livro))
print(livro.autor)
print(livro.id)
print(livro.titulo)
print(livro.sumario)

session.close()

# >>> from sqlalchemy import create_engine
# >>> from sqlalchemy.orm import sessionmaker
# >>> from biblioteca_sqlalchemy import Autor, Livro, Base
# >>> engine = create_engine('sqlite:///biblioteca.db')
# >>> Base.metadata.bind = engine
# >>> DBSession = sessionmaker(bind=engine)
# >>> session = DBSession()
# >>> autor_2 = Autor(nome='Felippe')
# >>> session.add(autor_2)
# >>> session.commit()
# >>> livro_1 = Livro(titulo='Python Matemática', sumario='Matemática e Python unidos', autor=autor_2)
# >>> session.add(livro_1)
# >>> session.commit()
# >>> livros = session.query(Livro).all()