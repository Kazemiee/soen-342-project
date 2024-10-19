from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models.model import Base
from db_models.users import *

url = "sqlite:///./db/database.db"
engine = create_engine(url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

admin.create_admin(session, "admin", "admin")
user.sign_in(session, "admin", "admin")