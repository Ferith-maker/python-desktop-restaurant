from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///maDatabase.db')

#creation de la db
Base = declarative_base()
