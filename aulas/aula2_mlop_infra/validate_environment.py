#!/usr/bin/env python3
"""
Quick validation script for Class II MLOps environment
Students can run this to verify all services are working correctly
"""

import requests
import time
import sys
from datetime import datetime

def check_service(name, url, timeout=5):
    """Check if a service is responding"""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            print(f"✅ {name}: Running (Status: {response.status_code})")
            return True
        else:
            print(f"⚠️ {name}: Unexpected status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ {name}: Connection failed - {e}")
        return False

def main():
    print("🔍 MLOps Class II - Environment Validation")
    print("=" * 50)
    print(f"⏰ Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    services = [
        ("MLflow Server", "http://localhost:5000/health"),
        ("JupyterLab", "http://localhost:8888"),
        ("FastAPI", "http://localhost:8080/health"),
    ]
    
    results = []
    for name, url in services:
        results.append(check_service(name, url))
    
    print()
    print("=" * 50)
    
    if all(results):
        print("🎉 All services are running correctly!")
        print("📚 Ready to start the notebook: notebooks/tracking_mlflow.ipynb")
        print()
        print("Quick links:")
        print("• JupyterLab: http://localhost:8888")
        print("• MLflow UI: http://localhost:5000")
        print("• API: http://localhost:8080")
        sys.exit(0)
    else:
        print("⚠️ Some services are not responding.")
        print("💡 Try running: docker-compose up -d")
        print("📋 Then check: docker-compose ps")
        sys.exit(1)

if __name__ == "__main__":
    main()
