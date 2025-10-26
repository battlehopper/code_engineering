# Guia de Configuração dos Segredos do GitHub para Deploy na Azure

Para que o workflow do GitHub Actions possa fazer o deploy na sua conta da Azure, ele precisa de credenciais seguras. Vamos criar um **Service Principal** (uma identidade de aplicação) na Azure e fornecer suas credenciais como um segredo no GitHub.

---

### Passo 1: Criar o Service Principal na Azure

Execute o seguinte comando da Azure CLI. Este comando cria uma nova identidade e concede a ela a role `Contributor` (Colaborador) sobre o seu grupo de recursos. A role de Colaborador permite que o GitHub Actions crie e gerencie os recursos necessários.

**Importante:** O output deste comando é um objeto JSON. **Copie o JSON inteiro**, pois você vai precisar dele no próximo passo.

```bash
# Lembre-se de substituir <MyResourceGroup> pelo nome do seu grupo de recursos
# e <MySubscriptionId> pelo ID da sua Assinatura Azure.
# Você pode encontrar o ID da sua assinatura com `az account show --query id -o tsv`

az ad sp create-for-rbac \
    --name "GitHubActionsDeploy" \
    --role "Contributor" \
    --scopes "/subscriptions/<MySubscriptionId>/resourceGroups/<MyResourceGroup>" \
    --sdk-auth
```

O output será algo como:

```json
{
  "clientId": "********-****-****-****-************",
  "clientSecret": "********************************",
  "subscriptionId": "********-****-****-****-************",
  "tenantId": "********-****-****-****-************",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "activeDirectoryGraphResourceId": "https://graph.windows.net/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

---

### Passo 2: Configurar o Segredo no Repositório do GitHub

1.  No seu repositório do GitHub, vá para **Settings** > **Secrets and variables** > **Actions**.
2.  Clique em **New repository secret**.
3.  **Nome do segredo:** Cole exatamente `AZURE_CREDENTIALS`.
4.  **Valor do segredo:** Cole o **objeto JSON completo** que você copiou do output do comando anterior.
5.  Clique em **Add secret**.

---

### Passo 3: Atualizar os Placeholders no Workflow

Finalmente, vá para o arquivo `.github/workflows/ci.yml` e substitua os placeholders no topo do arquivo pelos nomes exatos dos seus recursos na Azure:

```yaml
env:
  ACR_NAME: <SeuNomeDeACR>
  AKS_CLUSTER_NAME: <SeuNomeDeClusterAKS>
  RESOURCE_GROUP: <SeuNomeDeResourceGroup>
```

---

Com isso, seu pipeline de CI/CD está totalmente configurado. Na próxima vez que você fizer um `push` para a branch `main`, o GitHub Actions irá automaticamente construir suas imagens, enviá-las para o seu ACR e implantar a nova versão no seu cluster AKS.