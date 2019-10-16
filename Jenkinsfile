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
                sh 'sudo pip install -U pytest'
                sh 'python3 -m pytest'
            }
        }
    }
}
