import cloudinary
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from keras.api.models import load_model

app = FastAPI()

load_dotenv()

cloud_name = os.getenv('CLOUD_NAME')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

cloudinary.config( 
  cloud_name=cloud_name, 
  api_key=api_key, 
  api_secret=api_secret 
)

model = load_model("path_to_model.h5")

class_names = ['healthy', 'unhealthy']

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
