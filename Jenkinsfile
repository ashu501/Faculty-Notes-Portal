pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Version') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Create Database') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" create_db.py'
            }
        }

        stage('Syntax Check') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t faculty-notes-portal .'
            }
        }

        stage('Archive Files') {
            steps {
                archiveArtifacts artifacts: 'uploads/**', allowEmptyArchive: true
            }
        }

    }
}