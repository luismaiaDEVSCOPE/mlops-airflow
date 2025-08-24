"""
Bonsai Species Classification API
Serves models registered in MLflow Model Registry
"""

from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
import numpy as np
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', 'http://mlflow:5000')
MODEL_NAME = 'Airflow-Bonsai-Classifier-Production'
MODEL_STAGE = 'Production'

# Global variables
loaded_model = None
model_info = {}

def load_production_model():
    """Load the production model from MLflow Model Registry"""
    global loaded_model, model_info
    
    try:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        logger.info(f"🔗 Connecting to MLflow at {MLFLOW_TRACKING_URI}")
        
        # Try to load production model
        try:
            model_uri = f"models:/{MODEL_NAME}/{MODEL_STAGE}"
            loaded_model = mlflow.sklearn.load_model(model_uri)
            model_info = {
                "name": MODEL_NAME,
                "stage": MODEL_STAGE,
                "loaded_at": datetime.now().isoformat(),
                "status": "production"
            }
            logger.info(f"✅ Loaded production model: {MODEL_NAME}")
            
        except Exception as e:
            # If no production model, try latest version
            logger.warning(f"⚠️ No production model found, trying latest version: {e}")
            
            client = mlflow.tracking.MlflowClient()
            latest_versions = client.get_latest_versions(MODEL_NAME, stages=["None"])
            
            if latest_versions:
                latest_version = latest_versions[0].version
                model_uri = f"models:/{MODEL_NAME}/{latest_version}"
                loaded_model = mlflow.sklearn.load_model(model_uri)
                model_info = {
                    "name": MODEL_NAME,
                    "version": latest_version,
                    "stage": "None",
                    "loaded_at": datetime.now().isoformat(),
                    "status": "latest"
                }
                logger.info(f"✅ Loaded latest model version: {latest_version}")
            else:
                raise Exception(f"No model versions found for {MODEL_NAME}")
                
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")
        model_info = {
            "status": "error",
            "error": str(e),
            "loaded_at": datetime.now().isoformat()
        }

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    status = "healthy" if loaded_model is not None else "unhealthy"
    
    return jsonify({
        "status": status,
        "timestamp": datetime.now().isoformat(),
        "service": "bonsai-classifier-api",
        "model_info": model_info,
        "mlflow_uri": MLFLOW_TRACKING_URI
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Predict bonsai species from features"""
    try:
        if loaded_model is None:
            return jsonify({
                "error": "Model not loaded",
                "status": "error"
            }), 500
        
        # Get input data
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({
                "error": "Missing 'features' in request body",
                "expected_format": {
                    "features": [2.0, 1.5, 5.0, 25.0]
                }
            }), 400
        
        features = data['features']
        
        # Validate input
        if len(features) != 4:
            return jsonify({
                "error": "Expected 4 features",
                "received": len(features),
                "expected_features": [
                    "leaf_length_cm", 
                    "leaf_width_cm", 
                    "branch_thickness_mm", 
                    "height_cm"
                ]
            }), 400
        
        # Make prediction
        features_array = np.array([features])
        prediction = loaded_model.predict(features_array)[0]
        
        # Get prediction probabilities if available
        try:
            probabilities = loaded_model.predict_proba(features_array)[0]
            confidence = float(max(probabilities))
        except:
            probabilities = None
            confidence = None
        
        # Species mapping
        species_map = {0: "Juniper", 1: "Ficus", 2: "Pine", 3: "Maple"}
        species_name = species_map.get(prediction, "Unknown")
        
        response = {
            "prediction": int(prediction),
            "species": species_name,
            "confidence": confidence,
            "input_features": {
                "leaf_length_cm": features[0],
                "leaf_width_cm": features[1],
                "branch_thickness_mm": features[2],
                "height_cm": features[3]
            },
            "model_info": model_info,
            "timestamp": datetime.now().isoformat()
        }
        
        if probabilities is not None:
            response["probabilities"] = {
                species_map[i]: float(prob) 
                for i, prob in enumerate(probabilities)
            }
        
        logger.info(f"🌳 Prediction: {species_name} (confidence: {confidence})")
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"❌ Prediction error: {e}")
        return jsonify({
            "error": str(e),
            "status": "prediction_failed",
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/model/info', methods=['GET'])
def model_info_endpoint():
    """Get detailed model information"""
    return jsonify({
        "model_info": model_info,
        "mlflow_tracking_uri": MLFLOW_TRACKING_URI,
        "model_name": MODEL_NAME,
        "expected_stage": MODEL_STAGE,
        "api_version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "model_info": "/model/info",
            "reload": "/model/reload"
        }
    })

@app.route('/model/reload', methods=['POST'])
def reload_model():
    """Reload model from MLflow Registry"""
    try:
        load_production_model()
        return jsonify({
            "status": "model_reloaded",
            "model_info": model_info,
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "status": "reload_failed",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/', methods=['GET'])
def root():
    """Root endpoint with API information"""
    return jsonify({
        "service": "Bonsai Species Classifier API",
        "description": "MLOps API integrated with Airflow and GitHub Actions",
        "version": "1.0.0",
        "endpoints": {
            "health_check": "/health",
            "prediction": "/predict",
            "model_info": "/model/info",
            "reload_model": "/model/reload"
        },
        "usage": {
            "predict": {
                "method": "POST",
                "url": "/predict",
                "body": {
                    "features": [2.0, 1.5, 5.0, 25.0]
                }
            }
        },
        "model_info": model_info
    })

if __name__ == '__main__':
    logger.info("🚀 Starting Bonsai Classification API...")
    
    # Load model on startup
    load_production_model()
    
    # Start Flask app
    app.run(host='0.0.0.0', port=8080, debug=False)
