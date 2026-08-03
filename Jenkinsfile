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

    }
}