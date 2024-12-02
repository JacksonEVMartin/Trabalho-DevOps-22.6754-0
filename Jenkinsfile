pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/JacksonEVMartin/Trabalho-DevOps-22.6754-0.git'
        REPO_DIR = 'Trabalho-DevOps-22.6754-0'  // Nome do diretório onde o repositório será clonado
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                  echo 'Clonando o repositório...'
                  // Clona o repositório diretamente no Jenkins
                  git brach: "main", url: REPO_URL
                  sh 'docker compose down -v'
                  sh 'docker compose down build'
                }
            }
        }

        // stage('Rodar Testes') {
        //     steps {
        //         echo 'Executando testes com pytest...'
        //         sh '''
        //         cd ${REPO_DIR}/flask
        //         pip install -r requirements.txt
        //         pytest --junitxml=report.xml
        //         '''
        //     }
        //     post {
        //         always {
        //             junit '${REPO_DIR}/flask/report.xml' // Publica relatório de testes no Jenkins
        //         }
        //     }
        // }

        // stage('Build Docker Images') {
        //     steps {
        //         echo 'Construindo imagens Docker...'
        //         sh '''
        //         cd ${REPO_DIR}
        //         docker-compose build
        //         '''
        //     }
        // }

        // stage('Deploy') {
        //     steps {
        //         echo 'Subindo o ambiente com Docker Compose...'
        //         sh '''
        //         cd ${REPO_DIR}
        //         docker-compose up -d
        //         '''
        //     }
        // }

        // stage('Monitoramento') {
        //     steps {
        //         echo 'Verificando o ambiente e serviços...'
        //         sh '''
        //         curl -s http://localhost:5000/ || exit 1
        //         curl -s http://localhost:9090/ || exit 1
        //         curl -s http://localhost:3000/ || exit 1
        //         '''
        //     }
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
