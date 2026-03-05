from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] =  mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column()
    age : Mapped[int]  = mapped_column()
    score : Mapped[str] = mapped_column()
    