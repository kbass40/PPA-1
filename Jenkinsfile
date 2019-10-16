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
                sh 'python3 -m pytest' 
            }
        }
    }
}
