from pydantic import BaseModel

class UserCreate(BaseModel):
    """Request model for creating a user."""
    name: str
    age: int
    score: int
    
class UserResponse(BaseModel):
    """Response model for user data."""
    
    id: int
    name: str
    age: int
    score: int
    