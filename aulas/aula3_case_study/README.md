
# Class III: MLOps Automation with GitHub Actions + Airflow Integration

## 🎯 Learning Objectives

Transform manual MLOps workflows into **fully automated CI/CD pipelines** that integrate **GitHub Actions** with **Apache Airflow** for enterprise-grade ML orchestration.

### What You'll Build:
- **Automated Infrastructure**: Deploy MLOps stack via GitHub Actions
- **ML Pipeline Orchestration**: Use Airflow to manage complex ML workflows  
- **GitOps Integration**: Code changes trigger automated ML retraining
- **Production-Ready Setup**: Multi-service architecture with monitoring

## 🏗️ Architecture Overview

```
GitHub Push → GitHub Actions → Docker Compose → Airflow → MLflow → API
     ↓              ↓              ↓           ↓        ↓      ↓
   Trigger      CI/CD Tests    Infrastructure  ML     Model   Serving
               Validation      Deployment   Workflows Registry
```

### Services Deployed:
- **🔬 MLflow** (port 5000): Experiment tracking & model registry
- **🚁 Airflow** (port 8080): ML workflow orchestration  
- **🚀 API** (port 8081): Model serving endpoint
- **🐘 PostgreSQL** (port 5432): Airflow metadata database

## 🚀 Quick Start

### Prerequisites
- Git & GitHub account
- Docker & Docker Compose
- 8GB+ RAM recommended (for all services)

### 1. Setup Repository
```bash
# Fork this repository to your GitHub account
# Clone your fork
git clone <your-fork-url>
cd aulas/aula3_case_study

# Create environment file for Airflow
echo "AIRFLOW_UID=$(id -u)" > .env
```

### 2. Test Local Deployment
```bash
# Deploy the full stack locally
cd docker
docker compose up -d

# Check service status
docker compose ps

# View logs
docker compose logs -f
```

### 3. Access Services
- **Airflow UI**: http://localhost:8080 (admin/admin)
- **MLflow UI**: http://localhost:5000  
- **API**: http://localhost:8081

### 4. Trigger GitHub Actions
```bash
# Make a change and push to trigger CI/CD
echo "# Updated" >> README.md
git add README.md
git commit -m "Trigger CI/CD pipeline"
git push origin main
```

## 🔄 CI/CD Pipeline Flow

### Stage 1: Infrastructure Validation
```yaml
✅ Lint Python code (flake8)
✅ Validate Docker Compose syntax  
✅ Security scan Dockerfiles
✅ Test service configurations
```

### Stage 2: Continuous Training (CT)
```yaml
✅ Start MLflow tracking server
✅ Run automated model training
✅ Validate model performance
✅ Archive training artifacts
```

### Stage 3: Continuous Deployment (CD)
```yaml
✅ Build Docker images
✅ Deploy full MLOps stack
✅ Initialize Airflow & PostgreSQL
✅ Trigger Airflow ML pipeline
```

### Stage 4: Integration Testing
```yaml
✅ Test API endpoints
✅ Validate service connectivity  
✅ Monitor Airflow DAG execution
✅ Send deployment notifications
```

## 🚁 Airflow Integration

### MLOps DAG: `mlops_github_integration_pipeline`

The Airflow DAG orchestrates the complete ML lifecycle:

```python
check_mlflow → prepare_data → train_models → register_best_model
                                    ↓
validate_deployment → send_notification → cleanup
```

### Key Features:
- **Automated Triggering**: GitHub Actions triggers Airflow DAGs
- **ML Workflow Management**: Multi-step model training & validation
- **Model Registry Integration**: Automatic model registration in MLflow
- **Error Handling**: Robust retry logic and failure notifications

### Airflow Tasks:
1. **🔍 Check MLflow Connection**: Verify tracking server connectivity
2. **📊 Prepare Training Data**: Generate synthetic bonsai dataset  
3. **🤖 Train Model Experiments**: Multiple model configurations
4. **📦 Register Best Model**: MLflow Model Registry integration
5. **✅ Validate Deployment**: Test model loading & inference
6. **📢 Send Notification**: Pipeline completion alerts

