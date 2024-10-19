from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db_models.model import Base

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique = True)
    hashed_pass: Mapped[str] = mapped_column(String(128), nullable=False)
    salt: Mapped[str] = mapped_column(String(64), nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user',
    }
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"

    def on_sign_in(self) -> None:
        raise NotImplementedError("Failed to implement on_sign_in method for subclass of User")

def sign_in(session: Session, username: str, password: str) -> Optional[User]:
    user = session.query(User).filter_by(username=username).first()

    if user is None:
        print("User not found.")
        return None

    hashed_input_password = bcrypt.hashpw(password.encode('utf-8'), user.salt.encode('utf-8'))

    if hashed_input_password.decode('utf-8') == user.hashed_pass:
        print(f"{user.username} signed in.")
        return user
    print("Invalid password or username.")
    return None