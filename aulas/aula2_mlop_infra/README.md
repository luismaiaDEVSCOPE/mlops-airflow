

# Class II: Deep-dive into MLOps & Infrastructure

## Goal
Get hands-on with MLOps infrastructure by running MLflow and a model-serving API directly from Docker containers. Learn experiment tracking, model registry, and how to use your trained model via an API.

## Class Structure

### Prerequisites
Students only need:
- **Docker** and **Docker Compose** installed
- A web browser
- No Python, MLflow, or other tools needed locally!

### Quick Start
1. Clone the repository
2. Navigate to `aulas/aula2_mlop_infra/`
3. Run: `docker-compose up -d`
4. **Validate everything is working**:
   ```bash
   # Option 1: Python script
   python validate_environment.py
   
   # Option 2: PowerShell (Windows)
   .\validate_environment.ps1
   
   # Option 3: Manual check
   docker-compose ps
   ```
5. Open your browser to:
   - **JupyterLab**: http://localhost:8888 (main workspace)
   - **MLflow UI**: http://localhost:5000 (experiment tracking)
   - **API**: http://localhost:8080 (model serving)

### 1. Infrastructure Management & Quick Demo (15 min)
- Show the containerized setup: JupyterLab + MLflow + API
- Demonstrate accessing all three services from the browser
- Explain the benefits: consistent environment, no local setup needed

### 2. Hands-on in JupyterLab (50 min)
Students work through the notebook (`tracking_mlflow.ipynb`) which covers:

#### Experiment Tracking (25 min)
- **Concept**: Why tracking parameters and metrics matters for reproducibility
- **Hands-on**: Train models in JupyterLab, see experiments in MLflow UI
- **Practice**: Try different hyperparameters, compare results

#### Model Registry (25 min)
- **Concept**: Centralized, versioned model storage and lifecycle management
- **Hands-on**: Register models, promote between Staging/Production stages
- **Practice**: Version management and model governance

### 3. API Testing & Wrap-up (25 min)
- Test the containerized API directly from JupyterLab
- Make predictions with the registered model
- Discuss the complete MLOps workflow: Track → Register → Serve
- Preview next class: "We'll automate this entire process!"

## 🛠️ Troubleshooting Guide

### Common Issues & Solutions

**MLflow UI not loading?**
```bash
# Check if container is running
docker-compose ps

# Check logs
docker-compose logs mlflow
```

**JupyterLab connection issues?**
```bash
# Get the access token
docker-compose logs jupyter

# Look for: http://127.0.0.1:8888/lab?token=XXXXX
```

**Model Registry errors in notebook?**
- Make sure you run cells in order
- Check MLflow server connectivity first
- Verify all containers are running: `docker-compose ps`
- Look for error messages in the notebook output

**API connection failed?**
```bash
# Test API directly
curl http://localhost:8080/health

# Check API logs
docker-compose logs api
```

### Container Management Commands
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs for specific service
docker-compose logs [mlflow|jupyter|api]

# Restart a specific service
docker-compose restart [service-name]

# Check container status
docker-compose ps
```

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
