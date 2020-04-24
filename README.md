# Capstone project for Udacity's DevOps nanodegree
This is the repository for the Capstone project for Udacity's DevOps Nanodegree. 
In this project we will use rolling deployment and the deployment yaml file `quotes.yaml` is configured so that 
during a rolling update a max of 25% can be unavailable. 

The EKS cluster is setup using `amazon-eks-master.template.yaml` file which is based on the [quick-start cloudformation templates
provided by AWS](https://github.com/aws-quickstart/quickstart-amazon-eks). Parameters can be set in `parameters.json`. Small modifications have been made to the aws template so that the Security group for the Bastion host has port 8080 open for any kind of local testing of the kubernetes deployments without using the load balancer. 

## Setup
Install the following pre-requisites on the Build Server. Instructions for each of these dependencies for Amazon Linux are provided [below](#installation-on-amazon-ami)
- Install Jenkins
- Install hadolint 
- Install docker
- Install pylint, flask and numpy using `pip3 install flask pylint numpy`
- Copy kubeconfig file to Jenkin's user directory: 
```
sudo cp ~/.kube/config ~jenkins/.kube/
sudo chown -R jenkins: ~jenkins/.kube/
```

## Running the project
- Start the Kubernetes cluster using: `./create-stack.sh eks-stack amazon-eks-master.template.yaml parameters.json ` 
- Once the kubernetes cluster is setup, start Jenkins and install `Blue Ocean` and `Docker` plugins
- Create docker credentials with ID `docker-hub-credentials` in Jenkins Credentials 
- Create the pipeline using the github repository 
- Build the pipeline and it'll deploy the web app. It takes a couple of minutes for the external load balancer to be up and running
- Service will be available to be accessed at `http://<load-balancer-ip>:80/quote`. The load balancer's external IP can be displayed by using `kubectl get services` on the bastion host

## Installation on Amazon AMI
### Install docker
```
sudo yum -y install docker 
sudo service docker start
sudo chmod 666 /var/run/docker.sock
sudo usermod -a -G docker ec2-user
sudo usermod -a -G docker jenkins
```

### Jenkins:
```
sudo yum install java-1.8.0
sudo yum remove java-1.7.0-openjdk
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins
sudo service jenkins start
```
### Hadolint
```
wget https://github.com/hadolint/hadolint/releases/download/v1.17.5/hadolint-Linux-x86_64
chmod +x hadolint-Linux-x86_64 
mv hadolint-Linux-x86_64 /usr/local/bin/hadolint
```

### Install python 3 and pip 3
```
sudo yum install python35 python35-pip
sudo ln -s /usr/bin/pip-3.5 /usr/bin/pip3
pip3 install pylint
```

## TroubleShooting on Mac
https://stackoverflow.com/questions/54452082/jenkins-docker-command-not-found-path-setup
https://stackoverflow.com/questions/50333325/jenkins-cannot-run-program-docker-error-2-no-such-file-or-directory
