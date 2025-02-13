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
# ================================================
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
            return escolha
        except ValueError:
            print(Fore.RED + "Erro: Por favor, digite um número válido.")
            input(Fore.YELLOW + "Pressione Enter para continuar...")

# ================================================

# ================================================
#        Função principal

async def main():
    # Inicializa o colorama para suporte a cores no terminal
    init(autoreset=True)

    # Chama o menu principal
    escolha = menu_principal()
    

# ================================================    

# Executar o script
if __name__ == "__main__":
    asyncio.run(main())
