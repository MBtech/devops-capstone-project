# Capstone project for Udacity's DevOps nanodegree
This is the repository for the Capstone project for Udacity's DevOps Nanodegree

## Pre-requisites on the Build Server
Instructions for each of these dependencies for Amazon Linux are provided below
- Install Jenkins
- Install hadolint 
- Install pylint using `pip3 install -r requirements.txt`

## Plugins Required for Jenkins
- Blue Ocean
- Docker


## Installation on Amazon AMI
### Jenkins:
sudo yum install java-1.8.0
sudo yum remove java-1.7.0-openjdk
curl --silent --location http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo | sudo tee /etc/yum.repos.d/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins

### Hadolint
wget https://github.com/hadolint/hadolint/releases/download/v1.17.5/hadolint-Linux-x86_64
chmod +x hadolint-Linux-x86_64 
mv hadolint-Linux-x86_64 /usr/local/bin/hadolint

### Install python 3 and pip 3
sudo yum install python35 python35-pip
sudo ln -s /usr/bin/pip-3.5 /usr/bin/pip3
pip3 install pylint

## TroubleShooting on Mac
https://stackoverflow.com/questions/54452082/jenkins-docker-command-not-found-path-setup
https://stackoverflow.com/questions/50333325/jenkins-cannot-run-program-docker-error-2-no-such-file-or-directory
