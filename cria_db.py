# ================================================
#        Importar pacotes
# ================================================

import csv
import os
from datetime import datetime, timezone, timedelta

# ================================================
#        Adicionar mensagem
# ================================================

def adicionar_dados_mensagem():
    
    ano = ""
    mes = ""
    dia = ""
    horas = ""
    minutos = ""
    segundos = "0"

    while True:
        
        try:
            if ano == "":
                ano = int (input("Digite o ano: "))

            elif mes == "":
                mes = int(input("Digite o número do mês: "))
            
            elif dia == "":
                dia = int(input("Digite o dia do mês: "))

            elif horas == "":
                horas = int(input("Digite as horas do dia: "))

            elif minutos == "":
                minutos = int(input("Digite os minutos da hora: "))

            elif segundos == "":
                segundos = int(input("Digite os segundos dos minutos: "))

        except ValueError:
            print("# ================================================")
            print("Dados incorretos.")
            print("")
            print("")
            print("")
            print("# ================================================")
            input("Aperte Enter para continuar")
            limpar_tela()
            continue
        if ano != "" and mes != "" and dia != "" and horas != "" and minutos != "" and segundos != "":
            print("# ================================================")
            print("Dados completos.")
            print("")
            print("")
            print("")
            print("Aperte Enter para continuar.")
            limpar_tela()
            break
    
    name_id = cria_name_id(ano, mes, dia, horas, minutos, segundos)

    dia_semana = pega_dia_semana(ano, mes, dia)

    dados_mensagem = {}
    dados_mensagem[name_id] = {
        "Ano": ano,
        "Mês": mes,
        "Dia": dia,
        "Dia da Semana": dia_semana,
        "Horas": horas,
        "Minutos": minutos,
        "Segundos": segundos
        }

    return dados_mensagem, name_id

# ================================================
#        Salvar mensagem
# ================================================

def salvar_dados_mensagem(dados_mensagem, name_id):

    while True:
            
        # Carregar arquivo
        try:
            caminho_arquivo_csv = input("Digite o caminho do arquivo csv: ")
        except ValueError:
            print("Caminho Incorreto!!!")

        if caminho_arquivo_csv != "":
            break

    dados_arquivo = carregar_dados_csv(caminho_arquivo_csv)

    # Verifica o name_id para ver se a mensagem ja está no banco de dados
    if name_id in dados_arquivo:
        # Se sim não faz nada
        print("# ================================================")
        print("Mensagem ja salva no banco de dados")
        print("")
        print("")
        print("")
        input("Aperte Enter para continuar")
        limpar_tela()

    sub_dados = dados_mensagem[name_id]

    sub_dados["Name ID"] = {"Name ID": name_id}
    # Se não esta no arquivo vamos adicionar
    dados_arquivo[name_id] = {
            "Name ID": sub_dados["Name ID"],
            "Ano": sub_dados["Ano"],
            "Mês": sub_dados["Mês"],
            "Dia": sub_dados["Dia"],
            "Dia da Semana": sub_dados["Dia da Semana"],
            "Horas": sub_dados["Horas"],
            "Minutos": sub_dados["Minutos"],
            "Segundos": sub_dados["Segundos"]
        }
    print(f"Adicionando o Name ID '{name_id}' ao arquivo.")

    salvar_em_csv(dados_mensagem, caminho_arquivo_csv)

    print("# ================================================")
    print("Mensagem Salva!!!")
    print("")
    print("")
    print("")
    input("Aperte Enter para continuar.")
    limpar_tela()

    menu_principal()


# ================================================
#        Cria Name ID da mensagem
# ================================================

def cria_name_id(ano, mes, dia, horas, minutos, segundos):
    name_id = "datatime.datatime(" + str(ano) + ", " + str(mes) + ", " + str(dia) + ", " + str(horas) + ", " + str(minutos) + ", " + str(segundos) + ", tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600)))"

    return name_id

# ================================================
#        Função que "pega" o dia da semana
# ================================================

def pega_dia_semana(ano, mes, dia):

    data = datetime(ano, mes, dia)
    dia_semana = data.weekday()

    # Converte o dia_semana no nome do dia da semana
    nomes_dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado", "Domingo"]
    nome_dia_semana = nomes_dias[dia_semana]

    return nome_dia_semana

# ================================================
#        Função gerais
# ================================================    

# Detecta o sistema operacional para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para carregar os dados do arquivo CSV em um dicionário
def carregar_dados_csv(caminho_arquivo_csv):
    try:
        # Abre o arquivo CSV para leitura
        with open(caminho_arquivo_csv, mode='r', newline='', encoding='utf-8') as arquivo:
            lendo = csv.DictReader(arquivo)
            # Converte os dados em um dicionário onde a chave é o "Name ID"
            dados = {linha["Name ID"]: linha for linha in lendo}
        return dados
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}

# Função para salvar os dados no arquivo CSV
def salvar_em_csv(dados_mensagem, caminho_arquivo_csv):
    # Define os cabeçalhos das colunas
    cabecalhos = ["Name ID", "Ano", "Mês", "Dia", "Dia da Semana", "Horas", "Minutos", "Segundos"]
    
    # Abre o arquivo CSV para escrita
    with open(caminho_arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=cabecalhos)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados
        writer.writerows(dados_mensagem.values())

# ================================================
#        Menu Principal
# ================================================

def menu_principal():
    print("# ================================================")
    print("Digite:")
    print("1, para adicionar dados de uma nova mensagem.")
    print("2, para visualizar ultimas mensagens.")
    print("")
    print("")
    print("")
    print("0, para sair.")
    print("")
    print("")
    print("")
    print("# ================================================")
    

    try:
        escolha = int(input("Digite: "))
    except ValueError:
        print("Opção Incorreta!!!")
        input("Aperte Enter para continuar")
        limpar_tela()
        return
    return escolha
# ================================================
#        Função pricipal
# ================================================

def main():

    escolha = menu_principal()

    if escolha == 0:
        return
    
    elif escolha == 1:
        dados_mensagem, name_id = adicionar_dados_mensagem()
        sub_dados = dados_mensagem[name_id]

        print("# ================================================")
        print("Confira os dados e aperte o Enter:")
        print("")
        print("")
        print("")
        print("# ================================================")
        print(f"Name ID: {name_id}.")
        print(f"Ano: {sub_dados["Ano"]}.")
        print(f"Mês: {sub_dados["Mês"]}.")
        print(f"Dia: {sub_dados["Dia"]}.")
        print(f"Dia da Semana: {sub_dados["Dia da Semana"]}.")
        print(f"Horas: {sub_dados["Horas"]}.")
        print(f"Minutos: {sub_dados["Minutos"]}.")
        print(f"Segundos: {sub_dados["Segundos"]}.")
        print("# ================================================")
        input("Aperte o Enter para continuar")

        # Salvando dados em um arquivo csv
        salvar_dados_mensagem(dados_mensagem, name_id)


main()