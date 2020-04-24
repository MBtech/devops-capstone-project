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

        stage('Build image') {
            steps{
                script{
                    app = docker.build('mbilalce/quotes', 'app-container/')
                }
            }
        }         

        stage('Push image') {
            steps{
                script{
                    docker.withRegistry('', 'docker-hub-credentials') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }

        stage('Deploy on Kubernetes Cluster'){
            steps{
                sh 'kubectl create deployment quotes --image=mbilalce/quotes'
                sh 'kubectl rollout status deployment quotes'
                sh 'kubectl scale --replicas=3 deployment quotes'
                sh 'kubectl expose deployment quotes --type=LoadBalancer --name=quotes-service --port=80'
            }
        }
    }
}