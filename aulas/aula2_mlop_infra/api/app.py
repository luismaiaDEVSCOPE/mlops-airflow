
from fastapi import FastAPI, Request
import mlflow.pyfunc
import numpy as np

app = FastAPI()
model = mlflow.pyfunc.load_model("models:/Iris-RandomForest-Best/Production")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
