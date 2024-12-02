pipeline {
    agent any

    environment {
        // REPO_URL = 'https://github.com/JacksonEVMartin/Trabalho-DevOps-22.6754-0.git'
        REPO_DIR = 'Trabalho-DevOps-22.6754-0'  // Nome do diretório onde o repositório será clonado
    }

    stages {
        stage('Clonando o repositório') {
            steps {
                script {
                  // Clona o repositório diretamente no Jenkins
                  git branch: "main", url: 'https://github.com/JacksonEVMartin/Trabalho-DevOps-22.6754-0.git'
                }
            }
        }

         stage('Subir serviços com Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        // stage('Testar aplicação Flask') {
            // steps {
                // script {
                    // sh 'docker exec flask pytest /app/test_app.py'
                // }
            // }
        // }

    }

    post {
        success {
            echo 'Pipeline concluída com sucesso!'
        }
        failure {
            echo 'Algo deu errado. Verifique os logs para mais informações.'
        }
    }
}
