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
        stage('Unit Tests') { 
            agent {
                dockerfile true
            }
            steps {
                sh 'python3 -m pytest --ignore database_test.py'
            }
        }
        stage('Database Tests') { 
            agent {
                dockerfile true
            }
            steps {
                sh 'systemctl start docker && docker-compose up'
                sh 'python3 -m pytest'
                sh 'docker-compose down'
            }
        }
    }
}
