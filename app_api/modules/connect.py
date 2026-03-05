import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Création de l'unité de contrôle
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    """Get a database session."""
    db = SessionLocal(bind=engine)()
    try:
        yield db
    finally:
        db.close()
