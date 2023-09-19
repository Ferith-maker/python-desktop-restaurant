from sqlalchemy import Integer, Column, String

from config.database import Base


class Categorie(Base):
    __tablename__= 'categorie'
    id_categorie = Column(Integer,primary_key= True,autoincrement=True)
    libelle = Column(String(50), nullable=False)
