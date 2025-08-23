# MLOps Airflow Pipeline

A comprehensive MLOps platform built with Apache Airflow for orchestrating machine learning workflows, including data preprocessing, model training, inference, and monitoring.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Pipeline](#running-the-pipeline)
- [DAGs Overview](#dags-overview)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🎯 Overview

This project provides a complete MLOps solution using Apache Airflow for:
- **Data Ingestion**: Automated data extraction from SQL databases
- **Data Preprocessing**: Feature engineering and data transformation pipelines
- **Model Training**: Automated model training with MLflow integration
- **Model Inference**: Production inference pipelines
- **Monitoring**: Model performance and data drift monitoring

## ✨ Features

- 🐳 **Dockerized Environment**: Complete containerized setup with Docker Compose
- 🔄 **Automated Workflows**: End-to-end ML pipelines with dependency management
- 📊 **MLflow Integration**: Model versioning and experiment tracking
- 📓 **Notebook Execution**: Papermill integration for parameterized notebook execution
- 🗄️ **Database Connectivity**: Support for MSSQL and other databases
- 📈 **Monitoring**: Built-in monitoring with Flower and custom metrics
- 🔧 **Flexible Configuration**: Environment-based configuration management

## 🏗️ Architecture

The platform consists of the following components:

- **Airflow Webserver**: Web UI for managing workflows (Port 8080)
- **Airflow Scheduler**: Orchestrates task execution
- **Airflow Worker**: Executes tasks using CeleryExecutor
- **Flower**: Monitoring dashboard for Celery workers (Port 5555)
- **PostgreSQL**: Metadata database for Airflow
- **Redis**: Message broker for task distribution
- **MLflow**: Model registry and experiment tracking

## 🔧 Prerequisites

Before getting started, ensure you have the following installed:

- **Docker**: Community Edition (CE) with at least 4GB memory allocation
- **Docker Compose**: Version 1.29.1 or newer
- **Git**: For version control
- **Python 3.8+**: For local development (optional)

### System Requirements

- **Memory**: Minimum 8GB RAM (4GB allocated to Docker)
- **Storage**: At least 10GB free disk space
- **OS**: Windows 10/11, macOS, or Linux

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd mlops-airflow
```

### 2. Set Up Environment

Create the required directories and environment file:

```bash
# Create necessary directories
mkdir -p ./logs ./plugins

# Create .env file (Windows)
echo AIRFLOW_UID=50000 > .env

# For Linux/macOS users
mkdir -p ./dags ./logs ./plugins
echo "AIRFLOW_UID=$(id -u)" > .env
```

### 3. Build and Initialize

```bash
# Navigate to docker directory
cd docker

# Build custom images
docker compose build

# Initialize the database
docker compose up airflow-init
```

### 4. Start the Platform

```bash
# Start all services
docker compose up -d

# Check container health
docker compose ps
```

### 5. Access the Web Interface

- **Airflow UI**: http://localhost:8080
- **Flower Dashboard**: http://localhost:5555
- **Default Credentials**: `airflow` / `airflow`

## 📁 Project Structure

```
mlops-airflow/
├── artifacts/                 # Generated artifacts and outputs
├── docker/                   # Docker configuration
│   ├── docker compose.yml    # Main compose file
│   ├── Dockerfile            # Custom Airflow image
│   ├── requirements.txt      # Python dependencies
│   ├── airflow_worker/       # Worker-specific configuration
│   ├── config/               # Airflow configuration files
│   └── mlflow_dockerfile/    # MLflow service configuration
├── mlproject/                # Main project code
│   ├── clients/              # Client-specific implementations
│   ├── dags/                 # Airflow DAGs
│   │   ├── agent_rigor.py    # Data quality validation
│   │   ├── geo.py            # Geography processing
│   │   ├── inference_dag.py  # Model inference pipeline
│   │   ├── populate.py       # Data population
│   │   ├── notebooks/        # Jupyter notebooks for processing
│   │   └── statements/       # SQL statements and queries
│   └── engine/               # Core engine modules
│       ├── config.py         # Configuration management
│       ├── helpers/          # Helper utilities
│       └── scripts/          # Execution scripts
├── prj_requirements/         # Project requirements
├── tables/                   # Database table definitions
└── README.md                # This file
```

## ⚙️ Configuration

### Environment Variables

Key configuration options in your `.env` file:

```bash
# Airflow Configuration
AIRFLOW_UID=50000
AIRFLOW_IMAGE_NAME=apache/airflow:2.5.1

# Database Configuration
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

# MLflow Configuration
MLFLOW_BACKEND_STORE_URI=sqlite:///mlflow.db
MLFLOW_DEFAULT_ARTIFACT_ROOT=./mlruns
```

### Custom Dependencies

The project includes machine learning and data processing libraries:

- **Data Processing**: pandas, numpy, xlrd, unidecode
- **ML Libraries**: lightgbm, xgboost, scikit-learn, imblearn
- **Database**: pymssql for SQL Server connectivity
- **Notebook Execution**: papermill, apache-airflow-providers-papermill
- **Geospatial**: geopy for location processing
- **Optimization**: hyperopt for hyperparameter tuning

## 🏃‍♂️ Running the Pipeline

### Starting the Platform

```bash
cd docker
docker compose up -d
```

### Accessing Services

1. **Airflow Web UI**: Navigate to http://localhost:8080
2. **Login**: Use `airflow` / `airflow`
3. **Enable DAGs**: Toggle the DAGs you want to run
4. **Monitor**: Use the Graph View to monitor execution

### CLI Operations

Execute Airflow commands:

```bash
# Run airflow commands
docker compose exec airflow-worker airflow info

# Access interactive shell
docker compose exec airflow-worker bash

# View logs
docker compose logs airflow-scheduler
```

## 📊 DAGs Overview

### Available Workflows

1. **`agent_rigor.py`**: Data quality validation and cleansing
2. **`geo.py`**: Geospatial data processing and enrichment
3. **`inference_dag.py`**: Model inference and prediction pipeline
4. **`populate.py`**: Database population and data ingestion

### Notebook Execution

The platform executes Jupyter notebooks as part of the workflow:

- **`data_split.ipynb`**: Training/testing data splitting
- **`main_data_prep.ipynb`**: Primary data preprocessing
- **`inference_4_prod.ipynb`**: Production inference pipeline
- **`geo.ipynb`**: Geographic data processing
- **`utente.ipynb`**: User-specific data processing

## 🛠️ Development

### Adding New DAGs

1. Create your DAG file in `mlproject/dags/`
2. Follow Airflow best practices
3. Use the provided helper functions from `utils.py`
4. Test locally before deployment

### Extending Dependencies

To add new Python packages:

1. Update `docker/requirements.txt`
2. Rebuild the Docker image:
   ```bash
   docker compose build
   docker compose up -d
   ```

### Database Connections

Configure database connections in the Airflow UI:
- Go to Admin → Connections
- Add your database connection details
- Use the connection ID in your DAGs

## 🔍 Troubleshooting

### Common Issues

**Services won't start:**
```bash
# Check logs
docker compose logs

# Restart services
docker compose restart
```

**Permission issues (Linux/macOS):**
```bash
# Fix ownership
sudo chown -R $(id -u):$(id -g) ./logs ./plugins
```

**Out of memory:**
- Increase Docker memory allocation to 4GB+
- Monitor container resource usage

**Database connection errors:**
- Verify connection settings in Airflow UI
- Check network connectivity
- Validate credentials

### Health Checks

```bash
# Check all container status
docker compose ps

# View specific service logs
docker compose logs [service-name]

# Test Airflow scheduler
docker compose exec airflow-scheduler airflow scheduler --help
```

## 🧹 Cleaning Up

### Stop Services
```bash
docker compose down
```

### Complete Cleanup (removes all data)
```bash
# Stop and remove everything
docker compose down --volumes --rmi all

# Remove project directory (if needed)
# rm -rf /path/to/mlops-airflow
```

### Restart from Scratch
```bash
# Clean up
docker compose down --volumes --remove-orphans

# Remove images
docker compose down --rmi all

# Start fresh
docker compose up airflow-init
docker compose up -d
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a Pull Request

## 📚 Additional Resources

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Papermill Documentation](https://papermill.readthedocs.io/)

---

**Note**: This setup is optimized for development and testing. For production deployment, additional security configurations and resource optimizations are recommended.