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
    
    andar = ""
    ano = ""
    mes = ""
    dia = ""
    horas = ""
    minutos = ""
    segundos = "0"

    while True:
        
        try:
            if andar == "":
                andar = int(input("Digite o andar: "))

            elif ano == "":
                ano = int(input("Digite o ano: "))

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
        if andar != "" and ano != "" and mes != "" and dia != "" and horas != "" and minutos != "" and segundos != "":
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
        "Name ID": name_id,
        "Andar": andar,
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
    caminho_arquivo_csv = "/home/marcos/VScode/elevador_info/data_base/data_base.csv"
    
    # Carrega os dados existentes do arquivo CSV
    names_ids_arquivo = def_names_ids_arquivo(caminho_arquivo_csv)
    
    # Se os dados_arquivo for vazio, passa para o proximo passo
    if len(names_ids_arquivo) != 0:

        # Verifica se o name_id já existe no arquivo
        for name in names_ids_arquivo:
            if name_id == name:
                print("# ================================================")
                print("Mensagem já salva no banco de dados.")
                print("")
                input("Aperte Enter para continuar.")
                limpar_tela()
                return

    # Adiciona a nova mensagem ao dicionário
    sub_dados = dados_mensagem[name_id]
    dados_para_salvar = {}
    dados_para_salvar[name_id] = {
        "Name ID": name_id,
        "Andar": sub_dados["Andar"],
        "Ano": sub_dados["Ano"],
        "Mês": sub_dados["Mês"],
        "Dia": sub_dados["Dia"],
        "Dia da Semana": sub_dados["Dia da Semana"],
        "Horas": sub_dados["Horas"],
        "Minutos": sub_dados["Minutos"],
        "Segundos": sub_dados["Segundos"]
    }

    # Salva os dados atualizados no arquivo CSV
    salvar_em_csv(dados_para_salvar, caminho_arquivo_csv)
    print("================================================")
    print("Mensagem Salva!!!")
    print("")
    input("Aperte Enter para continuar.")
    limpar_tela()   

# ================================================
#        Cria Name ID da mensagem
# ================================================

def cria_name_id(ano, mes, dia, horas, minutos, segundos):
    name_id = f"datetime.datetime({ano}, {mes}, {dia}, {horas}, {minutos}, {segundos}, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=75600)))"
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

# Pega apenas os Names IDs do arquivo
def salva_name_id_arquivo(dados_arquivo):
    names_ids_arquivo = {}

    for i in range(len(dados_arquivo)):
        id = dados_arquivo["Name ID"][13:-5]
        names_ids_arquivo[i] = id

    return names_ids_arquivo

# Detecta o sistema operacional para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Salvar dados da mensagem no arquivo csv    
def salvar_em_csv(dados_mensagem, caminho_arquivo_csv):
    # Define os cabeçalhos das colunas
    cabecalhos = ["Name ID", "Andar", "Ano", "Mês", "Dia", "Dia da Semana", "Horas", "Minutos", "Segundos"]
    
    # Verifica se o arquivo já existe
    arquivo_existe = os.path.isfile(caminho_arquivo_csv)
    
    # Abre o arquivo CSV para escrita ou append
    with open(caminho_arquivo_csv, mode='a', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=cabecalhos)
        
        # Escreve o cabeçalho apenas se o arquivo não existir
        if not arquivo_existe:
            writer.writeheader()
        
        # Escreve os novos dados
        writer.writerows(dados_mensagem.values())

# Função para pegar os Names IDs 
def def_names_ids_arquivo(caminho_arquivo):
    
    name_ids_arquivo = []

    try:

        # Abrir o arquivo CSV
        with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
            # Criar um leitor CSV
            lendo = csv.DictReader(file)
            
            # Iterar sobre as linhas do arquivo
            for linha in lendo:
                # Adicionar o valor da coluna "Name ID" à lista
                name_ids_arquivo.append(linha["Name ID"])

    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}
        
    return name_ids_arquivo

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

    while True:

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
            print(f"Andar: {sub_dados["Andar"]}.")
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