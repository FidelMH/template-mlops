import os

import pandas as pd
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


def seed_db(session: Session) -> None:
    """Seed the database with initial data from CSV if the table is empty."""
    if session.scalars(select(User)).first() is not None:
        return
    csv_path = os.path.join(
        os.path.dirname(__file__), "..", "data", "moncsv.csv"
    )
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        create_user(
            UserCreate(
                name=row["name"], age=int(row["age"]), score=float(row["score"])
            ),
            session,
        )
