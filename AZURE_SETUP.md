# Guia de Provisionamento da Infraestrutura na Azure para a Aplicação de Voos

Este guia contém os comandos da Azure CLI para criar a infraestrutura completa para hospedar a aplicação de voos na Azure.

Execute estes comandos no seu terminal com a [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) instalada e logada na sua conta, ou utilize o [Azure Cloud Shell](https://shell.azure.com/).

---

### Passo 1: Definir Variáveis e Criar Senha

Defina as variáveis para os nomes dos seus recursos. Escolha nomes únicos onde for indicado.

```bash
# Substitua os valores abaixo pelos de sua preferência
export RESOURCE_GROUP="flight-app-rg"
export LOCATION="eastus" # Escolha a região da Azure mais próxima de você
export ACR_NAME="flightappacr$(openssl rand -hex 4)" # Nome único para o Container Registry
export AKS_NAME="flight-app-aks"
export POSTGRES_SERVER_NAME="flight-app-pg-server-$(openssl rand -hex 4)" # Nome único para o servidor PostgreSQL
export POSTGRES_DB_NAME="flights_db"
export POSTGRES_ADMIN_USER="pgadmin"
export STORAGE_ACCOUNT_NAME="flightappfrontend$(openssl rand -hex 4)" # Nome único para a conta de armazenamento

# CRIE UMA SENHA SEGURA para o banco de dados e guarde-a.
# O pipeline de CI/CD precisará dela mais tarde.
export POSTGRES_ADMIN_PASSWORD="<YourSecurePassword>"
```

---

### Passo 2: Criar o Grupo de Recursos

```bash
az group create --name $RESOURCE_GROUP --location $LOCATION
```

---

### Passo 3: Criar o Banco de Dados (Azure Database for PostgreSQL)

```bash
az postgres flexible-server create \
    --resource-group $RESOURCE_GROUP \
    --name $POSTGRES_SERVER_NAME \
    --location $LOCATION \
    --admin-user $POSTGRES_ADMIN_USER \
    --admin-password "$POSTGRES_ADMIN_PASSWORD" \
    --sku-name Standard_B1ms --tier Burstable --version 13 --storage-size 32 \
    --public-access 0.0.0.0
```

---

### Passo 4: Criar o Azure Container Registry (ACR)

```bash
az acr create \
    --resource-group $RESOURCE_GROUP \
    --name $ACR_NAME \
    --sku Basic
```

---

### Passo 5: Criar o Cluster do Azure Kubernetes Service (AKS)

**A criação pode levar de 10 a 15 minutos.**

```bash
az aks create \
    --resource-group $RESOURCE_GROUP \
    --name $AKS_NAME \
    --node-count 1 \
    --generate-ssh-keys \
    --attach-acr $ACR_NAME
```

---

### Passo 6: Habilitar o Ingress Controller no AKS

Para que o `Ingress` funcione e exponha nossa API, precisamos habilitar o addon de roteamento de aplicação HTTP.

```bash
az aks enable-addons --resource-group $RESOURCE_GROUP --name $AKS_NAME --addon http_application_routing
```

---

### Passo 7: Criar a Conta de Armazenamento para o Frontend

```bash
# Criar a conta de armazenamento
az storage account create \
    --name $STORAGE_ACCOUNT_NAME \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION \
    --sku Standard_LRS \
    --kind StorageV2

# Habilitar o modo de site estático
az storage blob service-properties update \
    --account-name $STORAGE_ACCOUNT_NAME \
    --static-website \
    --404-document index.html \
    --index-document index.html
```

---

### Passo 8: Conectar `kubectl` ao seu Cluster

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_NAME
```
Verifique a conexão: `kubectl get nodes`

---

Sua infraestrutura na Azure está provisionada.