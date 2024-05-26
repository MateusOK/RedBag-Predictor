import os
from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
