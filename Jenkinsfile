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
                sh 'python -m py_compile Retirement_test.py'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest'
                    image 'python:latest'
                }
            }
            steps {
                sh 'python3 -m pytest' 
            }
        }
    }
}
