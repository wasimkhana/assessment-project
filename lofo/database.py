from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./lofo.db'
#SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@localhost/db'
engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_recycle=3600)


#SessionLocal class of database session created using sessionmaker function
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


#Base class is created to store list of classes and mapped tables
Base = declarative_base()


def get_db():
    """
    A generator function creating `db` object of database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
