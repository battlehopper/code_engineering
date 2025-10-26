# Guia de Instalação da Stack de Observabilidade com Helm

Este guia contém os comandos para instalar Prometheus, Grafana, Loki e Tempo no seu cluster AKS usando o Helm.

**Pré-requisito:** Você precisa ter o [Helm](https://helm.sh/docs/intro/install/) instalado no seu terminal.

---

### Passo 1: Adicionar os Repositórios de Charts do Helm

Primeiro, vamos adicionar os repositórios que contêm os "pacotes" (charts) que precisamos.

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

---

### Passo 2: Instalar o kube-prometheus-stack

Este chart é a maneira mais fácil de instalar o Prometheus e o Grafana de forma integrada. Ele já vem com dashboards e regras de alerta pré-configurados para monitorar o próprio cluster Kubernetes.

Vamos instalá-lo usando o arquivo `prometheus-helm-values.yml` que criamos para que ele também colete métricas dos nossos serviços.

```bash
# Criar um namespace para a stack de monitoramento
kubectl create namespace monitoring

# Instalar o chart no namespace 'monitoring'
helm install prometheus-stack prometheus-community/kube-prometheus-stack \
    --namespace monitoring \
    -f prometheus-helm-values.yml
```

---

### Passo 3: Instalar o Loki e o Promtail (loki-stack)

Este chart irá instalar o Loki (servidor de logs) e o Promtail (agente de coleta de logs) em todos os nós do seu cluster.

```bash
helm install loki grafana/loki-stack \
    --namespace monitoring
```

---

### Passo 4: Instalar o Tempo

Finalmente, vamos instalar o Tempo para o tracing distribuído.

```bash
helm install tempo grafana/tempo \
    --namespace monitoring
```

---

### Passo 5: Acessar o Grafana

Após alguns minutos, todos os componentes estarão rodando. O Grafana instalado por este chart não é exposto publicamente por padrão. Use o port-forward do `kubectl` para acessá-lo:

1.  **Encontre a senha do Grafana:**
    ```bash
    kubectl get secret --namespace monitoring prometheus-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
    ```

2.  **Abra o port-forward em um novo terminal:**
    ```bash
    kubectl port-forward --namespace monitoring svc/prometheus-stack-grafana 3000:80
    ```

3.  **Acesse o Grafana:** Abra `http://localhost:3000` no seu navegador. Use o usuário `admin` e a senha obtida no passo 1. As fontes de dados para Prometheus, Loki e Tempo já estarão configuradas!

---

Com estes passos, sua stack de observabilidade estará rodando e coletando dados do seu cluster e dos seus microsserviços assim que eles forem implantados.