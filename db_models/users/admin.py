from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .user import *

class Admin(User):
    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }
    def __repr__(self) -> str:
        return f"Admin(id={self.id!r}, username={self.username!r})"
    def offer_time_location():
        pass

def create_admin(session: Session, username: str, password: str):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    new_admin = Admin(username=username, hashed_pass=hashed_pass, salt=salt.decode('utf-8'), type="admin")
    
    try:
        session.add(new_admin)
        session.commit()
        print(f"Admin {username} created successfully!")
    except IntegrityError:
        session.rollback()
        print(f"Username '{username}' already exists. Please choose another one.")