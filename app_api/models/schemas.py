from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    """Request model for creating a user."""

    name: str
    age: int
    score: int


class UserResponse(BaseModel):
    """Response model for user data."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    score: int
