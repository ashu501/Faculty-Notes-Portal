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

        stage('Syntax Check') {
            steps {
                bat '"C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" -m py_compile app.py'
            }
        }
        stage('Run Flask App') {
            steps {
               bat 'start "" "C:\\Users\\aceec\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe" app.py'
            }
        }

    }
}