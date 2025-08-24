"""
Plant Care LLMOps API
Serves LLM-powered plant care assistance using prompt engineering
"""

from flask import Flask, request, jsonify
import mlflow
import mlflow.pyfunc
import requests
import json
import logging
import os
from datetime import datetime
from typing import Dict, Any, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', 'http://mlflow:5000')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://ollama:11434')
# MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI', 'http://localhost:5000')
# OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
MODEL_NAME = 'llama2:7b'
EXPERIMENT_NAME = 'plant-care-llmops'

# Global variables
best_prompt_template = None
model_info = {}

def load_best_prompt():
    """Load the best performing prompt from MLflow"""
    global best_prompt_template, model_info
    
    try:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        logger.info(f"🔗 Connecting to MLflow at {MLFLOW_TRACKING_URI}")
        
        # Get the latest run from the experiment
        experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
        if experiment:
            runs = mlflow.search_runs(
                experiment_ids=[experiment.experiment_id],
                order_by=["start_time desc"],
                max_results=1
            )
            
            if not runs.empty:
                latest_run = runs.iloc[0]
                run_id = latest_run.run_id
                
                # Download the best prompt artifact
                try:
                    prompt_path = mlflow.artifacts.download_artifacts(
                        run_id=run_id, 
                        artifact_path="prompts/best_prompt.json"
                    )
                    
                    with open(prompt_path, 'r') as f:
                        prompt_data = json.load(f)
                    
                    best_prompt_template = prompt_data
                    model_info = {
                        "prompt_name": prompt_data.get("name", "unknown"),
                        "score": prompt_data.get("score", 0),
                        "loaded_at": datetime.now().isoformat(),
                        "status": "production",
                        "run_id": run_id
                    }
                    
                    logger.info(f"✅ Loaded best prompt: {prompt_data.get('name')}")
                    return True
                    
                except Exception as e:
                    logger.warning(f"⚠️ Could not load prompt artifact: {str(e)}")
        
        # Fallback to default prompt
        best_prompt_template = {
            "name": "friendly_helper",
            "template": """You are a friendly plant care helper who loves helping people grow healthy plants! 
Be encouraging and provide practical step-by-step advice.

Plant Parent Question: {query}

Friendly Advice:""",
            "input_variables": ["query"]
        }
        
        model_info = {
            "prompt_name": "friendly_helper",
            "score": 0.0,
            "loaded_at": datetime.now().isoformat(),
            "status": "fallback"
        }
        
        logger.info("📝 Using fallback prompt template")
        return True
        
    except Exception as e:
        logger.error(f"❌ Error loading prompt: {str(e)}")
        return False

def query_ollama(prompt: str) -> str:
    """Send query to Ollama LLM"""
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 200
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get("response", "Sorry, I couldn't generate a response.")
        else:
            logger.error(f"Ollama request failed: {response.status_code}")
            return "Sorry, the AI service is currently unavailable."
            
    except Exception as e:
        logger.error(f"Error querying Ollama: {str(e)}")
        return "Sorry, I encountered an error while processing your request."

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "plant-care-llmops-api",
        "model_info": model_info
    })

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint for plant care assistance"""
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({
                "error": "Missing 'query' field in request"
            }), 400
        
        user_query = data['query']
        
        # Validate input
        if not user_query.strip():
            return jsonify({
                "error": "Query cannot be empty"
            }), 400
        
        # Apply prompt template
        if best_prompt_template:
            formatted_prompt = best_prompt_template['template'].format(query=user_query)
        else:
            formatted_prompt = f"You are a plant care assistant. Answer this question: {user_query}"
        
        # Query the LLM
        logger.info(f"🤖 Processing query: {user_query[:50]}...")
        ai_response = query_ollama(formatted_prompt)
        
        # Prepare response
        response_data = {
            "query": user_query,
            "response": ai_response,
            "timestamp": datetime.now().isoformat(),
            "model": MODEL_NAME,
            "prompt_template": best_prompt_template.get('name', 'unknown') if best_prompt_template else 'fallback'
        }
        
        logger.info(f"✅ Response generated successfully")
        return jsonify(response_data)
        
    except Exception as e:
        logger.error(f"❌ Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/prompt-info', methods=['GET'])
def prompt_info():
    """Get information about the current prompt template"""
    return jsonify({
        "current_prompt": best_prompt_template,
        "model_info": model_info,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/evaluate', methods=['POST'])
def evaluate_response():
    """Evaluate a response for feedback (basic implementation)"""
    try:
        data = request.get_json()
        
        if not data or 'query' not in data or 'response' not in data or 'rating' not in data:
            return jsonify({
                "error": "Missing required fields: 'query', 'response', 'rating'"
            }), 400
        
        # Log evaluation data (in production, store in database)
        evaluation_data = {
            "query": data['query'],
            "response": data['response'], 
            "rating": data['rating'],
            "feedback": data.get('feedback', ''),
            "timestamp": datetime.now().isoformat(),
            "prompt_template": best_prompt_template.get('name', 'unknown') if best_prompt_template else 'fallback'
        }
        
        # In production, you would store this in a database for continuous learning
        logger.info(f"📊 Evaluation received: Rating {data['rating']}/5")
        
        return jsonify({
            "status": "evaluation_recorded",
            "message": "Thank you for your feedback!",
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"❌ Error in evaluate endpoint: {str(e)}")
        return jsonify({
            "error": "Internal server error"
        }), 500

@app.route('/models/available', methods=['GET'])
def available_models():
    """Get list of available models from Ollama"""
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)
        
        if response.status_code == 200:
            models_data = response.json()
            return jsonify({
                "available_models": models_data.get("models", []),
                "current_model": MODEL_NAME,
                "timestamp": datetime.now().isoformat()
            })
        else:
            return jsonify({
                "error": "Could not fetch available models",
                "current_model": MODEL_NAME
            }), 503
            
    except Exception as e:
        logger.error(f"❌ Error fetching models: {str(e)}")
        return jsonify({
            "error": "Service unavailable",
            "current_model": MODEL_NAME
        }), 503

@app.route('/', methods=['GET'])
def demo_queries():
    """Get demo queries for testing"""
    demo_data = [
        {
            "query": "My plant leaves are turning yellow, what should I do?",
            "category": "disease_diagnosis"
        },
        {
            "query": "How often should I water my succulent?",
            "category": "watering_advice"
        },
        {
            "query": "What's the best fertilizer for indoor plants?",
            "category": "fertilizer_advice"
        },
        {
            "query": "My plant isn't growing, help!",
            "category": "growth_issues"
        }
    ]
    
    return jsonify({
        "demo_queries": demo_data,
        "instructions": "Send POST request to /chat with {'query': 'your question'}"
    })

# Initialize the application
def initialize_app():
    """Initialize the Flask application"""
    logger.info("🚀 Initializing Plant Care LLMOps API")
    
    # Load the best prompt template
    if not load_best_prompt():
        logger.warning("⚠️ Using fallback configuration")
    
    logger.info("✅ API initialized successfully")

if __name__ == '__main__':
    initialize_app()
    app.run(host='0.0.0.0', port=6000, debug=True)
