# Projeto de Demonstração: Observabilidade com Microsserviços e Grafana Cloud

Este projeto demonstra como construir uma aplicação de microsserviços em Python com uma stack de observabilidade de nível de produção, utilizando o **Grafana Cloud** como backend de telemetria e o **Grafana Agent** como coletor.

A aplicação simula um fluxo de checkout de e-commerce e inclui funcionalidades de Chaos Engineering para demonstrar a detecção e resolução de problemas em um ambiente moderno.

## Arquitetura

A arquitetura é dividida em dois componentes principais:

1.  **A Aplicação:**
    -   `product-service`: Serviço Flask para listar produtos.
    -   `payment-service`: Serviço Flask que processa pagamentos e contém a lógica de **Chaos Engineering**.
    -   `checkout-service`: O orquestrador que lida com a lógica de checkout.
    -   Todos os serviços são instrumentados com **OpenTelemetry** (para traces) e **Prometheus client** (para métricas).

2.  **O Coletor de Telemetria:**
    -   **Grafana Agent:** Um único agente leve que coleta métricas, logs e traces da aplicação e os encaminha de forma segura para o Grafana Cloud.
    -   **Grafana Cloud:** A plataforma gerenciada que armazena, correlaciona e visualiza toda a nossa telemetria (métricas, logs e traces) em um único lugar.

---

## Como Começar: Configuração do Grafana Cloud

Antes de executar o projeto (seja localmente ou na nuvem), você precisa de uma conta do Grafana Cloud e de algumas credenciais.

Siga nosso guia detalhado para encontrar todos os endpoints e criar sua chave de API:
**[-> Guia de Configuração do Grafana Cloud (GRAFANA_CLOUD_SETUP.md)](GRAFANA_CLOUD_SETUP.md)**

---

## Opção 1: Execução Local com Docker Compose

Esta é a maneira mais rápida de ver a aplicação funcionando.

1.  **Clone o repositório.**
2.  **Configure suas credenciais:** Renomeie o arquivo `.env.example` para `.env` e preencha com as credenciais que você obteve no guia acima.
3.  **Inicie a aplicação e o agente:**
    ```bash
    docker-compose up --build
    ```
    Isso irá iniciar os 3 microsserviços e o Grafana Agent. O agente começará imediatamente a enviar dados para sua conta do Grafana Cloud.

---

## Opção 2: Deploy no Azure Kubernetes Service (AKS)

Para uma demonstração completa de ponta a ponta, você pode implantar a aplicação em um cluster Kubernetes na Azure.

1.  **Provisione a Infraestrutura na Azure:** Crie seu cluster AKS e o registro de contêiner (ACR) seguindo as instruções em:
    **[-> Guia de Provisionamento da Infraestrutura na Azure (AZURE_SETUP.md)](AZURE_SETUP.md)**

2.  **Instale o Grafana Agent no seu Cluster:** Use o Helm para instalar o Grafana Agent no seu cluster. Este guia contém o comando `helm install` que você precisará preencher com suas credenciais do Grafana Cloud.
    **[-> Guia de Instalação do Grafana Agent com Helm (HELM_SETUP.md)](HELM_SETUP.md)**

3.  **Configure o Pipeline de CI/CD:** Configure as credenciais no seu repositório do GitHub para permitir que o pipeline de deploy automatizado funcione.
    **[-> Guia de Configuração dos Segredos do GitHub (GITHUB_SECRETS_SETUP.md)](GITHUB_SECRETS_SETUP.md)**

Após completar estes passos, cada `push` para a branch `main` irá automaticamente implantar a aplicação no seu cluster AKS.

---

## Roteiro da Demonstração (com Grafana Cloud)

### Passo 1: Operação Normal

Execute uma requisição de checkout bem-sucedida contra seu ambiente (local ou na nuvem).

```bash
# Para o ambiente local
curl -X POST http://localhost:5003/checkout ... (resto do comando)

# Para AKS, use o IP público do seu Ingress
```

**No Grafana Cloud:**
-   Abra sua instância do Grafana Cloud.
-   Vá para **Explore** e selecione a fonte de dados **Tempo**. Você verá o trace da sua requisição, mostrando a comunicação entre os serviços.

### Passo 2: Ativar o Chaos Engineering

Ative o "modo caos" no `payment-service`:
```bash
# Para o ambiente local
curl -X POST http://localhost:5002/chaos/toggle

# Para AKS, você pode usar `kubectl port-forward` para acessar o serviço internamente ou expô-lo temporariamente
```

### Passo 3: Observar o Impacto

Tente fazer o checkout novamente. A requisição ficará lenta e provavelmente falhará.

**No Grafana Cloud:**
-   **Traces (Tempo):** Você verá traces vermelhos e lentos.
-   **Métricas (Prometheus):** Crie um painel ou use o Explore para ver a taxa de erros (`rate(flask_http_requests_total{job="microservices", status="500"}[1m])`).
-   **Logs (Loki):** Explore os logs do `payment-service` para ver as mensagens de erro.

### Passo 4: O "Self-Healing" com Alertas do Grafana Cloud

Explique como o sistema se recupera automaticamente.

-   **Alerta no Grafana Cloud:** Em vez do Alertmanager, você agora criaria o alerta diretamente na interface do Grafana Cloud (em `Alerting`). A regra seria a mesma (taxa de erro > 25%).
-   **Ponto de Contato (Contact Point):** Configure um "Contact Point" do tipo **Webhook** para apontar para o endpoint `/chaos/toggle` da sua aplicação (exposto via Ingress no AKS).
-   **Política de Notificação (Notification Policy):** Crie uma política para enviar os alertas para este webhook.

Quando a taxa de erro aumentar, o Grafana Cloud irá detectar, disparar o alerta e chamar o webhook, "curando" o sistema.
