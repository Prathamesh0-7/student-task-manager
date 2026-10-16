pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install Dependencies') {
            steps { bat 'py -m pip install -r requirements.txt' }
        }
        stage('Automated Tests') {
            steps { bat 'py -m unittest discover -s tests -v' }
        }
        stage('Build Docker Image') {
            steps { bat 'docker build -t student-task-manager:latest .' }
        }
        stage('Deploy') {
            steps {
                bat 'docker rm -f student-task-manager 2>nul || exit /b 0'
                bat 'docker run -d --name student-task-manager -p 5000:5000 student-task-manager:latest'
            }
        }
        stage('Health Check') {
            steps {
                bat 'powershell -Command "$ok=$false; for($i=0;$i -lt 15;$i++){try{$r=Invoke-RestMethod http://localhost:5000/health; if($r.status -eq ''healthy''){$ok=$true;break}}catch{};Start-Sleep 2};if(-not $ok){docker logs student-task-manager;exit 1}"'
            }
        }
    }
}
