# Guia de Configuração do Grafana Cloud

Este guia mostra onde encontrar as credenciais e endpoints necessários na sua conta do Grafana Cloud para configurar o Grafana Agent.

---

### Passo 1: Fazer Login no Grafana Cloud

Acesse [grafana.com](https://grafana.com/) e faça login na sua conta. Você será direcionado para o seu "Cloud Portal".

---

### Passo 2: Encontrar os Endpoints e User IDs

1.  No menu principal, navegue até a sua **Stack** (geralmente tem um nome como `[seu-usuario]/gcloud`).
2.  Na página da sua Stack, você verá caixas para cada serviço: **Prometheus**, **Loki**, e **Tempo**.
3.  Clique em **"Details"** em cada uma dessas caixas.
4.  Dentro dos detalhes, você encontrará:
    -   **Remote Write URL** (para Prometheus) ou **Endpoint** (para Loki/Tempo): Esta é a URL que o agente usará para enviar dados.
    -   **Username / User:** Este é o ID do usuário para aquele serviço específico.

    Copie esses valores. Você precisará de uma URL e um User ID para cada um dos três serviços.

    -   **Para Loki,** você também precisará do seu **Tenant ID**, que geralmente é o mesmo que o User ID.

    **Exemplos de como os valores se parecem:**
    -   `GCLOUD_PROMETHEUS_REMOTE_WRITE_URL`: `https://prometheus-prod-13-prod-us-east-0.grafana.net/api/prom/push`
    -   `GCLOUD_PROMETHEUS_USER`: `123456`
    -   `GCLOUD_LOKI_URL`: `https://logs-prod-us-east-0.grafana.net/loki/api/v1/push`
    -   `GCLOUD_LOKI_USER`: `789101`
    -   `GCLOUD_TEMPO_URL`: `tempo-prod-us-east-0.grafana.net:443`
    -   `GCLOUD_TEMPO_USER`: `234567`

---

### Passo 3: Criar uma Chave de API (API Key)

O Grafana Agent usará uma única chave de API para se autenticar em todos os serviços.

1.  No menu à esquerda do seu Cloud Portal, clique em **Security** > **API Keys**.
2.  Clique em **"+ Add API Key"**.
3.  Dê um nome para a chave, por exemplo, `grafana-agent-key`.
4.  Na seção **Role**, selecione a role `MetricsPublisher`, `LogsPublisher`, e `TracesPublisher`. Isso garante que a chave tenha as permissões corretas para enviar telemetria.
5.  Clique em **"Create API Key"**.
6.  **IMPORTANTE:** O Grafana mostrará a chave de API **apenas uma vez**. Copie-a imediatamente e guarde-a em um local seguro. Esta será a sua `GCLOUD_API_KEY`.

---

### Passo 4: Preencher os Arquivos

Com todas essas informações em mãos, você pode agora:

1.  **Para o ambiente local:** Criar o arquivo `.env` a partir do `.env.example` e preencher todas as variáveis.
2.  **Para o ambiente Kubernetes:** Usar esses valores para substituir os placeholders no comando `helm install` encontrado no arquivo `HELM_SETUP.md`.

Sua configuração está completa!