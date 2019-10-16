pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'mariusgheorghies/pytest'
                    image 'python:latest' 
                }
            }
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
