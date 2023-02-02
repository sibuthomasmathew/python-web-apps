# Python web application

A simple python web application based on [flask](https://palletsprojects.com/p/flask/). It includes a workflow that can be executed on a local machine to containerize the application and deploy it to kubernetes.

## Requirements

1. Docker
2. [Minikube](https://minikube.sigs.k8s.io)
3. kubectl CLI
4. [skaffold CLI](https://skaffold.dev/docs/install/#standalone-binary)
5. cURL


## Building container image

1. Clone this repository
    ```bash
    git clone git@github.com:sibuthomasmathew/python-web-apps.git
    ```
2. Go to the directory `application` 
    ```bash
    cd python-web-apps/applications
    ```
3. Build a container image using `docker` CLI
    ```bash
    docker build -t simple-app:v1.0 .
    ```
4. Once the build is complete, verify the presence of the image
    ```bash
    docker image ls simple-app
    ```

## Deploy the application to Kubernetes

The workflow of 

- building a container
- pushing the container image to a repository
- deploying the application to kubernetes

is abstracted by `skaffold`. Run the commands below to bootstrap the environment

1. Ensure the following CLIs are installed
    - minikube
    - kubectl
    - skaffold
2. Start a single node `minikube` cluster
    ```bash
    minikube start --cpus=2 --memory=4g --cni=flannel
    ```
3. Once the cluster is up, ensure `minikube` is the current-context, and access the cluster:
    ```bash
    kubectl get nodes,pods -A
    ```
4. Enable the Nginx ingress controller on `minikube`
    ```bash
    minikube addons enable ingress
    ```
5. Verify `ingress-nginx` controller is up
    ```bash
    kubectl -n ingress-nginx get pods,svc
    ```
6. Go to the base directory where `skaffold.yaml` exist
    ```bash
    cd python-web-apps
    ```
7. Build the container image and deploy the application using `skaffold`
    ```bash
    skaffold run
    ```
8. Capture the Node IP of minikube
    ```bash
    MINIKUBE_IP=$(minikube ip)
    ```
9. Capture the NodePort of `ingress-nginx` controller
    ```bash
    NODEPORT=$(kubectl -n ingress-nginx get svc ingress-nginx-controller -o jsonpath={.spec.ports[0].nodePort})
    ```
10. Test the application by making requests for `time`
    ```bash
    curl -H "Host: demo.adjust.app" $MINIKUBE_IP:$NODEPORT/time
    ```
11. Test the application by making requests for `hostname`
    ```bash
    curl -H "Host: demo.adjust.app" $MINIKUBE_IP:$NODEPORT/hostname
    ```
12. Clean-up the deployment
    ```bash
    skaffold delete
    ```