## 🛠️ Configuration

### Environment Variables
```bash
# MLflow Configuration
MLFLOW_TRACKING_URI=http://mlflow:5000

# Airflow Configuration  
AIRFLOW_UID=50000
AIRFLOW__CORE__EXECUTOR=LocalExecutor

# Database Configuration
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
```

### GitHub Secrets (Optional)
```bash
DOCKER_REGISTRY=your-registry.com
DEPLOY_ENVIRONMENT=staging
SLACK_WEBHOOK_URL=https://hooks.slack.com/...
```

## 🧪 Testing the Pipeline

### Manual API Testing
```bash
# Health check
curl http://localhost:8081/health

# Prediction test
curl -X POST http://localhost:8081/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [2.0, 1.5, 5.0, 25.0]}'
```

### Airflow DAG Testing
```bash
# List available DAGs
docker compose exec airflow-webserver airflow dags list

# Trigger DAG manually
docker compose exec airflow-webserver airflow dags trigger mlops_github_integration_pipeline

# Check DAG run status
docker compose exec airflow-webserver airflow dags state mlops_github_integration_pipeline 2024-01-01
```

### Integration Tests
```bash
# Run automated tests
python -m pytest tests/ -v

# Test specific components
python -m pytest tests/test_api.py -v
python -m pytest tests/test_infrastructure.py -v
```

## 🔍 Monitoring & Debugging

### Service Health Checks
```bash
# Check all services
docker compose ps

# Service-specific logs
docker compose logs mlflow
docker compose logs airflow-webserver  
docker compose logs airflow-scheduler
docker compose logs postgres
docker compose logs api
```

### Airflow Debugging
```bash
# Access Airflow container
docker compose exec airflow-webserver bash

# Check Airflow configuration
airflow config list

# View DAG details
airflow dags show mlops_github_integration_pipeline
```

### Common Issues & Solutions

**🔥 Port Conflicts**
```bash
# Check port usage
netstat -tulpn | grep -E "(5000|8080|8081|5432)"

# Stop conflicting services
sudo systemctl stop apache2  # if using port 8080
```

**🔥 MLflow Connection Issues**
```bash
# Check MLflow health
curl http://localhost:5000/health

# Restart MLflow service
docker compose restart mlflow
```

**🔥 Airflow Initialization Problems**
```bash
# Check Airflow logs
docker compose logs airflow-init

# Reset Airflow database
docker compose down -v
docker compose up airflow-init
```

## 📊 Production Considerations

### Scaling to Cloud
- **AWS**: Use ECS/EKS for container orchestration
- **Azure**: Deploy to ACI/AKS with Azure ML integration
- **GCP**: Use Cloud Run/GKE with Vertex AI

### Security Hardening
- Use secrets management (AWS Secrets Manager, etc.)
- Enable HTTPS/TLS for all services
- Implement authentication & authorization
- Regular vulnerability scanning

### Monitoring & Observability  
- **Metrics**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger for distributed tracing
- **Alerting**: PagerDuty/Slack integration

## 🎓 Learning Path

**Class II** → **Class III** → **Class IV**
```
Infrastructure    →    CI/CD + Airflow    →    Cloud + Kubernetes
   as Code             Orchestration           Production Scale
```

### Next Steps:
1. **Explore Airflow UI**: Understand DAG visualization & monitoring
2. **Customize Workflows**: Add your own ML tasks to the DAG
3. **Scale Infrastructure**: Deploy to cloud environments  
4. **Add Monitoring**: Implement comprehensive observability

## 🤝 Contributing

