# Flight Status and Notification App

This is a flight status and notification application. The application will provide real-time flight information to users and allow them to sign up for notifications about flight status changes. The application will be built using a React frontend, a Python backend with Flask, and a PostgreSQL database.

---

## Deploy na Azure

Este projeto está configurado para ser implantado na nuvem da Microsoft Azure, utilizando uma arquitetura moderna e escalável. O deploy é totalmente automatizado através de um pipeline de CI/CD com GitHub Actions.

### Arquitetura na Nuvem

-   **Frontend (React):** A aplicação de frontend é hospedada como um site estático no **Azure Blob Storage**, com o conteúdo distribuído globalmente via **Azure CDN** para baixa latência.
-   **Backend (Python/Flask):** A API do backend é containerizada com Docker e implantada no **Azure Kubernetes Service (AKS)** para alta disponibilidade e escalabilidade.
-   **Banco de Dados (PostgreSQL):** Os dados são armazenados no **Azure Database for PostgreSQL**, um serviço de banco de dados gerenciado que cuida de segurança, backups e escalabilidade.
-   **CI/CD (GitHub Actions):** Um pipeline automatizado gerencia todo o processo de build, teste e deploy tanto do frontend quanto do backend.

### Como Fazer o Deploy

O processo de deploy está dividido em duas etapas principais:

1.  **Provisionamento da Infraestrutura na Azure:**
    Crie todos os recursos necessários (AKS, PostgreSQL, Storage Account, etc.) na sua conta da Azure seguindo as instruções em:
    **[-> Guia de Provisionamento da Infraestrutura na Azure (AZURE_SETUP.md)](AZURE_SETUP.md)**

2.  **Configuração do Pipeline de CI/CD:**
    Configure as credenciais seguras no seu repositório do GitHub para permitir que o pipeline de deploy automatizado se autentique na sua conta da Azure. As instruções estão em:
    **[-> Guia de Configuração dos Segredos do GitHub (GITHUB_SECRETS_SETUP.md)](GITHUB_SECRETS_SETUP.md)**

Após completar estes dois guias e atualizar os placeholders no arquivo de workflow, cada `push` para a branch `main` irá automaticamente construir e implantar a versão mais recente da aplicação na sua infraestrutura da Azure.
