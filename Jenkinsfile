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
                sh 'sudo service docker start'
                echo 'docker1'
                sh 'docker-compose up'
                echo 'docker2'
                sh 'python3 -m pytest --ignore database_test.py'
                echo 'docker3'
                sh 'docker-compose down'
                echo 'docker4'
                sh 'sudo service docker stop'
            }
        }
    }
}
