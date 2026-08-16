pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/i-karsikaroutray/employee-management-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-management-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f employee-app || true'
                sh 'docker run -d -p 5000:5000 --name employee-app --env-file /home/ubuntu/employee-management-cicd/.env employee-management-app'
            }
        }
    }
}
