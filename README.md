# GitHub Repo Age Analyzer

Este projeto consiste em um script Python que calcula o tempo de existência de repositórios do GitHub em meses, desde sua data de criação até um mês e ano fornecidos. O objetivo é permitir a comparação da maturidade entre diferentes projetos ao longo do tempo. Os resultados são salvos em um arquivo CSV.

## Funcionalidades

- Calcula a idade de repositórios em meses, a partir da data de criação até uma data específica.
- Verifica se a data fornecida é anterior à criação do repositório e exibe uma mensagem de erro apropriada.
- Salva os resultados em um arquivo CSV com o nome do repositório, a data de criação e a idade em meses.

## Como Usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/github-repo-age-analyzer.git
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install requests
    ```

3. Substitua o token do GitHub no script:
    No arquivo principal, substitua o valor da variável `token` com seu [token pessoal do GitHub](https://github.com/settings/tokens), que é necessário para acessar a API do GitHub.

4. Execute o script:
    ```bash
    python script.py
    ```

5. **Insira o ano e mês finais quando solicitado**: Durante a execução do script, você será solicitado a inserir o ano e o mês finais para o cálculo da idade dos repositórios.

## Configurando o Token do GitHub

Para que o script funcione corretamente, você precisará fornecer um token pessoal do GitHub. Esse token deve ter permissões de leitura para repositórios públicos (e, se necessário, privados). Veja os passos para gerar o token:

1. Vá até as [configurações de tokens pessoais do GitHub](https://github.com/settings/tokens).
2. Clique em "Generate new token" e selecione as permissões necessárias.
3. Copie o token e cole no lugar da variável `token` no script.

## Exemplo de Saída

Após a execução do script, um arquivo CSV será gerado, contendo os seguintes dados:

   ```bash
Repositório,Data de Criação,Idade em Meses
hyperledger-labs/fablo,2019-11-29T11:01:59Z,59
hyperledger-labs/fabric-operator,2022-06-07T18:16:42Z,28
hyperledger-labs/ansible-collection,2023-02-21T16:43:19Z,20
...
```

## Observações

- Se a data final fornecida for anterior à criação do repositório, o script exibirá uma mensagem de erro.
- Repositórios com menos de um mês serão registrados como "0" no campo "Idade em Meses".
