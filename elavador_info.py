# ================================================
#        Importar pacotes
# ================================================
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import os
import csv
from dotenv import load_dotenv
import asyncio
from datetime import datetime, timedelta, timezone

# ================================================
#        Pegar dados do arquivo .env
# ================================================

def dados_telegram():
    # Caminho do arquivo .env
    caminho_env = "/home/marcos/VScode/dados.env"
    
    # Carregar variáveis do arquivo .env
    load_dotenv(caminho_env)
    
    # Obter variáveis de ambiente
    api_id = os.getenv("api_id")
    api_hash = os.getenv("api_hash")
    phone_number = os.getenv("phone_number")
    session_name = os.getenv("session_name")
    user_name_grupo = os.getenv("user_name_grupo")
    
    # Verificar se as variáveis foram carregadas corretamente
    if not all([api_id, api_hash, phone_number, session_name, user_name_grupo]):
        print("Erro: Variáveis de ambiente não encontradas. Verifique o arquivo .env.")
        return

    return api_id, api_hash, phone_number, session_name, user_name_grupo

# ================================================
#        Menu principal do programa
# ================================================

def menu_principal():
    print("================================================")
    print("Digite: ")
    print("1, para buscar mensagens novas.")
    print("2, teste teste")
    print("")
    print("")
    print("")
    print("0, para sair.")
    escolha = int(input("Digite: "))

    limpar_tela()

    return (escolha)

# ================================================
#        Pesquisar novas mensagens
# ================================================

async def pesquisar_mensagens():
    api_id, api_hash, phone_number, session_name, user_name_grupo = dados_telegram()
            # Criar cliente do Telegram
    client = TelegramClient(session_name, api_id, api_hash)
            
    try:
        # Conectar ao Telegram
        await client.start(phone=phone_number)
        print("Conectado ao Telegram!")
        
        # Verificar se o usuário está autorizado
        if not await client.is_user_authorized():
            print("Usuário não autenticado. Iniciando autenticação...")
            await client.send_code_request(phone_number)
            codigo = input("Digite o código recebido no telefone: ")
            await client.sign_in(phone=phone_number, code=codigo)
        
        print("Autenticação concluída com sucesso!")
        
        # Acessar o grupo
        try:
            group_entity = await client.get_entity(user_name_grupo)
            print(f"Acessando grupo: {group_entity.title}")
            
            # Capturar as últimas mensagens do grupo
            print("Capturando as últimas mensagens...")
            mensagens = await client.get_messages(group_entity, limit=100)  # Limitar a 100 mensagens
            
            dicionario_mensagens = {}
            for mensagem in mensagens:
                # Ajustar data e hora para o brasil
                data_utc = mensagem.date  # Data original em UTC
                data_brasil = data_utc.astimezone(timezone(timedelta(hours=-3)))  # Ajuste para UTC-3

                # Adicionar informações da mensagem no dicionario
                
                dicionario_mensagens[data_brasil] = {"Andar": mensagem.message,"Ano": data_brasil.year, "Mês": data_brasil.month, "Dia": data_brasil.day, "Horas": data_brasil.hour, "Minutos": data_brasil.minute, "Segundos": data_brasil.second} 

            ids_mensagens = dicionario_mensagens.keys()
            lista_ids_mensagens = list(ids_mensagens)
            
        except Exception as e:
            print(f"Erro ao acessar o grupo: {e}")
    
    finally:
        # Desconectar o cliente
        await client.disconnect()

    return lista_ids_mensagens, dicionario_mensagens

# ================================================
#        Função gerais
# ================================================    

# Detecta o sistema operacional para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para pegar os Names IDs 
def def_names_ids_arquivo(caminho_arquivo_csv):
    
    name_ids_arquivo = []

    try:

        # Abrir o arquivo CSV
        with open(caminho_arquivo_csv, mode='r', encoding='utf-8') as file:
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

