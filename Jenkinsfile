pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/SvZhdanovich/test.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest
                '''
            }
        }
    }
    post {
        always {
            junit '/test-reports/*.xml'
            archiveArtifacts artifacts: '/logs/*.log', allowEmptyArchive: true
        }
    }
}