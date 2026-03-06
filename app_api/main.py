import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from models.models import Base
from models.schemas import UserCreate, UserResponse
from modules.connect import SessionLocal, engine, get_db
from modules.crud import create_user, get_users, seed_db
from sqlalchemy.orm import Session

load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"


Base.metadata.create_all(bind=engine)

with SessionLocal() as session:
    seed_db(session)

app = FastAPI()


@app.get("/health")
def health():
    """Health check endpoint to verify that the API is running."""
    return {"status": "ok"}


@app.get("/data", response_model=list[UserResponse])
def get_data(session: Session = Depends(get_db)):
    """Retrieve data from the API."""
    data = get_users(session)
    return data


@app.post("/data", response_model=UserResponse)
def post_data(user: UserCreate, session: Session = Depends(get_db)):
    """Create new data in the API."""
    return create_user(user, session)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=DEBUG)
