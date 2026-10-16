pipeline {
    agent any

    environment {
        DOCKER_CLI = 'C:\\Users\\Prathamesh\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
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
                bat '"%DOCKER_CLI%" build -t student-task-manager:latest .'
            }
        }

        stage('Deploy') {
            steps {
                bat '"%DOCKER_CLI%" rm -f student-task-manager 2>nul || exit /b 0'
                bat '"%DOCKER_CLI%" run -d --name student-task-manager -p 5000:5000 student-task-manager:latest'
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl.exe --fail --silent --show-error --retry 10 --retry-delay 2 http://localhost:5000/health'
            }
        }
    }
}
