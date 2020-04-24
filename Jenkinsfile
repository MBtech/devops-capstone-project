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
            steps{
                script{
                    app = docker.build('mbilalce/quotes', 'app-container/')
                }
                
            }
            
        }

        stage('Security Scan') {
              steps { 
                 aquaMicroscanner imageName: 'mbilalce/quotes:latest', notCompliesCmd: 'exit 1', onDisallowed: 'fail', outputFormat: 'json'
              }
         }              

        stage('Push image') {
            steps{
                script{
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
    }
}