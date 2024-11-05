# GitHub Repo Metrics Collector

Este projeto é uma ferramenta para coletar e analisar métricas de repositórios do GitHub, como o número de commits e releases em um intervalo de datas. Ele permite automatizar a coleta de informações de múltiplos repositórios e exportar os resultados em um arquivo CSV.

## Funcionalidades

- Coleta de dados de commits em repositórios do GitHub em um período específico.
- Coleta de dados de releases de repositórios do GitHub em um período específico.
- Exportação de dados em um arquivo CSV para análise posterior.

## Pré-requisitos

- Python 3.x
- Token de acesso do GitHub (para acessar a API com permissões adequadas)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/meu_projeto.git
   cd meu_projeto
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a variável de ambiente `GITHUB_TOKEN`:**
   - Crie um arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:
     ```plaintext
     GITHUB_TOKEN=seu_token_do_github
     ```

   - **OU** defina a variável de ambiente manualmente:
    ```bash
    export GITHUB_TOKEN=seu_token_do_github  # Linux/macOS
    set GITHUB_TOKEN=seu_token_do_github     # Windows (CMD)
    ```

## Uso

1. **Prepare o arquivo `repositorios.txt`** com os nomes dos repositórios a serem analisados, um por linha:
   ```
   torvalds/linux
   microsoft/vscode
   numpy/numpy
   ```

2. **Execute o script principal:**
   ```bash
   python main.py <data_referencia> <arquivo_repositorios>
   ```

   - `data_referencia`: Data de início no formato `YYYY-MM-DD`.
   - `arquivo_repositorios`: Caminho para o arquivo `.txt` contendo os repositórios.

   **Exemplo de execução:**
   ```bash
   python main.py 2024-11-01 repositorios.txt
   ```

3. **Verifique o diretório `output/`** para encontrar o arquivo CSV gerado:
   ```
   output/relatorio_github_2024-11-01.csv
   ```

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir com melhorias, por favor, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -m 'Adicionei uma nova feature'`).
4. Faça um push para a branch (`git push origin minha-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato:
- Email: seu-email@example.com
- GitHub: [SeuUsuário](https://github.com/SeuUsuário)