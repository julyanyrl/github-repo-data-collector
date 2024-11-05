import requests
from datetime import datetime

def calcular_idade_em_meses(data_criacao, ano_final, mes_final):
    data_criacao_dt = datetime.strptime(data_criacao, '%Y-%m-%dT%H:%M:%SZ')
    data_final_dt = datetime(ano_final, mes_final, 1)

    if data_final_dt < data_criacao_dt:
        return "Erro: Data anterior à criação."
    
    idade_em_meses = (data_final_dt.year - data_criacao_dt.year) * 12 + (data_final_dt.month - data_criacao_dt.month)
    return idade_em_meses if idade_em_meses >= 1 else 0

def obter_data_criacao(token, repo):
    url = f"https://api.github.com/repos/{repo}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    return response.json().get('created_at') if response.status_code == 200 else None

def main(repositorios, data_referencia, github_token):
    ano_final, mes_final, _ = map(int, data_referencia.split('-'))
    dados_idade = []

    for repo in repositorios:
        data_criacao = obter_data_criacao(github_token, repo)
        if data_criacao:
            idade = calcular_idade_em_meses(data_criacao, ano_final, mes_final)
            dados_idade.append({
                'Repositório': repo,
                'Data de Criação': data_criacao,
                'Idade em Meses': idade
            })
        else:
            print(f"Erro ao obter dados de {repo}")

    return dados_idade
