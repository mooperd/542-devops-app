#!/bin/bash

## First we need to put together some environment variables.
# The namespace is derived from the git branch name. We use this to namespace Kubernetes and our database. 
# It must be a DNS compliant string so t might be nessisary to sanitise this if you're using funny characters in your branch names.
export NAMESPACE=$(git rev-parse --abbrev-ref HEAD)

# This is the name of our service. Ideally this should be the name of the repo.
export SERVICE_NAME=andrews-app

# Git commit short sha for the end of the docker tag 
export SHORT_SHA=$(git rev-parse --short HEAD)

# This is the docker tag. This tag is the address of where we will push the docker image after build.
export BUILD_IMAGE=gcr.io/devops-542/$SERVICE_NAME:$SHORT_SHA

# The top level domain of our application.
export TLD=devops-wizard.com

# The hostname of the deployment. e.g. https://<branch_name>.<domain>/ 
export HOSTNAME=$NAMESPACE.$TLD

# the name of the SSL certificate that we want to use. 
# This certificate must already be deployed into the kubernetes cluster using the ssl/lets-encrypt.sh script. 
export CERT_NAME=wildcard-${TLD/./-}

# Application secrets. Hopefully self explanitary.
export SECRET_KEY=test1234

# Please note that the database is also namespaces so that each deployment gets its own instance of the database.
export MYSQL_SCHEMA=${NAMESPACE/-/_}_${SERVICE_NAME/-/_}
export MYSQL_HOST=mysql.database
export MYSQL_USER=root
export MYSQL_PWD=password
export SQLALCHEMY_DATABASE_URI=mysql+pymysql://$MYSQL_USER:$MYSQL_PWD@$MYSQL_HOST/$MYSQL_SCHEMA


# Authenticate with google services. We need our CLI to be logged in with google before these will work.
gcloud container clusters get-credentials cluster-1 --zone europe-west1-b --project devops-542
gcloud auth configure-docker --quiet

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

# Horrible hacky cludge to copy ssl certs from default namespace. There used to be a nice kubectl option to do this but they depriciated it. The bastards.
kubectl get secret $CERT_NAME -o json \
| jq 'del(.metadata["namespace","creationTimestamp","resourceVersion","selfLink","uid"])' \
| kubectl apply -n $NAMESPACE -f -
kubectl rollout status deployment/$SERVICE_NAME -n $NAMESPACE
