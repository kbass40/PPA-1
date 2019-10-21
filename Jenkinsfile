pipeline {
    agent any
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
                echo 'Run unit tests'
                sh 'python3 -m pytest --ignore database_test.py --ignore api_test.py'
            }
        }
        stage('Database Tests') { 
            agent {
                dockerfile true
            }
            steps {
                echo 'Run database tests'
                sh 'python3 -m pytest database_test.py'
            }
        }
        stage('Flask app Tests') {
            agent {
                dockerfile true
            }
            steps {
                echo 'Run flask app tests'
                sh 'python3 -m pytest api_test.py'
            }
        }
    }
}
