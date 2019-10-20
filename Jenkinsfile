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
                sh 'python3 -m pytest --ignore database_test.py'
            }
        }
        stage('Database Tests') { 
            steps {
                sh 'python3 -m pytest database_test.py'
            }
        }
    }
}
