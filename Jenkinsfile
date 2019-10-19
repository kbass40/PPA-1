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
                sh 'sudo service docker start'
                sh '/usr/local/bin/docker-compose up'
                sh 'python3 -m pytest'
                sh '/usr/local/bin/docker-compose down'
            }
        }
    }
}
