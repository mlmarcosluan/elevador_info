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

