import requests

def check_ci_cd_integration(repo, github_token):
    headers = {'Authorization': f'token {github_token}'}

    # Verifica a presença de arquivo de configuração do Travis CI
    travis_url = f'https://api.github.com/repos/{repo}/contents/.travis.yml'
    response = requests.get(travis_url, headers=headers)
    
    if response.status_code == 200:
        return "Travis CI"

    # Verifica a presença de workflows do GitHub Actions
    actions_url = f'https://api.github.com/repos/{repo}/contents/.github/workflows'
    response = requests.get(actions_url, headers=headers)
    
    if response.status_code == 200:
        workflows = response.json()
        if workflows:
            return "GitHub Actions"
    
    return "Nenhuma Integração"

def main(repositorios, github_token):
    dados_gerais = []
    for repo in repositorios:
        ci_cd_tool = check_ci_cd_integration(repo, github_token)
        dados_gerais.append({
            'Repositório': repo,
            'Ferramentas de CI/CD Integradas': ci_cd_tool
        })

    return dados_gerais
