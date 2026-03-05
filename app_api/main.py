from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = os.getenv("DEBUG", "false" ).lower() == "true"

app = FastAPI()


@app.get("/health")
def health():
    """Health check endpoint to verify that the API is running."""
    return {"status": "ok"}


@app.get("/data")
def get_data():
    data = {}
    return {"status": "success", "data" : data}

@app.post("/data")
def post_data(data: dict):
    return {
        "status": "success",
        "data" : data,
        "message" : "Created" 
    }


if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=DEBUG)