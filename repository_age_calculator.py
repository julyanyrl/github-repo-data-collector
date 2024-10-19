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

def salvar_csv_idade(dados_idade):
    with open('repositorios_com_idade.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Repositório", "Data de Criação", "Idade em Meses"])
        for repo, (data_criacao, idade) in dados_idade.items():
            writer.writerow([repo, data_criacao, idade])

if __name__ == "__main__":
    ano_final = int(input("Insira o ano final (ex: 2024): "))
    mes_final = int(input("Insira o mês final (1-12): "))

    dados_idade = {}

    for repo in repositorios:
        data_criacao = obter_data_criacao(GITHUB_TOKEN, repo)
        if data_criacao:
            idade = calcular_idade_em_meses(data_criacao, ano_final, mes_final)
            dados_idade[repo] = (data_criacao, idade)
        else:
            print(f"Erro ao obter dados de {repo}")

    salvar_csv_idade(dados_idade)
    print("CSV gerado com sucesso em 'repositorios_com_idade.csv'.")