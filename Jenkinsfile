def app

pipeline {
    agent any

    stages {
        stage('Lint') {
            steps {
                parallel(
                    "Lint Dockerfile": {
                        sh 'hadolint app-container/Dockerfile'
                    },
                    "Lint Application code": {
                        sh 'pylint app-container/app.py'
                    }
                
                )
                
            }
         }  

        stage('Lint Application Code') {
              steps {
                  
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
                  script{
                    aquaMicroscanner imageName: 'mbilalce/quotes:latest', notCompliesCmd: 'exit 1', onDisallowed: 'fail', outputFormat: 'json'
                  }
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