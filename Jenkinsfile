pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:latest'
                }
            }
            //steps {
            //    sh 'python -m py_compile Retirement_test.py'
            //}
        }
        stage('Test') { 
            agent {
                docker {
                    image 'python:latest'
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'python3 -m pytest' 
            }
        }
    }
}
