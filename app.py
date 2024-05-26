import os
import io
import requests
import numpy as np
from PIL import Image
from fastapi import FastAPI, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from keras.models import load_model
from keras.preprocessing import image as keras_image
from keras.applications.vgg16 import preprocess_input
import cloudinary
import cloudinary.api
from dotenv import load_dotenv
import httpx
import asyncio

app = FastAPI()

load_dotenv()

# Load the saved model
model = load_model("VGG16.h5")

cloud_name = os.getenv('CLOUD_NAME')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')

# Define the classes
class_names = ['healthy', 'unhealthy']

cloudinary.config( 
  cloud_name=cloud_name, 
  api_key=api_key, 
  api_secret=api_secret 
)

def process_image(public_id):
    image_url = cloudinary.api.resource(public_id)["url"]

    response = requests.get(image_url)
    image_data = response.content

    img = Image.open(io.BytesIO(image_data))
    img = img.resize((224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index] * 100

    # Return the results
    results = {
        'predicted_class': predicted_class,
        'confidence': confidence
    }
    return results

@app.get("/result/{public_id}")
async def image_result(public_id: str):
    analysis_result = process_image(public_id)
    json_response = jsonable_encoder(analysis_result)
    return JSONResponse(content=json_response, status_code=200)

@app.get("/health")
async def health_check():
    return {"status": "alive"}

async def keep_alive():
    while True:
        async with httpx.AsyncClient() as client:
            await client.get("http://localhost:8000/health")
        await asyncio.sleep(300)  # Wait for 5 minutes

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(keep_alive())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
