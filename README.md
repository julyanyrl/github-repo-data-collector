# github-repo-data-collector

Este script em Python permite monitorar a quantidade de commits e releases em repositórios do GitHub em um determinado mês e ano. Os dados coletados são salvos em um arquivo CSV para fácil análise.

## :computer: Como Funciona

- *Autenticação*: O script utiliza um token de autenticação do GitHub para acessar a API. Você deve substituir o valor da variável GITHUB_TOKEN pelo seu próprio token.

- *Lista de Repositórios*: O script possui uma lista predefinida de repositórios a serem monitorados. Você pode adicionar ou remover repositórios nessa lista para personalizar a monitoração.

### Coleta de Dados:

1. O usuário insere um mês e um ano.
2. O script obtém a data de lançamento de cada repositório.
3. Se o repositório foi criado antes do mês e ano solicitados, ele coleta:
   - *Commits*: O número de commits realizados entre a data de lançamento e o final do mês especificado.
   - *Releases*: O número de releases publicadas no mesmo período.
4. *Salvar Dados*: Os dados são salvos em um arquivo CSV chamado dados_commits_releases.csv.

## :gear: Requisitos

- Python 3.x
- Biblioteca requests
- Biblioteca csv (incluída por padrão no Python)

## :rocket: Como Usar

1. Clone o repositório ou copie o código para um arquivo Python (ex: monitor.py).

2. Instale a biblioteca requests, se ainda não estiver instalada:

   ```bash
   pip install requests
Abra o arquivo Python e substitua o valor de GITHUB_TOKEN pelo seu token de autenticação do GitHub.
Para acessar repositórios privados e públicos, siga estas etapas:

1. Acesse GitHub.
2. Vá para Configurações (Settings) > Desenvolvedor (Developer settings) > Tokens de acesso pessoal (Personal access tokens).
3. Clique em Gerar novo token (Generate new token).
4. Adicione uma descrição para o token e selecione as permissões necessárias:
    - **repo** (acesso completo a repositórios privados e públicos).
5. Após criar o token, copie-o e cole na variável GITHUB_TOKEN no seu script.
6. Salve o arquivo e execute o script como descrito na seção Como Usar.
  
**O arquivo CSV gerado terá a seguinte estrutura:**
    
  ```bash
Repositório,Commits,Releases
hyperledger-labs/fablo,30,9
hyperledger-labs/fabric-operator,30,18.
...
```

A API do GitHub tem limites de taxa, então evite executar o script muitas vezes em um curto período. Se algum repositório não for encontrado, o script exibirá um erro apropriado.
