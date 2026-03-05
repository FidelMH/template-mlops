from models.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session


def get_users(session: Session):
    """Retrieve all users from the database."""
    stmt = select(User)
    users = session.scalars(stmt).all()
    return users


# def create_user(session: Session):
