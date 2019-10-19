pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:latest'
                }
            }
            steps {
                echo 'Inital build'
            }
        }
        stage('Test') { 
            agent {
                dockerfile true
            }
            steps {
                sh 'sudo service docker start && docker-compose up -d'
                sh 'python3 -m pytest'
                sh 'docker-compose down' 
            }
        }
    }
}
