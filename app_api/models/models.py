from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy models."""

    pass


class User(Base):
    """User model for the database.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        age (int): The age of the user.
        score (int): The score achieved by the user.

    """

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    score: Mapped[int] = mapped_column()
