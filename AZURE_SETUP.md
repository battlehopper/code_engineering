# Guia de Provisionamento de Infraestrutura na Azure

Este guia contém os comandos da Azure CLI necessários para criar a infraestrutura base para o deploy da nossa aplicação no Azure Kubernetes Service (AKS).

Execute estes comandos no seu terminal com a [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) instalada e logada na sua conta, ou utilize o [Azure Cloud Shell](https://shell.azure.com/).

---

### Passo 1: Definir Variáveis

Para facilitar, vamos definir algumas variáveis. Escolha nomes únicos para seus recursos e uma localização (região) da Azure.

```bash
# Substitua os valores abaixo pelos de sua preferência
RESOURCE_GROUP="<MyResourceGroup>"
ACR_NAME="<MyUniqueContainerRegistryName>"
AKS_NAME="<MyAKSClusterName>"
LOCATION="<EastUS>" # Ex: EastUS, WestEurope, BrazilSouth
```

---

### Passo 2: Criar o Grupo de Recursos (Resource Group)

Um grupo de recursos é um contêiner lógico para agrupar os recursos da Azure.

```bash
az group create --name $RESOURCE_GROUP --location $LOCATION
```

---

### Passo 3: Criar o Azure Container Registry (ACR)

O ACR é um registro Docker privado onde armazenaremos as imagens dos nossos microsserviços.

```bash
az acr create \
    --resource-group $RESOURCE_GROUP \
    --name $ACR_NAME \
    --sku Basic \
    --admin-enabled true
```

---

### Passo 4: Criar o Cluster do Azure Kubernetes Service (AKS)

Agora, vamos criar o cluster Kubernetes. Este comando provisiona um cluster com um pool de nós Linux, habilitado para se conectar ao ACR que criamos.

**Atenção:** A criação do cluster pode levar vários minutos (10-15 min).

```bash
az aks create \
    --resource-group $RESOURCE_GROUP \
    --name $AKS_NAME \
    --node-count 1 \
    --generate-ssh-keys \
    --attach-acr $ACR_NAME
```
O argumento `--attach-acr $ACR_NAME` cuida automaticamente de conceder as permissões necessárias para que o cluster AKS possa baixar imagens do seu ACR.

---

### Passo 5: Conectar `kubectl` ao seu Cluster AKS

Após a criação do cluster, você precisa configurar sua ferramenta de linha de comando do Kubernetes (`kubectl`) para se conectar a ele.

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_NAME
```

---

### Passo 6: Verificar a Conexão

Verifique se `kubectl` está conectado corretamente ao seu novo cluster.

```bash
kubectl get nodes
```

Você deverá ver o nó (ou nós) do seu cluster AKS com o status `Ready`.

---

Com estes passos, sua infraestrutura na Azure está pronta para receber a aplicação.

---

### Passo Opcional, mas Recomendado: Habilitar o Ingress Controller

Para expor nossa aplicação à internet via um Ingress, você precisa habilitar o addon de *HTTP application routing* ou instalar um Ingress Controller como o NGINX. O addon é mais simples para começar.

```bash
az aks enable-addons --resource-group $RESOURCE_GROUP --name $AKS_NAME --addon http_application_routing
```