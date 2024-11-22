import requests
from datetime import datetime

def get_pr_statistics(repo, date_limit, github_token):
    headers = {'Authorization': f'token {github_token}'}
    open_prs = accepted_prs = rejected_prs = total_no_response_time = 0
    page = 1

    while True:
        url = f'https://api.github.com/repos/{repo}/pulls?state=all&per_page=100&page={page}'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Erro ao acessar {repo}: {response.status_code}")
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
                comments = requests.get(pr['comments_url'], headers=headers).json()
                no_response_time = (
                    (datetime.strptime(comments[0]['created_at'], "%Y-%m-%dT%H:%M:%SZ") - pr_date).days
                    if comments else (date_limit - pr_date).days
                )
                total_no_response_time += no_response_time

            elif pr['merged_at'] and datetime.strptime(pr['merged_at'], "%Y-%m-%dT%H:%M:%SZ") <= date_limit:
                accepted_prs += 1

            elif pr['closed_at'] and not pr['merged_at'] and datetime.strptime(pr['closed_at'], "%Y-%m-%dT%H:%M:%SZ") <= date_limit:
                rejected_prs += 1

        page += 1

    avg_no_response_time = round(total_no_response_time / open_prs) if open_prs else 0
    return open_prs, avg_no_response_time, accepted_prs, rejected_prs

def main(repos, date_limit, github_token):
    date_limit = datetime.strptime(date_limit, "%Y-%m-%d") if isinstance(date_limit, str) else date_limit
    results = []

    for repo in repos:
        open_prs, avg_no_response_time, accepted_prs, rejected_prs = get_pr_statistics(repo, date_limit, github_token)
        results.append({
            'Repositório': repo,
            'PRs Abertos': open_prs,
            'Tempo Médio Sem Resposta (dias)': avg_no_response_time,
            'PRs Aceitos': accepted_prs,
            'PRs Rejeitados': rejected_prs
        })
    
    return results