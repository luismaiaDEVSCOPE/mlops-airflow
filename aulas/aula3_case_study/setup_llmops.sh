#!/bin/bash

# 🌱🤖 LLMOps Setup Script for Aula 3
# Plant Care Assistant with Prompt Engineering

set -e  # Exit on any error

echo "🌱🤖 Setting up LLMOps Plant Care Assistant..."
echo "================================================="

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check prerequisites
echo ""
echo "🔍 Checking prerequisites..."

# Check Docker
if command -v docker &> /dev/null; then
    print_status "Docker is installed"
    docker --version
else
    print_error "Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check Docker Compose
if command -v docker-compose &> /dev/null || docker compose version &> /dev/null; then
    print_status "Docker Compose is available"
else
    print_error "Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

# Check available memory
echo ""
echo "💾 Checking system resources..."

if command -v free &> /dev/null; then
    MEMORY_MB=$(free -m | awk 'NR==2{printf "%.0f", $2}')
    if [ "$MEMORY_MB" -gt 8000 ]; then
        print_status "Sufficient memory available: ${MEMORY_MB}MB"
    else
        print_warning "Low memory detected: ${MEMORY_MB}MB. Recommended: 8GB+"
        echo "   The LLM services may run slowly or fail to start."
    fi
fi

# Create necessary directories
echo ""
echo "📁 Creating project directories..."

mkdir -p airflow/logs
mkdir -p airflow/plugins
mkdir -p artifacts
mkdir -p data

print_status "Directories created"

# Set up environment variables
echo ""
echo "🔧 Setting up environment..."

# Create .env file for Airflow
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOF
# Airflow Configuration
AIRFLOW_UID=50000
AIRFLOW_GID=0

# LLMOps Configuration
MODEL_NAME=llama2:7b
OLLAMA_HOST=0.0.0.0

# MLflow Configuration
MLFLOW_TRACKING_URI=http://mlflow:5000
EOF
    print_status ".env file created"
else
    print_info ".env file already exists"
fi

# Pull required Docker images
echo ""
echo "📥 Pulling Docker images (this may take a while)..."

cd docker

# Pull images
docker-compose pull

print_status "Docker images pulled successfully"

# Start services
echo ""
echo "🚀 Starting LLMOps services..."

# Start services in detached mode
docker-compose up -d

print_status "Services started successfully"

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to initialize..."

# Function to wait for service
wait_for_service() {
    local url=$1
    local service_name=$2
    local max_attempts=30
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        if curl -f "$url" > /dev/null 2>&1; then
            print_status "$service_name is ready"
            return 0
        fi
        
        echo -n "."
        sleep 3
        ((attempt++))
    done
    
    print_warning "$service_name took longer than expected to start"
    return 1
}

# Wait for MLflow
echo -n "Waiting for MLflow"
wait_for_service "http://localhost:5000/health" "MLflow"

# Wait for Airflow
echo -n "Waiting for Airflow"
wait_for_service "http://localhost:8080/health" "Airflow"

# Pull LLM model
echo ""
echo "🤖 Setting up LLM model..."

print_info "Pulling LLM model (this will take several minutes)..."
docker exec ollama_server ollama pull llama2:7b

if [ $? -eq 0 ]; then
    print_status "LLM model (llama2:7b) downloaded successfully"
else
    print_warning "LLM model download failed. You can try again later with:"
    echo "   docker exec ollama_server ollama pull llama2:7b"
fi

# Test services
echo ""
echo "🧪 Testing services..."

# Test MLflow
if curl -f "http://localhost:5000/health" > /dev/null 2>&1; then
    print_status "MLflow is accessible"
else
    print_warning "MLflow may not be fully ready yet"
fi

# Test Ollama
if curl -f "http://localhost:11434/api/tags" > /dev/null 2>&1; then
    print_status "Ollama is accessible"
else
    print_warning "Ollama may not be fully ready yet"
fi

# Create initial experiment in MLflow
echo ""
echo "🔬 Setting up MLflow experiment..."

python3 -c "
import requests
import json

try:
    # Create plant-care-llmops experiment
    response = requests.post(
        'http://localhost:5000/api/2.0/mlflow/experiments/create',
        json={'name': 'plant-care-llmops'},
        timeout=10
    )
    
    if response.status_code in [200, 400]:  # 400 if already exists
        print('✅ MLflow experiment ready')
    else:
        print('⚠️ Could not create MLflow experiment')
        
except Exception as e:
    print(f'⚠️ MLflow experiment setup: {e}')
" 2>/dev/null || print_warning "MLflow experiment setup skipped"

# Setup complete
echo ""
echo "🎉 LLMOps Setup Complete!"
echo "========================="
echo ""
print_info "Services are now running:"
echo ""
echo "🔗 Airflow UI:     http://localhost:8080 (admin/admin)"
echo "🔗 MLflow UI:      http://localhost:5000"
echo "🔗 Plant Care API: http://localhost:8081"
echo "🔗 Ollama API:     http://localhost:11434"
echo ""
print_info "Next steps:"
echo ""
echo "1. 📖 Read the README_LLMOps.md for detailed instructions"
echo "2. 🌐 Open Airflow UI and trigger the 'llmops_plant_care_pipeline' DAG"
echo "3. 🧪 Test the Plant Care Assistant:"
echo "   curl -X POST http://localhost:8081/chat \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"query\": \"My plant leaves are turning yellow\"}'"
echo ""
print_info "To stop services:"
echo "   docker-compose down"
echo ""
print_info "To restart services:"
echo "   docker-compose up -d"
echo ""
print_info "To view logs:"
echo "   docker-compose logs -f [service_name]"
echo ""
print_status "Happy LLMOps learning! 🌱✨"