# Salvar dados da mensagem no arquivo csv    
def salvar_em_csv(dados_mensagem, caminho_arquivo_csv):
    
    # Cria um novo dicionario com as informações que ja temos para poder salvar no arquivo csv
    subdados = dados_mensagem.values()
    lista_subdados = list(subdados)
    
    # Verifica mensagem antes de salvar
    if type(lista_subdados[1] != str):
        print("================================================")
        print("")
        print("")
        print("")
        print(f"Mensagem do dia: {lista_subdados[4]}/{lista_subdados[3]}/{lista_subdados[2]}, as {lista_subdados[5]}:{lista_subdados[6]}, não salva...")  
        input("Aperte enter para continuar.")
        return 
    # Troca o str do andar por int
    try:
        int_andar = int(lista_subdados[0])
    except ValueError:
        print(f"Verifique a mensagem do dia {lista_subdados[4]}/{lista_subdados[3]}/{lista_subdados[2]}, as {lista_subdados[5]}:{lista_subdados[6]}")
        return  # Sai da função se houver erro na conversão
    
    novo_dicionario = {
        "Name ID": lista_subdados[0],
        "Andar": int_andar,
        "Ano": lista_subdados[2],
        "Mês": lista_subdados[3],
        "Dia": lista_subdados[4],
        "Dia da Semana": lista_subdados[5],
        "Horas": lista_subdados[6],
        "Minutos": lista_subdados[7],
        "Segundos": lista_subdados[8]
    }
    
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
        
        # Escreve os novos dados (um único dicionário)
        writer.writerow(novo_dicionario)  # Use writerow em vez de writerows

# Pega o Ano, Mes e dia para transformar em dia da semana
def pega_dia_semana(ano, mes, dia):

    data = datetime(ano, mes, dia)
    dia_semana = data.weekday()

    # Converte o dia_semana no nome do dia da semana
    nomes_dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sabado", "Domingo"]
    nome_dia_semana = nomes_dias[dia_semana]

    return nome_dia_semana

# ================================================
#        Salvar mensagens no arquivo csv
# ================================================

def salvar_dados_mensagens(lista_ids_mensagens, caminho_arquivo_csv, dicionario_mensagens):
    
    names_ids_arquivo = def_names_ids_arquivo(caminho_arquivo_csv)

    # Percorre todos os elementos da lista de Ids das mensagens
    for id_mensagem in lista_ids_mensagens:
        mensagem_exite = False

        # Percorre por todos os IDs no arquivo csv
        for id_arquivo in names_ids_arquivo:
            if id_mensagem == id_arquivo:
                mensagem_exite = True
                break
        
        if mensagem_exite == False:

            dados = dicionario_mensagens[id_mensagem]

            teste = id_mensagem

    
            list_keys = list(dicionario_mensagens.keys())
            list_values = list(dicionario_mensagens.values())
            

            
            dados_mensagem = {
                "Name ID": id_mensagem,
                "Andar": dados["Andar"],
                "Ano": dados["Ano"],
                "Mês": dados["Mês"],
                "Dia": dados["Dia"],
                "Dia da Semana": pega_dia_semana(dados["Ano"], dados["Mês"], dados["Dia"]),
                "Horas": dados["Horas"],
                "Minutos": dados["Minutos"],
                "Segundos": dados["Segundos"]
            }

            
            salvar_em_csv(dados_mensagem, caminho_arquivo_csv)

            




# ================================================
#        Função principal
# ================================================

async def main():

    caminho_arquivo_csv = "/home/marcos/VScode/elevador_info/data_base/data_base.csv"
    while True:

        try:
            escolha = menu_principal()

        except ValueError:
            print ("Valor incorreto")
            input("Aperte enter para continuar...")
            continue

        if escolha == 1: # Foi escolhido pesquisar novas mensagens
            lista_ids_mensagens, dicionario_mensagens = await pesquisar_mensagens()
            salvar_dados_mensagens(lista_ids_mensagens, caminho_arquivo_csv, dicionario_mensagens)
        
        elif escolha == 0:
            print("Encerrando programa.")
            break
        
        print("Final")
# Executar o script
if __name__ == "__main__":
    asyncio.run(main())