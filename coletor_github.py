import requests
import csv
from datetime import datetime

# Autenticação via token do GitHub
GITHUB_TOKEN = 'token-github'  # Substitua pelo seu token
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

# Lista de repositórios para monitorar
repositorios = [
    'hyperledger-labs/fablo',
    'hyperledger-labs/fabric-operator',
    'hyperledger-labs/ansible-collection',
    'hyperledger/fabric-samples',
    'hyperledger/fabric-test',
    'hyperledger/bevel',
    'hyperledger/indy-node-container',
    'bcgov/von-network',
    'hyperledger-labs/minifabric',
    'hyperledger-labs/besu-operator',
    'hyperledger-labs/minifabric',
    'hyperledger-labs/nephos',
    'hyperledger-labs/microfab',
    'Consensys/quorum'
]

# Função para coletar a data de criação do repositório
def obter_data_lancamento(repo):
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()['created_at'][:10]  # Retorna apenas a data (YYYY-MM-DD)
    else:
        print(f"Erro ao acessar {repo}: {response.status_code}")
        return None

# Função para coletar commits por mês
def obter_commits_por_mes(repo, data_inicio, data_fim):
    url = f"https://api.github.com/repos/{repo}/commits"
    params = {'since': data_inicio, 'until': data_fim, 'per_page': 100}
    commits_count = 0

    while True:
        response = requests.get(url, headers=HEADERS, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao acessar commits de {repo}: {response.status_code}")
            break

        commits = response.json()

        # Se não houver mais commits, sair do loop
        if not commits:
            break

        commits_count += len(commits)

        # Paginando resultados
        if 'Link' in response.headers:
            links = response.headers['Link']
            if 'rel="next"' in links:
                url = links.split(';')[0][1:-1]  # Pega o URL da próxima página
                params = {}  # Limpa os parâmetros para a próxima página
            else:
                break
        else:
            break

    return commits_count

# Função para coletar releases por mês
def obter_releases_por_mes(repo, data_inicio, data_fim):
    url = f"https://api.github.com/repos/{repo}/releases"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Erro ao acessar releases de {repo}: {response.status_code}")
        return 0

    releases = response.json()
    releases_count = sum(1 for release in releases if data_inicio <= release['published_at'][:10] <= data_fim)
    
    return releases_count

# Função para salvar dados no CSV
def salvar_csv(dados):
    with open('dados_commits_releases.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Repositório', 'Commits', 'Releases'])
        for repo, (commits, releases) in dados.items():
            writer.writerow([repo, commits, releases])

# Executar o script
if __name__ == "__main__":
    mes_usuario = input("Digite o mês (MM) que deseja consultar: ")
    ano_usuario = input("Digite o ano (YYYY) que deseja consultar: ")
    data_usuario = f"{ano_usuario}-{mes_usuario}-01"
    data_fim = f"{ano_usuario}-{mes_usuario}-31"  # Considerando o último dia do mês

    dados_gerais = {}

    for repo in repositorios:
        data_lancamento = obter_data_lancamento(repo)
        if data_lancamento and data_usuario >= data_lancamento:
            commits = obter_commits_por_mes(repo, data_lancamento, data_fim)
            releases = obter_releases_por_mes(repo, data_lancamento, data_fim)
            dados_gerais[repo] = (commits, releases)

    salvar_csv(dados_gerais)
    print("Dados salvos em 'dados_commits_releases.csv'")