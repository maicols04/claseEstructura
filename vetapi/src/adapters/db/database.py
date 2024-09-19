from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://vetdb:vetpass@localhost:3306/vetdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DATABASE_URL = "mysql+mysqlclient://vetdb:vetpass@localhost/vetdb"
# engine = create_engine(DATABASE_URL)
# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    session = Session()
    try:
        # yield session
        return session
    except:
        session.rollback()
        raise
    finally:
        session.close()
