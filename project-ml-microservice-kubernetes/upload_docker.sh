#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
# dockerpath=<your docker ID/path>
dockerpath=lowry09/ml-kubernetes:v1.0.1

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag ml-microservice-kubernetes $dockerpath
docker login

# Step 3:
# Push image to a docker repository
docker push $dockerpath
