# How to install hadolint
sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64

sudo chmod +x /bin/hadolint


# Quick fix for project 4 cos python 3.7.0 is not supported by some dependences

If you encounter this error after running make install in project 4.
with exit status 1
    [end of output]

     note: This error originates from a subprocess, and is likely not a problem with pip.
    error: legacy-install-failure

    × Encountered error while trying to install package.
    ╰─> numpy

    note: This is an issue with the package mentioned above, not pip.
    hint: See above for output from the failure.
    [end of output]

 note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
make: *** [install] Error 1

I have a quick fix. It works on Ubuntu O.S.
First, the dependencies in requirements.txt works best in python3.7 so you might be having this issue if you are running on an higher python version. I have the following commands to install, set up venv and install the dependencies.
# enter a folder 

$ cd ~/Desktop

# install python 3.7 and needed dependencies
$ sudo apt update

$ sudo apt install software-properties-common

$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt install python3.7

$ sudo apt install python3.7-venv

$ sudo apt install python3.7-distutils

# install pip
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3.7 get-pip.py --user

# confirm your python version - it won't change the default version too
$ python3.7 -V && pip3 -V

# Installing VirtualEnv
$ python3.7 -m pip install virtualenv

# Creating Virtual Environment called devops
$ python3.7 -m virtualenv ~/.devops

# To activate devops venv
source ~/.devops/bin/activate

# Install requirements.txt
(.devops)$ cd /path/to/project/folder

(.devops)$ make install
This worked well for me.

# SAMPLE DOCKERFILE

FROM python:3.7.3-stretch

# Working directory
WORKDIR /app

# Copy source code to working dorectory
COPY . app.py /app/

# Install package form requirements.txt
# Hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Use this tp run docker
$ docker build --tag=app .
$ docker image ls
$ docker run -it app bash


# Run this command to rename the container and the image
$ docker run -it --rm --name my-running-app my-python-app

# Install minikube from here
Follow the guide to install minikube for kubernetes
https://minikube.sigs.k8s.io/docs/start/


# Creating a kubernetes cluster using eksctl
$ eksctl create cluster --name my-cluster --region us-east-1 --nodegroup-name my-nodegroup --node-type t2.medium --nodes 2

------------------OR------------------------------------
How it works?

    Create a basic cluster
    Once you have installed EKSCTL utility, you can create a basic cluster with just one command:

    eksctl create cluster

    A cluster will be created with default parameters, such as:
        An auto-generated name
        Two m5.large worker nodes. Recall that the worker nodes are the virtual machines, and the m5.large type defines that each VM will have 2 vCPUs, 8 GiB memory, and up to 10 Gbps network bandwidth.
        Use the Linux AMIs as the underlying machine image
        Your default region
        A dedicated VPC

# However, you can specify all the above details explicitly, for example:
    eksctl create cluster --name myCluster --nodes=4

    Create an advanced cluster

    If you want to specify a detailed configuration, then you may have to write all the configuration in a separate YAML file, and pass it along with the command:

    eksctl create cluster --config-file=<path>

# To list the details of the cluster, you can use the following command:
    We will not discuss the option above to use configuration files, however, you can have a look at an example here.

    List the details
    List the details about the existing cluster(s)

    eksctl get cluster [--name=<name>][--region=<region>]

# Delete a cluster
    Run a simple command, it will delete the cluster as well as all the associated resources.

    eksctl delete cluster --name=<name> [--region=<region>]

There are many more options while creating a cluster, such as defining the auto-scaling size (min-max number of nodes), and SSH access to the nodes.

# Use this to view the progress of the cluster creation
    eksctl get cluster --name=<name> [--region=<region>]


################## Deploy a Sample App ####################

Let's deploy a sample Python "Hello World" app to the kubernetes cluster.

# Assuming you have already cloned the course repo as
git clone git clone https://github.com/udacity/DevOps_Microservices.git
# Move to the exercise folder if you want to write Dockerfile from scratch
cd DevOps_Microservices/Lesson-3-Containerization/python-helloworld

Once you are in the right folder, run these commands and read the inline comments carefully.

# Ensure Docker Desktop is running locally
docker --version
# Build an image using the Dockerfile in the current directory
docker build -t python-helloworld .
docker images # To see the image you just built
# Run a container
docker run -d -p 5000:5000 python-helloworld
# Check the output at http://localhost:5000/ or http://0.0.0.0:5000/ or http://127.0.0.1:5000/
docker ps
# Now, stop the container.
# Tag locally before pushing to the Dockerhub
# We have used a sample Dockerhub profile /lowry09
# Replace sudkul/ with your Dockerhub profile
docker tag python-helloworld lowry09/python-helloworld:v1.0.0
docker images
# Log into the Dockerhub from your local terminal
docker login
# Replace sudkul/ with your Dockerhub profile
docker push sudkul/python-helloworld:v1.0.0
# Check the image in your Dockerhub online at https://hub.docker.com/repository/docker/lowry09/python-helloworld

Once your Docker image is publicly available, you can deploy it to the kubernetes cluster.

# Assuming the Kubernetes cluster is ready
kubectl get nodes
# Deploy an App from the Dockerhub to the Kubernetes Cluster
kubectl create deploy python-helloworld --image=lowry09/python-helloworld:v1.0.0
# See the status
kubectl get deploy,rs,svc,pods
# Port forward 
kubectl port-forward pod/python-helloworld-84857d9565-2598m --address 0.0.0.0 5000:5000

Access the app locally at http://127.0.0.1:5000/

# Grab your application logs for your pod (given a pod named my-pod) by running this 
command: kubectl logs my-pod
