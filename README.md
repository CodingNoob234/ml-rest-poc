# Introduction
This repository contains a REST API that can receive post requests with data that is used to compute features and return a prediction. As an example, main.ipynb trains a model on the Credit Card Fraud Detection dataset from Kaggle. The model and pre-computed features are stored in pickle so it can be loaded in the REST API. The API supports validation of the input data and using pre-computed features (for example features based on grouped averages for example or historic means).

# Build and Test
Below is described how the applications can be run locally or through container orchestration. For all the descriptions below, requests can be send to localhost:port/api/prediction.

## Running locally
It is generally adviced to use a virtual environment to prevent dependency conflicts. First run the following commands:
- ``` conda create --name my-temporary-env python=3.11.4```
- ``` conda activate my-temporary-env ```
- (removing is done by ``` conda remove my-temporary-env ```)
- ``` pip install -r requirements.txt ```

After making sure all dependencies are installed, the application can be started by running ``` python -m app.main ``` from the root of the project.
(In case an error is thrown related to importing LightGBM, running ``` conda install -c conda-forge lightgbm ``` probably solves the issue).

## Running in Docker
The application can also be run in a container by ``` docker compose up --build ```. 

## Running in Kubernetes Cluster
It is also possible to run the application in a kubernetes cluster. To do so, a list of commands need to be executed from the root of the project. First, make sure you have a local kubernetes cluster running (can be easily achieved with docker desktop or minikube).
- ``` docker build -t ml-api-poc-image:latest . ```
- ``` kubectl apply -f deployment-kubernetes/namespace.yaml ```
- ``` kubectl apply -f deployment-kubernetes/deployment.yaml ```
- ``` kubectl apply -f deployment-kubernetes/service.yaml ```

## Test Call to API
Through all the above methods, the API is reachable for POST requests at http(s)://localhost:31738/api/prediction (port 8000 for local and docker). The test2.ipynb notebook contains an example call to the API. This should work independent of how the application is build (local, docker, kubernetes), but make sure to set the booleans 'local', 'k8' and 'http' correctly.

# Creating Self-Signed Certificates
For creating self signed certificates to enable one-way SSL communcation, execute the following commands:
- ``` cd config ```
- ``` openssl genpkey -algorithm RSA -out key.pem ```
- ``` openssl req -new -key key.pem -out csr.pem ```
- ``` openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out cert.pem ```

# Properties
The application makes use of environment properties. The following table describes all properties that are required for the application to function properly.

| Property      | Default value| Description                                   |
|---------------|--------------|-----------------------------------------------|
| APPLICATION_NAME  | ml-api-poc  | The application name indicated in the logstring             |
| LOG_LEVEL         | INFO           | Logging level of application |
| ENDPOINT          | /prediction           | The endpoint (automatically with /api suffix) |
| LOCAL_MODEL_PATH  | tmp/model_pre_features.pkl | Containing the model instance and precomputed features    |
| SSL_CERTFILE      | /config/cert.pem      | Certfile for one-way SSL                      |
| SSL_KEYFILE       | /config/key.pem       | Keyfile for one-way SSL                       |
| SSL_KEYFILE_PASSWORD | Passw0rd           | Password for Keyfile                          |
| SSL_ENABLED       | False                 | To enable SSL communication                  |

# To-Do
Many things can be improved in this application, such as:
- configure the monitoring of logs through elasticsearch and kibana
- health endpoints (also for auto scaling)
