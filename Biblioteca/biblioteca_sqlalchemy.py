from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///biblioteca.db', echo=True)
Base = declarative_base()
  
class Autor(Base):
    __tablename__ = "autores"
 
    id = Column(Integer, primary_key=True)
    nome = Column(String)
 
    def __repr__(self):
        return "{}".format(self.nome)
  
class Livro(Base):
    __tablename__ = "livros"
 
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    sumario = Column(String)
    autor_id = Column(Integer, ForeignKey("autores.id"))
    autor = relationship("Autor", backref=backref("livros", order_by=id))
 
# create tables
Base.metadata.create_all(engine)