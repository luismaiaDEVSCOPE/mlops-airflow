from fastapi import FastAPI, Request, HTTPException
import mlflow.pyfunc
import mlflow
import numpy as np
import os

app = FastAPI()

# Try to load model from registry, fallback to local artifact if not available
try:
    model = mlflow.pyfunc.load_model("models:/Iris-RandomForest-Best/Production")
    print("Model loaded from registry: Iris-RandomForest-Best/Production")
except Exception as e:
    print(f"Could not load from registry: {e}")
    try:
        # Fallback to latest run artifact
        model = mlflow.pyfunc.load_model("runs:/<run_id>/model")  # You'll need to replace <run_id>
        print("Model loaded from run artifact")
    except Exception as e2:
        print(f"Could not load model: {e2}")
        model = None

@app.get("/")
async def root():
    return {"message": "MLflow Model API", "model_loaded": model is not None}

@app.post("/predict")
async def predict(request: Request):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    data = await request.json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
