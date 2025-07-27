
# Lesson 3: Practical Case-Study (Building the MLOps Cycle)

## Goal
Integrate the components from Lesson 2 into an automated CI/CD pipeline, focusing on local process automation.

## Main Tools
- GitHub Actions for orchestration
- Docker for execution

## Lesson Structure

### 1. Case-Study Presentation & Goal (30 min)
- Review the "mini-project": model and web API.
- Define the goal: "Create a workflow that, with every code change, tests, trains, registers in local MLflow, and builds a new Docker image."

### 2. Building the Local CI/CD Pipeline (2h)
- **Concept:** CI/CD applies even in local environments. Automation is the goal.
- **Hands-on:** Build the GitHub Actions workflow step by step.

#### Step 1: CI (Continuous Integration)
- Pipeline is triggered by git push.
- Jobs: code checkout, install dependencies, run basic tests (linting, unit tests).

#### Step 2: Automated Training & Registration (CT - Continuous Training)
- Jobs: If CI passes, a new job runs the training script. Local MLflow generates artifacts.

#### Step 3: Build Artifact
- Jobs: After training, build a new Docker image with the trained model.

### 3. Running & Testing the Full Cycle (30 min)
- Demonstrate the cycle: MLflow server, code change, git push, CI/CD pipeline, manual Docker image run, endpoint test.
- Discuss "Deployment" and advanced automation (Kubernetes/K3s).

---

Suggested Folder Structure:
```
aula3_case_study/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── notebooks/
│   └── tracking_mlflow.ipynb
├── src/
│   └── train_model.py
├── docker/
│   └── Dockerfile
│   └── requirements.txt
├── api/
│   └── app.py
├── README.md
```
