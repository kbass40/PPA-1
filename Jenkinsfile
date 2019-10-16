pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}
