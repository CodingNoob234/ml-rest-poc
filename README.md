# Introduction 
This repository contains a REST api that can receive post request with data, that it uses to predict a fraudulent transaction. This application is aimed to provide a proof-of-concept and is related to ml-model-poc. There the model is trained and the necessary functions for feature engineering are packaged from there.

# Build and Test
Below is described how the applications can be run locally or through container orchestration. For all below build descriptions, requests can be send to localhost:8000/api/prediction.

## Running locally
It is generally advices to use a virtual environment to prevent dependency conflicts. If this is desired, first run the following commands:
- ``` conda create --name my-temporary-env python=3.11.4```
- ``` conda activate my-temporary-env ```
Removing the environment is done by:
- ``` conda remove my-temporary-env ```
The required dependencies are installed through:
``` pip install -r requirements.txt ```
After making sure all dependencies are installed, the application can be started by running ``` python -m app.main ``` in the root of the project.
(In case an error is thrown related to importing LightGBM, running ``` conda install -c conda-forge lightgbm ``` probably solves the issue).

## Running in Docker
The application can also be run in a container by ``` docker compose up --build ```. 

## Running in Minikube kubernetes cluster
To mimic the Azure environment as much as possible, the application can be run in a locally managed kubernetes cluster as well. To do so, a list of commands need to be executed from the root of the project.
- ``` minikube start ```
- ``` eval $(minikube -p minikube docker-env) ```
- ``` docker build -t ml-api-poc-image:latest . ```
- ``` kubectl apply -f namespace.yaml ```
- ``` kubectl apply -f deployment.yaml ```
- ``` kubectl apply -f service.yaml ```
- ``` kubectl apply -f ingress.yaml ```
- ``` kubectl port-forward service/ml-api-poc-service 8000:8000 -n ml-api-t ```

## Test Call to API
Through all the above methods, the API is reachable for POST requests at http(s)://localhost:8000/api/prediction. Data processing 
The test2.ipynb notebook contains an example call to the ML api. This should work independent of how the application is build (local, docker, kubernetes).

# Creating Self-Signed Certificates
For creating self signed certificates to enable one-way SSL communcation, execute the following commands:
- ``` cd config ```
- ``` openssl genpkey -algorithm RSA -out key.pem ```
- ``` openssl req -new -key key.pem -out csr.pem ```
- ``` openssl x509 -req -days 365 -in csr.pem -signkey key.pem -out cert.pem ```

# Properties
The application makes use of environment properties, partially to fully enable CI/CD development. In the following table the properties described that are required for the application to function properly.

| Property      | Default value| Description                                   |
|---------------|--------------|-----------------------------------------------|
| APPLICATION_NAME  | ml-api-poc  | The application name indicated in the logstring             |
| LOG_LEVEL         | INFO           | Logging level of application |
| ENDPOINT          | /prediction           | The endpoint (automatically with /api suffix) |
| LOCAL_MODEL_PATH  | tmp/model_pre_features.pkl | Containing the model instance and precomputed features    |
| SSL_CERTFILE      | /config/cert.pem      | Certfile for one-way SSL                      |
| SSL_KEYFILE       | /config/key.pem       | Keyfile for one-way SSL                       |
| SSL_KEYFILE_PASSWORD | Passw0rd           | Password for Keyfile                          |
| SSL_ENABLED       | False                 | To disable SSL communication                  |