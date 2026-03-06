from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    """Request model for creating a user.

    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
        score (int): The score achieved by the user.

    """

    name: str
    age: int
    score: int


class UserResponse(BaseModel):
    """Response model for user data.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        age (int): The age of the user.
        score (int): The score achieved by the user.

    """

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int
    score: int
