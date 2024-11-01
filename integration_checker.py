import requests
import csv

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

def check_ci_cd_integration(repo):
    travis_url = f'https://api.github.com/repos/{repo}/contents/.travis.yml'
    response = requests.get(travis_url, headers=HEADERS)
    
    if response.status_code == 200:
        return "Travis CI"

    actions_url = f'https://api.github.com/repos/{repo}/contents/.github/workflows'
    response = requests.get(actions_url, headers=HEADERS)
    
    if response.status_code == 200:
        workflows = response.json()
        if workflows:
            return "GitHub Actions"
    
    return "Nenhuma Integração"

with open('ci_cd_integration.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Repositório', 'Ferramentas de CI/CD Integradas'])

    for repo in repositorios:
        ci_cd_tool = check_ci_cd_integration(repo)
        writer.writerow([repo, ci_cd_tool])

print("CSV atualizado com as informações de CI/CD.")