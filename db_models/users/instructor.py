from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .user import *

class Instructor(User):
    __tablename__ = "instructor"
    id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    phone_number: Mapped[str] = mapped_column(String(30))
    specialization: Mapped[str] = mapped_column(String(30))
    __mapper_args__ = {
        'polymorphic_identity': 'instructor',
    }
    def __repr__(self) -> str:
        return f"Instructor(id={self.id!r}, name={self.username!r})"
    def reserve_time_location():
        pass

def create_instructor(session: Session,
username: str,
password: str,
first_name: str,
last_name: str,
phone_number: str,
specialization: str):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    new_instructor = Instructor(username=username,
    hashed_pass=hashed_pass,
    salt=salt.decode('utf-8'),
    type="instructor",
    first_name = first_name,
    last_name = last_name,
    phone_number = phone_number,
    specialization = specialization)
    
    try:
        session.add(new_instructor)
        session.commit()
        print(f"Instructor {username} created successfully!")
    except IntegrityError:
        session.rollback()
        print(f"Username '{username}' already exists. Please choose another one.")