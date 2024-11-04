import sys
import pandas as pd
from scripts.commit_release_collector import main as commit_release_collector
from scripts.active_branches_collector import main as active_branches_collector
from scripts.integration_checker import main as integration_checker
from scripts.pull_requests_analyzer import main as pull_requests_analyzer
from scripts.repository_age_calculator import main as repository_age_calculator
import os
from datetime import datetime
from dotenv import load_dotenv  # Se estiver usando python-dotenv

# Carregar variáveis de ambiente do arquivo .env (opcional)
load_dotenv()

# Define o diretório onde os arquivos CSV serão salvos
OUTPUT_DIR = "output"

def main(data_referencia, arquivo_repositorios):
    # Obtém o token do GitHub do ambiente
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        raise EnvironmentError("Erro: A variável de ambiente 'GITHUB_TOKEN' não foi definida.")

    # Leitura dos repositórios a partir do arquivo .txt
    try:
        with open(arquivo_repositorios, 'r') as file:
            repositorios = [linha.strip() for linha in file if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo_repositorios} não foi encontrado.")
        sys.exit(1)

    # Converte a data de referência para datetime
    data_limite = datetime.strptime(data_referencia, "%Y-%m-%d")

    # Coleta de dados de commits e releases
    print("Executando coleta de dados de commits e releases do GitHub...")
    dados_commits_releases = commit_release_collector(data_referencia, repositorios, github_token)

    # Coleta de dados de branches ativas
    print("Executando coleta de branches ativas do GitHub...")
    dados_branches = active_branches_collector(repositorios, data_limite, github_token)

    # Coleta de dados de integração CI/CD
    print("Executando verificação de integração de CI/CD...")
    dados_ci_cd = integration_checker(repositorios, github_token)

    # Coleta de dados de pull requests
    print("Executando análise de pull requests...")
    dados_pull_requests = pull_requests_analyzer(repositorios, data_limite, github_token)

    # Coleta de dados de idade dos repositórios
    print("Calculando a idade dos repositórios...")
    dados_repository_age = repository_age_calculator(repositorios, data_referencia, github_token)

    # Criação dos DataFrames a partir dos dados coletados
    df_commits_releases = pd.DataFrame(dados_commits_releases)
    df_branches = pd.DataFrame(dados_branches)
    df_ci_cd = pd.DataFrame(dados_ci_cd)
    df_pull_requests = pd.DataFrame(dados_pull_requests)
    df_repository_age = pd.DataFrame(dados_repository_age)

    # Mesclagem dos DataFrames com base no repositório
    df_merged = pd.merge(df_commits_releases, df_branches, on='Repositório', how='outer')
    df_merged = pd.merge(df_merged, df_ci_cd, on='Repositório', how='outer')
    df_merged = pd.merge(df_merged, df_pull_requests, on='Repositório', how='outer')
    df_merged = pd.merge(df_merged, df_repository_age, on='Repositório', how='outer')

    # Criação do diretório de saída, se não existir
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Adiciona um timestamp ao nome do arquivo de saída
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"relatorio_github_{data_referencia}_{timestamp}.csv")

    # Salvando os dados no arquivo CSV
    df_merged.to_csv(output_file, index=False)
    print(f"Arquivo CSV gerado com sucesso: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <data_referencia> <arquivo_repositorios>")
        sys.exit(1)

    data_referencia = sys.argv[1]
    arquivo_repositorios = sys.argv[2]
    main(data_referencia, arquivo_repositorios)
