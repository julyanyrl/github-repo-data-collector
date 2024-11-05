import requests
from datetime import datetime

def get_active_branches(repo, date_limit, github_token):
    headers = {'Authorization': f'token {github_token}'}
    url = f'https://api.github.com/repos/{repo}/branches'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erro ao recuperar branches do repositório {repo}: {response.status_code}")
        print("Verifique o nome do repositório e o token de autenticação.")
        return 0
    
    branches = response.json()
    active_branches = 0
    
    for branch in branches:
        branch_url = branch['commit']['url']
        branch_response = requests.get(branch_url, headers=headers)
        if branch_response.status_code != 200:
            print(f"Erro ao recuperar commit da branch {branch['name']} do repositório {repo}")
            continue

        branch_commit = branch_response.json()
        commit_date = branch_commit['commit']['committer']['date']
        commit_date = datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ")
        
        if commit_date <= date_limit:
            active_branches += 1
    
    return active_branches

def main(repositorios, data_limite, github_token):
    dados_gerais = []
    for repo in repositorios:
        branches_ativas = get_active_branches(repo, data_limite, github_token)
        dados_gerais.append({
            'Repositório': repo,
            'Branches Ativas': branches_ativas
        })
    
    return dados_gerais
