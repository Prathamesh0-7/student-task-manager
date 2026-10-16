pipeline {
    agent any

    environment {
        PATH+DOCKER = 'C:\\Users\\Prathamesh\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Automated Tests') {
            steps {
                bat 'py -m unittest discover -s tests -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker.exe build -t student-task-manager:latest .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker.exe rm -f student-task-manager 2>nul || exit /b 0'
                bat 'docker.exe run -d --name student-task-manager -p 5000:5000 student-task-manager:latest'
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl.exe --fail --silent --show-error --retry 10 --retry-delay 2 http://localhost:5000/health'
            }
        }
    }
}
