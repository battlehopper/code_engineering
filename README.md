# Projeto de Demonstração: Observabilidade com Microsserviços e a Stack Grafana

Este projeto foi criado para demonstrar habilidades em observabilidade, DevOps (CI/CD) e Chaos Engineering, utilizando uma arquitetura de microsserviços em Python instrumentada com a stack Grafana (Prometheus, Loki, Tempo). A aplicação simula um fluxo de checkout de e-commerce que pode ser deliberadamente degradado para mostrar o poder da observabilidade na detecção e resolução de problemas.

## Arquitetura

A aplicação consiste em três microsserviços principais e uma stack de observabilidade completa, todos gerenciados via Docker Compose:

-   **Microsserviços:**
    -   `product-service`: Serviço Flask para listar produtos.
    -   `payment-service`: Serviço Flask que processa pagamentos e contém a lógica de **Chaos Engineering**.
    -   `checkout-service`: O orquestrador que lida com a lógica de checkout.

-   **Stack de Observabilidade:**
    -   **Prometheus:** Coleta e armazena métricas.
    -   **Loki:** Coleta e agrega logs de todos os contêineres.
    -   **Tempo:** Coleta e armazena traces distribuídos (APM).
    -   **Grafana:** A interface de visualização para criar dashboards com dados do Prometheus, Loki e Tempo.
    -   **Promtail:** Agente que envia os logs dos contêineres para o Loki.
    -   **Alertmanager:** Gerencia os alertas enviados pelo Prometheus.

---

## Pré-requisitos

-   [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/)

---

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2.  **Construa e inicie os contêineres:**
    ```bash
    docker-compose up --build
    ```
    Aguarde alguns instantes para que todos os serviços iniciem. Você pode acessar as interfaces:
    -   **Grafana:** `http://localhost:3000` (login: admin/admin)
    -   **Prometheus:** `http://localhost:9090`
    -   **Alertmanager:** `http://localhost:9093`

---

## Roteiro da Demonstração

### Passo 1: Operação Normal

Execute uma requisição de checkout bem-sucedida:

```bash
curl -X POST http://localhost:5003/checkout \
-H "Content-Type: application/json" \
-d '{
    "items": [{"product_id": 1, "quantity": 1}],
    "payment_details": {"credit_card": "1234-5678-9012-3456"}
}'
```
Você receberá uma resposta de sucesso.

**No Grafana (`http://localhost:3000`):**
-   Vá para **Explore** e selecione a fonte de dados **Tempo**.
-   Execute uma busca. Você verá um trace para a requisição `/checkout` mostrando a comunicação entre os três serviços (`checkout-service` -> `payment-service`) com baixa latência.

### Passo 2: Ativar o Chaos Engineering

Ative o "modo caos" no `payment-service`:

```bash
curl -X POST http://localhost:5002/chaos/toggle
```
A resposta será: `{"status":"Chaos mode is now enabled"}`.

### Passo 3: Observar o Impacto

Tente fazer o checkout novamente. A requisição levará mais tempo e provavelmente falhará com um erro 500.

**No Grafana:**
-   **Traces (Tempo):** Execute a busca novamente. Você verá traces vermelhos (indicando erro) com duração muito maior. O *flame graph* mostrará a latência no `span` do `payment-service`.
-   **Métricas (Prometheus):** Em **Explore**, use a fonte de dados Prometheus e execute a query `rate(flask_http_requests_total{job="microservices", status="500"}[1m])`. Você verá a taxa de erros aumentar.
-   **Logs (Loki):** Em **Explore**, use a fonte de dados Loki e execute a query `{container="payment-service"}`. Você verá os logs de erro sendo gerados.

### Passo 4: O "Self-Healing" com Alertmanager

Explique como o sistema se recupera automaticamente.

-   **Regra de Alerta do Prometheus:** Mostre o arquivo `prometheus/alert.rules.yml`. Explique que a regra `HighErrorRatePaymentService` calcula se a taxa de erro 500 ultrapassa 25% por mais de 30 segundos.
-   **Alertmanager:** Abra a interface do Alertmanager (`http://localhost:9093`). Após 30 segundos, o alerta do Prometheus aparecerá aqui como "firing".
-   **Webhook:** Mostre o arquivo `alertmanager/config.yml`. Explique que o Alertmanager está configurado para, ao receber este alerta, chamar o webhook `http://payment-service:5002/chaos/toggle`.
-   **Verificação:** Verifique o status do modo caos. Ele terá sido desativado automaticamente.
    ```bash
    curl http://localhost:5002/chaos/status
    ```
    A resposta será: `{"chaos_mode":"disabled"}`.

### Passo 5: Recuperação

Execute o comando de checkout novamente, e ele voltará a funcionar instantaneamente, provando que o sistema se "curou".

---

## CI/CD

Este projeto inclui um pipeline de CI básico configurado com GitHub Actions (`.github/workflows/ci.yml`). A cada push, ele executa um linter (`flake8`) e valida a construção das imagens Docker.
