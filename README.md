# Sailnavsim web

## Application Installation

**Installation via `requirements.txt`**:

```shell
$ git clone https://github.com/hackersandslackers/flasklogin-tutorial.git
$ cd flasklogin-tutorial
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```

## Kubernetes stuff.

# Database

Firstly we need to deploy a database. We'll create a single database in the cluster within a `Database` *Namespace*. We'll deploy the database with a *Service* called `mysql` making it accessible on `mysql://mysql.database:3306` - `mysql://<Service>.<Namespace>:<port>`.

```
kubectl create namepace database
kubectl apply -f k8s/deploy-database.yaml -n database
```

# Application

Our application is deployed as a container within a pod by a *Deployment*. The *Pod* is residing inside a *Namespace* along with the *Service* and *Ingress*.

The *Deployment* provides two key bits of information: The image to be deployed and the number of replicas. Kubernetes will maintain the type and number of *Pods* described in the *Deployment* by `spec.replicas` and `spec.template.containers[].image.
 
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sailnavsim-python
spec:
  replicas: 3                                                   # Three pods will be created.
  template:
    spec:
      containers:
        - name: sailnavsim-python
          image: gcr.io/sailnavsim/sailnavsim-python:fdf55b31   # The image name tagged with the git commit sha.
          imagePullPolicy: Always
          envFrom:
          - configMapRef:
              name: environment-variables                       # We get our env vars from here. 
          ports:
          - name: web
            containerPort: 8080                                 # The application is exposed on this port.
          livenessProbe:
            httpGet:
              path: /healthz                                                   
              port: 8080
            initialDelaySeconds: 15
            timeoutSeconds: 15
          readinessProbe:
            httpGet:
              path: /healthz
              port: 8080
            initialDelaySeconds: 5
            timeoutSeconds: 3
```

The *Pods* are ephemeral with temporary ip addresses so we should never try and connect to them directly. We use a *Service* as a discovery mechanism and load balancer. The *Service* discoveres all the pods produced by a deployment and load balances them.

*Ingress* is mapping  
# 
