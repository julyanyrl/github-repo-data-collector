# github-repo-data-collector

Este projeto consiste em cinco scripts Python:

1. **coletor_github.py**: Monitora o número de commits e releases em repositórios do GitHub, permitindo analisar a atividade de desenvolvimento.
2. **repository_age_calculator.py**: Calcula o tempo de existência de repositórios do GitHub em meses, desde a data de criação até um mês e ano fornecidos. O objetivo é permitir a comparação da maturidade entre diferentes projetos ao longo do tempo. Os resultados são salvos em arquivos CSV.
3. **active_branches_collector.py**: Recupera a quantidade de branches ativas em repositórios do GitHub até uma data específica, fornecendo uma métrica da atividade de desenvolvimento e do interesse em novas funcionalidades. Os resultados também são salvos em um arquivo CSV.
4. **pull_requests_analyzer.py**: Analisa o nível de colaboração em projetos do GitHub, registrando a quantidade de Pull Requests abertos, o tempo médio sem resposta e o número de PRs aceitos e rejeitados até uma data específica.
5. **integration_checker.py**: Verifica se os repositórios possuem integração com ferramentas de Continuous Integration/Continuous Delivery (CI/CD), como GitHub Actions ou Travis CI, e salva os resultados em um arquivo CSV.

## Funcionalidades

### Monitoramento de Commits e Releases

- Coleta informações sobre o número de commits e releases em repositórios do GitHub.
- Permite que o usuário especifique um mês e um ano para consultar as atividades desses repositórios.
- Salva os dados em um arquivo CSV com o nome do repositório, o número de commits e o número de releases.

### Cálculo da Idade dos Repositórios

- Calcula a idade dos repositórios em meses, a partir da data de criação até um mês e ano finais específicos.
- Verifica se a data fornecida é anterior à criação do repositório e exibe uma mensagem de erro apropriada.
- Salva os resultados em um arquivo CSV com o nome do repositório, a data de criação e a idade em meses.

### Contagem de Branches Ativas

- Recupera a quantidade de branches ativas em repositórios do GitHub até uma data fornecida pelo usuário.
- Ignora branches criadas após a data especificada.
- Salva os resultados em um arquivo CSV com o nome do repositório e a contagem de branches ativas.

### Análise de Pull Requests

- Coleta informações sobre Pull Requests abertos, calculando o tempo médio sem resposta e o número de PRs aceitos ou rejeitados até uma data específica.
- Salva os resultados em um arquivo CSV com o nome do repositório, quantidade de PRs abertos, tempo médio sem resposta (em dias), PRs aceitos e PRs rejeitados.

### Verificação de Integração com CI/CD

- Identifica se os repositórios têm integração com ferramentas de CI/CD, como GitHub Actions ou Travis CI.
- Salva os resultados em um arquivo CSV com o nome do repositório e as ferramentas de CI/CD integradas. Caso não haja integração, registra "Nenhuma Integração" na coluna correspondente.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/github-repo-data-collector.git

2. Instale as dependências necessárias:
  ```bash
   pip install requests
```

3. Substitua o token do GitHub nos scripts: No arquivo **coletor_github.py**, **repository_age_calculator.py**, **active_branches_collector.py**, **pull_requests_analyzer.py** e **integration_checker.py**, substitua o valor da variável ```token``` pelo seu token pessoal do GitHub, que é necessário para acessar a API do GitHub.

4. Execute o script de monitoramento:
  ```bash
python coletor_github.py
```
*Durante a execução, você será solicitado a inserir o mês (MM) e o ano (YYYY) para consultar.*

5. Execute o script de cálculo da idade:
  ```bash
python repository_age_calculator.py
```
*Durante a execução, você será solicitado a inserir o ano final (YYYY) e o mês final (MM) para calcular a idade dos repositórios.*

6. Execute o script de contagem de branches ativas:
  ```bash
python active_branches_collector.py
```
*Durante a execução, você será solicitado a inserir a data limite (AAAA-MM-DD) para contar as branches ativas.*

7. Execute o script para análise de Pull Requests:

  ```bash
python pull_requests_analyzer.py
```
*Durante a execução de cada script, você será solicitado a inserir a data limite no formato adequado para a busca de dados.*

8. Execute o script para verificar a integração com CI/CD:
  ```bash
python integration_checker.py
```
*Durante a execução, o script verifica automaticamente a integração de CI/CD nos repositórios especificados e salva os resultados no arquivo CSV.*

### Configurando o Token do GitHub

Para que os scripts funcionem corretamente, você precisará fornecer um token pessoal do GitHub. Esse token deve ter permissões de leitura para repositórios públicos (e, se necessário, privados). Veja os passos para gerar o token:

1. Vá até as configurações de tokens pessoais do GitHub.
2. Clique em "Generate new token" e selecione as permissões necessárias.
4. Copie o token e cole no lugar da variável ```token``` nos scripts.

### Exemplo de Saída
Após a execução dos scripts, os seguintes arquivos CSV serão gerados:

1. dados_commits_releases.csv:
  ```bash
Repositório,Commits,Releases
hyperledger-labs/fablo,1547,9
hyperledger-labs/fabric-operator,99,18
hyperledger-labs/ansible-collection,116,1
...
```

2. repositorios_com_idade.csv:
  ```bash
Repositório,Data de Criação,Idade em Meses
hyperledger-labs/fablo,2019-11-29T11:01:59Z,59
hyperledger-labs/fabric-operator,2022-06-07T18:16:42Z,28
hyperledger-labs/ansible-collection,2023-02-21T16:43:19Z,20
...
```

3. repositorios.csv:
  ```bash
Repositório,Branches Ativas
hyperledger-labs/fablo,3
hyperledger-labs/fabric-operator,5
hyperledger-labs/ansible-collection,4
...
```

4. pull_requests.csv:
  ```bash
Repositório,Quantidade PRs Abertos,Tempo Médio Sem Resposta (dias),PRs Aceitos,PRs Rejeitados
hyperledger-labs/fablo,1,25.0,27,2
hyperledger-labs/fabric-operator,5,172.2,22,3
hyperledger-labs/ansible-collection,0,0,25,5
...
```

5. ci_cd_integration.csv:
  ```bash
Repositório,Ferramentas de CI/CD Integradas
hyperledger-labs/fablo,GitHub Actions
hyperledger-labs/fabric-operator,GitHub Actions
...
```

## Observações
- Se a data final fornecida for anterior à criação do repositório, o script exibirá uma mensagem de erro.
- Repositórios com menos de um mês serão registrados como "0" no campo "Idade em Meses".
- Para obter o tempo médio sem resposta de PRs, são considerados apenas PRs abertos sem comentários.
- Repositórios sem integração com CI/CD serão registrados como "Nenhuma Integração" no arquivo CSV.
