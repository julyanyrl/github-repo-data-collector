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

def get_active_branches(repo, date_limit):
    url = f'https://api.github.com/repos/{repo}/branches'
    
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Erro ao recuperar branches do repositório {repo}: {response.status_code}")
        print("Verifique o nome do repositório e o token de autenticação.")
        return 0
    
    branches = response.json()
    active_branches = 0
    
    for branch in branches:
        branch_url = branch['commit']['url']
        branch_response = requests.get(branch_url, headers=HEADERS)
        branch_commit = branch_response.json()

        commit_date = branch_commit['commit']['committer']['date']
        commit_date = datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ")
        
        if commit_date <= date_limit:
            active_branches += 1
    
    return active_branches

data_input = input("Digite a data limite para a busca (formato: AAAA-MM-DD): ")
data_limite = datetime.strptime(data_input, "%Y-%m-%d")

with open('repositorios.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Repositório', 'Branches Ativas'])

    for repo in repositorios:
        branches_ativas = get_active_branches(repo, data_limite)
        writer.writerow([repo, branches_ativas])

print("CSV atualizado com sucesso.")