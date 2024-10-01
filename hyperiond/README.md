# Django Project Setup

This guide explains how to build and run the Django application using a virtual environment (`venv`) and Docker.

## Prerequisites

- Python 3.x
- Docker
- Git

## 1. Setup using Virtual Environment (`venv`)

### Step 1: Clone the Repository

First, clone the repository:

```bash
git clone https://github.com/Sebaks1/CapstoneDjango1.git
cd your-repo-directory

# Create a virtual environment
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate


# Install pip
# Create requirements.txt
pip install -r requirements.txt

# Run the Django application to check if the installagions were successful
python manage.py migrate
python manage.py runserver

# The application should run on http://127.0.0.1:8000/. if the installations 
# are successful

# Step 1: Setup Docker
# Download Docker from the Docker homepage if using Windows or macOS, for linux use:
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Check if Docker is working:
docker --version

# Step 2: Pull Docker Image from Repository
# Pull the Docker image from the Docker Hub repository using:
docker pull sebaks1/CapstoneDjango1:latest

# Step 3:Run Docker Container Locally using:
docker run -d -p 8000:8000 sebaks1/CapstoneDjango1

# Step 4:Build and Run the Docker Image Locally 
# Build the Docker image using: 
docker build -t CapstoneDjango1 .

# Run the Docker container using: 
docker run -d -p 8000:8000 capstonedjango1

# Step 5: Stop the Container using its ID
docker stop <container_id>

# Step 6: Push Docker Image to Docker Hub
docker tag capstonedjango1 sebaks1/capstonedjango1:latest
docker push sebaks1/capstonedjango1:latest



