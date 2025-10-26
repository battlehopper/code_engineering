# Guia de Configuração dos Segredos do GitHub para Deploy na Azure

Para que o workflow do GitHub Actions possa fazer o deploy na sua conta da Azure, ele precisa de credenciais seguras. Vamos criar um **Service Principal** na Azure e configurar os segredos necessários no repositório do GitHub.

---

### Segredo 1: Credenciais da Azure (`AZURE_CREDENTIALS`)

Este segredo permite que o GitHub Actions se autentique na sua conta da Azure para gerenciar recursos.

#### Passo 1.1: Criar o Service Principal na Azure

Execute o seguinte comando da Azure CLI. Ele cria uma identidade de aplicação com a role `Contributor` sobre o seu grupo de recursos, o que é suficiente para o pipeline.

**Importante:** O output deste comando é um objeto JSON. **Copie o JSON inteiro**, pois você vai precisar dele.

```bash
# Lembre-se de substituir <MyResourceGroup> pelo nome do seu grupo de recursos
# e <MySubscriptionId> pelo ID da sua Assinatura Azure.
# Você pode encontrar o ID da sua assinatura com `az account show --query id -o tsv`

az ad sp create-for-rbac \
    --name "GitHubActionsFlightApp" \
    --role "Contributor" \
    --scopes "/subscriptions/<MySubscriptionId>/resourceGroups/<MyResourceGroup>" \
    --sdk-auth
```

O output será um objeto JSON parecido com este:
```json
{
  "clientId": "...",
  "clientSecret": "...",
  "subscriptionId": "...",
  "tenantId": "...",
  ...
}
```

#### Passo 1.2: Configurar o Segredo no GitHub

1.  No seu repositório do GitHub, vá para **Settings** > **Secrets and variables** > **Actions**.
2.  Clique em **New repository secret**.
3.  **Nome:** `AZURE_CREDENTIALS`
4.  **Valor:** Cole o **objeto JSON completo** que você copiou.
5.  Clique em **Add secret**.

---

### Segredo 2: Senha do Banco de Dados (`POSTGRES_PASSWORD`)

Este segredo armazena a senha do seu banco de dados PostgreSQL para que o pipeline possa se conectar a ele e rodar as migrações.

1.  No mesmo menu de segredos do GitHub, clique em **New repository secret**.
2.  **Nome:** `POSTGRES_PASSWORD`
3.  **Valor:** Cole a senha segura que você definiu para o seu banco de dados no arquivo `AZURE_SETUP.md`.
4.  Clique em **Add secret**.

---

### Passo Final: Atualizar os Placeholders no Workflow

Finalmente, vá para o arquivo `.github/workflows/deploy.yml` e substitua os placeholders no topo da seção `env:` pelos nomes exatos dos seus recursos na Azure:

```yaml
env:
  ACR_NAME: "<SeuNomeDeACR>"
  STORAGE_ACCOUNT_NAME: "<SeuNomeDeContaDeArmazenamento>"
  POSTGRES_SERVER_NAME: "<SeuNomeDeServidorPostgreSQL>"
```

Com isso, seu pipeline de CI/CD está totalmente configurado e pronto para rodar.