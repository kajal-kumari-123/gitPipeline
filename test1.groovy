pipeline {
    agent any

    stages {
        stage('') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Testing Stage') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Deployment Stage') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
