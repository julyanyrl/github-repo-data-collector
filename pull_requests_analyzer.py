import requests
import csv
from datetime import datetime

GITHUB_TOKEN = 'seu_token'
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'}

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
    'hyperledger-labs/nephos',
    'hyperledger-labs/microfab',
    'Consensys/quorum'
]

def get_pr_statistics(repo, date_limit):
    open_prs = 0
    total_no_response_time = 0
    accepted_prs = 0
    rejected_prs = 0
    page = 1

    while True:
        url = f'https://api.github.com/repos/{repo}/pulls?state=all&per_page=100&page={page}'
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code != 200:
            print(f"Erro ao recuperar PRs do repositório {repo}: {response.status_code}")
            print("Verifique o nome do repositório e o token de autenticação.")
            return 0, 0, 0, 0

        prs = response.json()
        if not prs:
            break

        for pr in prs:
            pr_date = datetime.strptime(pr['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            
            if pr_date > date_limit:
                continue
            
            if pr['state'] == 'open':
                open_prs += 1
                
                if not pr.get('comments', 0):
                    no_response_time = (date_limit - pr_date).days
                    total_no_response_time += no_response_time
            elif pr['merged_at'] is not None and datetime.strptime(pr['merged_at'], "%Y-%m-%dT%H:%M:%SZ") <= date_limit:
                accepted_prs += 1
            elif pr['closed_at'] is not None and pr['merged_at'] is None and datetime.strptime(pr['closed_at'], "%Y-%m-%dT%H:%M:%SZ") <= date_limit:
                rejected_prs += 1

        page += 1

    avg_no_response_time = total_no_response_time / open_prs if open_prs > 0 else 0
    
    return open_prs, avg_no_response_time, accepted_prs, rejected_prs

data_input = input("Digite a data limite para a busca (formato: AAAA-MM-DD): ")
data_limite = datetime.strptime(data_input, "%Y-%m-%d")

with open('pull_requests.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Repositório', 'Quantidade PRs Abertos', 'Tempo Médio Sem Resposta (dias)', 'PRs Aceitos', 'PRs Rejeitados'])

    for repo in repositorios:
        open_prs, avg_no_response_time, accepted_prs, rejected_prs = get_pr_statistics(repo, data_limite)
        writer.writerow([repo, open_prs, avg_no_response_time, accepted_prs, rejected_prs])

print("CSV atualizado com sucesso.")