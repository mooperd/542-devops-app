#!/bin/bash

export NAMESPACE=andrew
export SERVICE_NAME=andrews_app
export SHORT_SHA=$(git rev-parse --short HEAD)
export BUILD_IMAGE=gcr.io/devops-542/$SERVICE_NAME:$SHORT_SHA

# Authenticate with google services
gcloud container clusters get-credentials cluster-1 --zone europe-west1-b --project devops-542
gcloud auth configure-docker

# Build and push the docker image      
docker build -t $BUILD_IMAGE .
docker push $BUILD_IMAGE

# Deploy the application.

# First create the namespace
cat k8s/namespace.yaml | envsubst
cat k8s/namespace.yaml | envsubst | kubectl apply -f - 

# Create the configmap
cat k8s/configmap.yaml | envsubst
cat k8s/configmap.yaml | envsubst | kubectl apply -n $NAMESPACE -f - 

# Create the deployment
cat k8s/deployment.yaml | envsubst
cat k8s/deployment.yaml | envsubst | kubectl apply -n $NAMESPACE -f -

# Create the service
cat k8s/service.yaml | envsubst
cat k8s/service.yaml | envsubst | kubectl apply -n $NAMESPACE -f -

# Create the ingress 
cat k8s/ingress.yaml | envsubst
cat k8s/ingress.yaml | envsubst | kubectl apply -n $NAMESPACE -f -

