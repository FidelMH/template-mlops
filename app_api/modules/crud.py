from models.models import User
from models.schemas import UserCreate
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_users(session: Session):
    """Retrieve all users from the database."""
    stmt = select(User)
    users = session.scalars(stmt).all()
    return users


def create_user(user: UserCreate, session: Session) -> User:
    """Create a new user in the database and return the created user object."""
    new_user = User(**user.model_dump())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user
