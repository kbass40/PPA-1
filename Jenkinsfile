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
                // sh '/usr/local/bin/docker-compose up'
                sh 'python3 -m pytest --ignore database_test.py'
                // sh 'docker-compose down' 
            }
        }
    }
}
