

# Lesson 2: MLOps & Infrastructure (Docker-first Practical)

## Goal
Get hands-on with MLOps infrastructure by running MLflow and a model-serving API directly from Docker containers. Learn experiment tracking, model registry, and how to use your trained model via an API.

## Lesson Structure

### 1. Infrastructure Management & Quick Demo (20 min)
- Quick intro to MLOps infrastructure and containerization.
- Show how to run MLflow and a FastAPI/Flask API from Docker containers.
- Demo: Start both containers, access MLflow UI and API endpoint locally.

### 2. Experiment Tracking (30 min)
- **Concept:** Why it's important to log parameters and metrics for reproducibility.
- **Hands-on:** Run a training script (from notebook or Python file) that logs to MLflow (served from Docker). Explore experiments, metrics, and artifacts in the MLflow UI.

### 3. Model Registry (20 min)
- **Concept:** Why a centralized and versioned model registry matters.
- **Hands-on:** Register the best model in the MLflow Model Registry and promote it between "Staging" and "Production" in the UI (served from Docker).

### 4. Wrap-up: Using the API with Your Trained Model (20 min)
- Use the running API container to make predictions with your trained model.
- Test the endpoint with Postman/curl and discuss how this fits into a real MLOps workflow.
- Recap: We have experiment tracking, model registry, and a working API—all running locally in containers.
- Tease the next lesson: "Next, we'll automate the whole process!"

---

Suggested Folder Structure:
```
aula2_mlop_infra/
├── notebooks/
│   └── tracking_mlflow.ipynb
├── src/
│   └── train_model.py
├── docker/
│   └── Dockerfile
│   └── requirements.txt
│   └── docker-compose.yml
├── api/
│   └── app.py
├── README.md
```
