# Guia de Instalação do Grafana Agent no Kubernetes com Helm

Este guia contém os comandos para instalar o **Grafana Agent** no seu cluster AKS. O agente irá coletar métricas, logs e traces e enviá-los para a sua conta do Grafana Cloud.

**Pré-requisito:** Você precisa ter o [Helm](https://helm.sh/docs/intro/install/) instalado no seu terminal.

---

### Passo 1: Adicionar o Repositório de Charts do Grafana

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

---

### Passo 2: Preparar as Credenciais do Grafana Cloud

Você precisará das mesmas credenciais que usou para o ambiente local. Tenha em mãos:
-   A URL de Remote Write do seu Prometheus.
-   O User ID do seu Prometheus.
-   A URL do seu Loki.
-   O User ID do seu Loki.
-   A URL do seu Tempo.
-   O User ID do seu Tempo.
-   Sua chave de API do Grafana Cloud.

---

### Passo 3: Instalar o Helm Chart do Grafana Agent

Vamos instalar o chart usando o comando `helm install`. Usaremos várias flags `--set` para injetar suas credenciais e endpoints diretamente no comando. O Helm irá criar um `Secret` do Kubernetes para armazená-las de forma segura.

**Copie o comando abaixo para um editor de texto e substitua todos os placeholders `<...>` pelos seus valores reais.**

```bash
# Crie um namespace para o agente
kubectl create namespace grafana-agent

# Comando de instalação do Helm
helm install grafana-agent grafana/grafana-agent \
--namespace grafana-agent \
--set controller.replicas=1 \
--set agent.mounts.dockerSock=true \
--set logs.configs[0].scrapeConfigs[0].docker_sd_configs[0].host="unix:///var/run/docker.sock" \
--set metrics.prometheus.remote_write[0].url=<GCLOUD_PROMETHEUS_REMOTE_WRITE_URL> \
--set metrics.prometheus.remote_write[0].basic_auth.username=<GCLOUD_PROMETHEUS_USER> \
--set 'metrics.prometheus.remote_write[0].basic_auth.password'=<GCLOUD_API_KEY> \
--set logs.loki.url=<GCLOUD_LOKI_URL> \
--set logs.loki.basic_auth.username=<GCLOUD_LOKI_USER> \
--set 'logs.loki.basic_auth.password'=<GCLOUD_API_KEY> \
--set traces.tempo.remote_write.endpoint=<GCLOUD_TEMPO_URL> \
--set traces.tempo.remote_write.basic_auth.username=<GCLOUD_TEMPO_USER> \
--set 'traces.tempo.remote_write.basic_auth.password'=<GCLOUD_API_KEY>
```

---

### Passo 4: Verificar a Instalação

Após alguns minutos, verifique se os pods do Grafana Agent estão rodando no namespace `grafana-agent`:

```bash
kubectl get pods -n grafana-agent
```

Você deverá ver pods como `grafana-agent-*` e `grafana-agent-logs-*` com o status `Running`.

---

Com este passo, seu cluster Kubernetes agora está enviando toda a telemetria (métricas do cluster, logs dos pods, etc.) para o Grafana Cloud. A única coisa que falta é garantir que os traces da *nossa aplicação* sejam enviados para o agente. Faremos isso na próxima etapa.