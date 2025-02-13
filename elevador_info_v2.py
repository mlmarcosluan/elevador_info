# ================================================
#        Importar pacotes
# ================================================
# Importa a classe TelegramClient da biblioteca Telethon, que permite interagir com a API do Telegram.
from telethon import TelegramClient

# Importa a exceção SessionPasswordNeededError, que é levantada quando uma senha de duas etapas é necessária para acessar a conta.
from telethon.errors import SessionPasswordNeededError

# Importa o módulo asyncio, que fornece suporte para programação assíncrona em Python, permitindo executar tarefas concorrentes.
import asyncio

# Importa o módulo os, que fornece funções para interagir com o sistema operacional, como acessar variáveis de ambiente e manipular caminhos de arquivos.
import os

# Importa o módulo csv, que permite ler e escrever dados em formato CSV (Comma-Separated Values).
import csv

# Importa a função load_dotenv do módulo dotenv, que carrega variáveis de ambiente a partir de um arquivo .env, facilitando o gerenciamento de configurações sensíveis.
from dotenv import load_dotenv

# Importa classes do módulo datetime (datetime, timedelta, timezone) para manipular datas, horários e fusos horários.
from datetime import datetime, timedelta, timezone

# Importa funcionalidades da biblioteca colorama para adicionar cores e estilos ao terminal.
from colorama import init, Fore, Style

# ================================================
#        Pegar dados do arquivo .env

def dados_api_telegram():
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

# ================================================
#       Conectar ao telegram
async def conectar_telegram ():
    api_id, api_hash, phone_number, session_name, user_name_grupo = dados_api_telegram()
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

# ================================================
#        Funções gerais

# ================================================
# Detecta o sistema operacional para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
# ================================================

# ================================================

# ================================================
#        Menus do script

def menu_principal():
    while True:
        limpar_tela()
        
        # Cabeçalho estilizado
        print(Fore.CYAN + "================================================")
        print(Fore.GREEN + "              MENU PRINCIPAL                   ")
        print(Fore.CYAN + "================================================")
        
        # Opções do menu
        print(Fore.YELLOW + "[1]" + Fore.WHITE + " - Buscar mensagens novas")
        print(Fore.YELLOW + "[2]" + Fore.WHITE + " - Teste teste")
        print(Fore.YELLOW + "[3]" + Fore.WHITE + " - Outra opção")
        print(Fore.YELLOW + "[4]" + Fore.WHITE + " - Mais uma opção")
        print(Fore.RED + "[0]" + Fore.WHITE + " - Sair")
        
        print(Fore.CYAN + "================================================")
        
        # Entrada do usuário
        try:
            escolha = int(input(Fore.MAGENTA + "Digite sua escolha: " + Fore.WHITE))

        except ValueError:
            print(Fore.RED + "Erro: Por favor, digite um número válido.")
            input(Fore.YELLOW + "Pressione Enter para continuar...")

        # Verifica a escolha
        if escolha == 0:
            return escolha
        elif escolha == 1:
            return escolha
        else:
            print(Fore.RED + "Digite uma opção válida...")
            input(Fore.YELLOW + "Aperte enter para continuar...")
        


# ================================================

# ================================================
#        Função principal

async def main():
    # Inicializa o colorama para suporte a cores no terminal
    init(autoreset=True)

    # Chama o menu principal
    escolha = menu_principal()

    if escolha == 0:
        return
    elif escolha == 1:
        # Procurar dados do telegram
        lista_ids_mensagens, dicionario_mensagens = await conectar_telegram()

        # Conecta ao telgram e busca as mensagens


# ================================================    

# Executar o script
if __name__ == "__main__":
    asyncio.run(main())
