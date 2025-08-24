#!/bin/bash

# MLOps CI/CD Setup Script
# Prepares the environment for GitHub Actions + Airflow integration

set -e

echo "🚀 Setting up MLOps CI/CD Pipeline with Airflow..."

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are available"

# Create necessary directories
echo "📁 Creating required directories..."
mkdir -p airflow/logs airflow/plugins airflow/dags
mkdir -p src api tests docker

echo "✅ Directories created"

# Set up environment file
echo "⚙️ Setting up environment configuration..."

if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ Environment file created from .env.example"
    else
        # Create basic .env file
        cat > .env << EOF
AIRFLOW_UID=$(id -u)
AIRFLOW_GID=0
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
MLFLOW_TRACKING_URI=http://mlflow:5000
EOF
        echo "✅ Basic environment file created"
    fi
else
    echo "✅ Environment file already exists"
fi

# Check available ports
echo "🔍 Checking port availability..."

PORTS=(5000 8080 8081 5432)
BLOCKED_PORTS=()

for port in "${PORTS[@]}"; do
    if netstat -tuln 2>/dev/null | grep -q ":$port "; then
        BLOCKED_PORTS+=($port)
    fi
done

if [ ${#BLOCKED_PORTS[@]} -gt 0 ]; then
    echo "⚠️ Warning: The following ports are already in use: ${BLOCKED_PORTS[*]}"
    echo "   Please stop services using these ports or modify docker-compose.yml"
    echo "   Required ports: 5000 (MLflow), 8080 (Airflow), 8081 (API), 5432 (PostgreSQL)"
else
    echo "✅ All required ports are available"
fi

# Validate Docker Compose file
echo "🔍 Validating Docker Compose configuration..."

if [ -f docker/docker-compose.yml ]; then
    cd docker
    if docker compose config > /dev/null 2>&1; then
        echo "✅ Docker Compose configuration is valid"
    else
        echo "❌ Docker Compose configuration has errors"
        docker compose config
        exit 1
    fi
    cd ..
else
    echo "❌ docker/docker-compose.yml not found"
    exit 1
fi

# Test local deployment (optional)
read -p "🚀 Would you like to test the local deployment now? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Starting local deployment..."
    
    cd docker
    
    # Pull latest images
    echo "📥 Pulling Docker images..."
    docker compose pull
    
    # Start services
    echo "🚀 Starting services..."
    docker compose up -d
    
    # Wait for services
    echo "⏳ Waiting for services to start..."
    
    # Wait for PostgreSQL
    echo "⏳ Waiting for PostgreSQL..."
    timeout 60 bash -c 'until docker compose exec -T postgres pg_isready -U airflow; do sleep 2; done'
    
    # Wait for MLflow
    echo "⏳ Waiting for MLflow..."
    timeout 120 bash -c 'until curl -f http://localhost:5000/health 2>/dev/null; do sleep 5; done'
    
    # Wait for Airflow
    echo "⏳ Waiting for Airflow..."
    timeout 180 bash -c 'until curl -f http://localhost:8080/health 2>/dev/null; do sleep 5; done'
    
    # Wait for API
    echo "⏳ Waiting for API..."
    timeout 120 bash -c 'until curl -f http://localhost:8081/health 2>/dev/null; do sleep 5; done'
    
    echo ""
    echo "🎉 Local deployment successful!"
    echo ""
    echo "📊 Services available:"
    echo "   🔬 MLflow UI: http://localhost:5000"
    echo "   🚁 Airflow UI: http://localhost:8080 (admin/admin)"
    echo "   🚀 API: http://localhost:8081"
    echo ""
    echo "💡 To stop services: docker compose down"
    echo "💡 To view logs: docker compose logs -f"
    
    cd ..
else
    echo "⏭️ Skipping local deployment test"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. 🔧 Review and customize docker/docker-compose.yml if needed"
echo "2. 🚁 Explore Airflow DAG in airflow/dags/mlops_github_integration.py"
echo "3. 🔄 Push changes to GitHub to trigger CI/CD pipeline"
echo "4. 📊 Monitor pipeline execution in GitHub Actions"
echo ""
echo "📚 Documentation: README.md"
echo "🆘 Troubleshooting: Check service logs with 'docker compose logs'"
echo ""
echo "🚀 Happy MLOps automation!"
