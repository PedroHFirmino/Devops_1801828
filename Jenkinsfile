pipeline {
    agent any
    environment {
        REPOSITORY_URL = 'https://github.com/PedroHFirmino/Devops_1801828'
        BRANCH_NAME = 'dev'
    }
    stages {
        stage('Baixar código do Git') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPOSITORY_URL}" //Clonar o repositório do Git.
            }
        }
        stage('Rodar Testes') {
            steps {
                script {
                    
                    sh 'docker compose run --rm test' //Rodar os testes com o pytest.
                }
            }
        }
        stage('Build e Deploy') {
            steps {
                script {
                    // Construir as imagens Docker
                    sh '''
                        docker compose build 
                    '''
                    // Subir os containers do Docker com Docker-Compose
                    sh '''
                        docker compose up -d
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline executada com sucesso!'
        }
        failure {
            echo 'Falha ao executar a pipeline.'
        }
    }
}