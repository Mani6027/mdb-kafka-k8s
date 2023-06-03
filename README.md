# mdb-kafka-k8s
This repository contains a comprehensive setup and configuration for integrating MongoDB, Kafka using Kubernetes(k8s). It provides a streamlined solution for efficiently synchronizing data between MongoDB and Kafka within a Kubernetes using minikube environment. The setup includes deployment manifests, configuration files, and documentations links.

## Installation Steps

Follow the steps to up minikube and run mongodb with kafka connect.

- First we need minikube to be running in our local machine. For that
  
         - Download binary from here - https://github.com/kubernetes/minikube/releases
         - chmod +x <minikube-binary-name>
         - sudo mv <minikube-binary-name> /usr/local/bin/minikube
         - minikube start
         - minikube status

      Minikube should be up and running by now. If you are facing any issues just go back and check whether you have missed anything.

- Now we have minikube running, we can start with installing mongodb community operator.
  
- ``Note: We are using mongodb community operator to setup mongodb locally.``
- To install mongodb community operator

  - git clone git@github.com:mongodb/mongodb-kubernetes-operator.git
  - Follow the steps in the doc to install community operator on your cluster
    - https://github.com/mongodb/mongodb-kubernetes-operator/blob/master/docs/install-upgrade.md
  - Follow the steps to install custom resource for mongo operator.
    - https://github.com/mongodb/mongodb-kubernetes-operator/blob/master/docs/deploy-configure.md
  - Follow the steps to change username and password of your mongo app
    - https://github.com/mongodb/mongodb-kubernetes-operator/blob/master/docs/users.md
  - Once done, check whether your mongo operator is running inside your cluster.
    - kubectl get pods
- Now you will see there are 4 pods are running on your node, this is because the default configuration will be set to 4. We can reduce it to 3.
- We have mongodb up and running on the local cluster, now we are going to test it.
- To make it easier, minikube has built-in dashboard which we can use to see the metrics of our local cluster.
- Through this dashboard we are going to shell into example-mongodb pods and check whether primary and secondary are running.
  - choose your namespace from the dropdown and scroll down to pods.
  - click on the three dots(vertical dot) choose `exec`. Now you are into shell.
    - Execute - `mongod` you can see the pod state there. Primary or Secondary.
- We are ready to install kafka connect now,
  - Install, `mongo-source-connector` from this repo by executing `kubect apply -f mongo-source-connector`
  - Build docker image of stremzi connector for kafka. Before that, execute `eval $(minikube docker-env)` to get docker images from your machine.
  - Now, build docker image.
  - Apply kubernetes files one by one.
    - `kubectl apply -f kafka-connect.yml`
    - `kubectl apply -f kafaka-ui-svc.yml`
    - `kubectl apply -f kafaka-ui-deployment.yml`
  - We will be using flask-app to insert data in mongodb.
  - You can install flask app from this repo by applying the respective yml file. This is just an sample To-Do app, if you want to connect with your own app just deploy the app inside the same namespace. And use you local mongo connection string.
#
### We are done with the installation part. Now we can check 
  - Port forward mongo and flask app first to see the result. 
    - `kubectl port-forward <your-pod-name> <local-port>:<remote-port>`

🎉It's done.  
  

 

