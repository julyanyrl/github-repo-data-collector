import requests

def obter_data_lancamento(repo, github_token):
    headers = {'Authorization': f'token {github_token}'}
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['created_at'][:10]
    else:
        print(f"Erro ao acessar {repo}: {response.status_code}")
        return None

def obter_commits_por_mes(repo, data_inicio, data_fim, github_token):
    headers = {'Authorization': f'token {github_token}'}
    url = f"https://api.github.com/repos/{repo}/commits"
    params = {'since': data_inicio, 'until': data_fim, 'per_page': 100}
    commits_count = 0

    while True:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Erro ao acessar commits de {repo}: {response.status_code}")
            break

        commits = response.json()

        if not commits:
            break

        commits_count += len(commits)

        if 'Link' in response.headers:
            links = response.headers['Link']
            if 'rel="next"' in links:
                url = links.split(';')[0][1:-1]
                params = {}
            else:
                break
        else:
            break

    return commits_count

def obter_releases_por_mes(repo, data_inicio, data_fim, github_token):
    headers = {'Authorization': f'token {github_token}'}
    url = f"https://api.github.com/repos/{repo}/releases"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Erro ao acessar releases de {repo}: {response.status_code}")
        return 0

    releases = response.json()
    releases_count = sum(1 for release in releases if data_inicio <= release['published_at'][:10] <= data_fim)
    
    return releases_count

def main(data_referencia, repositorios, github_token):
    data_fim = f"{data_referencia[:8]}31"
    dados_gerais = []

    for repo in repositorios:
        data_lancamento = obter_data_lancamento(repo, github_token)
        if data_lancamento and data_referencia >= data_lancamento:
            commits = obter_commits_por_mes(repo, data_lancamento, data_fim, github_token)
            releases = obter_releases_por_mes(repo, data_lancamento, data_fim, github_token)
            dados_gerais.append({
                'Repositório': repo,
                'Commits': commits,
                'Releases': releases
            })

    return dados_gerais