Found an issue? Want to add features?
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`  
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📚 Additional Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)  
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

---

**🎉 Ready to automate your MLOps pipeline? Let's get started!**
- **Production Considerations**: Scaling to cloud environments (AWS, Azure, GCP)
- **Preview Next Class**: "Advanced orchestration with Kubernetes and Airflow!"

## 🚀 Quick Start

### Prerequisites
- **Git repository** with GitHub Actions enabled
- **Docker** and **Docker Compose** (from Class II)
- **GitHub account** for CI/CD pipeline hosting

### Setup
1. Fork this repository to your GitHub account
2. Clone your fork locally: `git clone <your-fork-url>`
3. Navigate to `aulas/aula3_case_study/`
4. **Review the automated pipeline**: `.github/workflows/mlops-pipeline.yml`
5. **Make a code change** and push to trigger the automated deployment

### Automated Pipeline Flow
```
Git Push → Infrastructure Validation → Model Training → Deployment → Testing
     ↓              ↓                    ↓              ↓         ↓
  Trigger      Docker Compose       MLflow Registry   Full Stack  Health Check
              Lint & Test          Auto-training     Deployment   & Validation
```

## 🛠️ Pipeline Configuration

### Environment Variables (GitHub Secrets)
```bash
# MLflow Configuration  
MLFLOW_TRACKING_URI=http://localhost:5000
MLFLOW_BACKEND_STORE_URI=sqlite:///mlflow.db

# Docker Configuration
DOCKER_REGISTRY=your-registry.com
IMAGE_TAG=latest

# Deployment Configuration
DEPLOY_ENVIRONMENT=staging  # or production
```

### Pipeline Stages

#### 1. Infrastructure Validation
- Lint `docker compose.yml` and Dockerfiles
- Validate infrastructure configuration
- Security scan for container vulnerabilities
- Test service dependencies and networking

#### 2. Continuous Training (CT)
- Automated model training on code/data changes
- MLflow experiment tracking and comparison  
- Model validation against performance thresholds
- Automated model registration and versioning

#### 3. Continuous Deployment (CD)
- Deploy full MLOps stack using Docker Compose
- Automated service health checks and validation
- Integration testing of the complete pipeline
- Automated rollback on deployment failures

## 🔧 Troubleshooting Automated Deployments

### Pipeline Failures

**Infrastructure Validation Failed?**
```bash
# Check Docker Compose syntax
docker compose config

# Validate service definitions
docker compose ps
```

**Model Training Pipeline Failed?**
```bash
# Check MLflow server connectivity
curl http://localhost:5000/health

# Review training logs
docker compose logs -f mlflow
```

**Deployment Pipeline Failed?**
```bash
# Check service startup order
docker compose logs --tail=100

# Validate container health
docker compose ps
docker compose exec api curl http://localhost:8080/health
```

### GitHub Actions Debugging
```bash
# View pipeline logs in GitHub Actions tab
# Check for: "Run failed" or "Deploy failed"

# Common fixes:
# 1. Check GitHub Secrets configuration
# 2. Verify Docker Compose file syntax  
# 3. Review MLflow server connectivity
# 4. Check for port conflicts (5000, 8080, 8888)
```
---

## 📁 Project Structure
```
aula3_case_study/
├── .github/
│   └── workflows/
│       └── mlops-pipeline.yml      # Complete CI/CD pipeline
├── docker/
│   ├── docker compose.yml          # Infrastructure as Code (from Class II)
│   ├── Dockerfile                  # API service container
│   └── requirements.txt            # Python dependencies
├── src/
│   ├── train_model.py              # Automated training script
│   └── model_validation.py         # Model performance validation
├── api/
│   ├── app.py                      # Model serving API
│   └── health_check.py             # API health monitoring
├── tests/
│   ├── test_infrastructure.py      # Infrastructure validation tests
│   ├── test_model.py               # Model validation tests  
│   └── test_api.py                 # API integration tests
├── notebooks/
│   └── model_analysis.ipynb        # Interactive model analysis
└── README.md                       # This file
```