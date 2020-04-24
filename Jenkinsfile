def app

pipeline {
    agent any

    stages {
        stage('Lint Dockerfile') {
              steps {
                  sh 'hadolint app-container/Dockerfile'
              }
         }  
        stage('Lint Application Code') {
              steps {
                  sh 'pylint app-container/app.py'
              }
         }

        stage('Build image') {

            app = docker.build("mbilalce/quotes")
        }

        stage('Security Scan') {
              steps { 
                 aquaMicroscanner imageName: 'mbilalce/quotes:latest', notCompleted: 'exit 1', onDisallowed: 'fail'
              }
         }              

        stage('Push image') {
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                app.push("${env.BUILD_NUMBER}")
                app.push("latest")
            }
        }
    }
}