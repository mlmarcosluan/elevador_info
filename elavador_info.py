"""

# ================================================
#        Importar configuração do Telegram
# ================================================
    
    # Iniciar cliente
    asyncio.run(executar_cliente(api_id, api_hash, phone_number, session_name))

# ================================================
#        Função para iniciar sessão do Telegram
# ================================================
async def iniciar_sessao(api_id, api_hash, phone_number, session_name):
    try:
        # Criar cliente do Telegram
        client = TelegramClient(session_name, api_id, api_hash)
        
        print("Conectando ao Telegram...")
        await client.connect()
        
        # Verificar se a sessão já está ativa
        if await client.is_user_authorized():
            print("Sessão já está ativa!")
            return client
        
        # Se a sessão não estiver ativa, iniciar autenticação
        print("Usuário não autenticado. Iniciando autenticação...")
        await client.send_code_request(phone_number)
        
        # Solicitar o código enviado pelo Telegram
        codigo = input("Digite o código recebido no telefone: ")
        await client.sign_in(phone=phone_number, code=codigo)
        
        # Verificar se é necessário autenticação em dois fatores
        if not await client.is_user_authorized():
            senha = input("Autenticação em dois fatores necessária! Digite sua senha: ")
            await client.sign_in(password=senha)
        
        print("Autenticação concluída com sucesso!")
        return client
    
    except SessionPasswordNeededError:
        print("Autenticação em dois fatores necessária!")
        senha = input("Digite sua senha: ")
        await client.sign_in(password=senha)
    
    except Exception as e:
        print(f"Erro durante a autenticação: {e}")
        return None

# ================================================
#        Acessar mensagens do grupo
# ================================================
async def acessar_grupo(client):
    # Substitua pelo ID ou username do grupo
    id_grupo = "-1002461674456"  # Certifique-se de usar um ID válido
    
    try:
        # Obter a entidade do grupo
        group_entity = await client.get_entity(id_grupo)
        print(f"Acessando grupo: {group_entity.title}")
        
        # Iterar sobre as mensagens do grupo (da mais antiga para a mais recente)
        print("Capturando mensagens...")
        async for message in client.iter_messages(group_entity, reverse=True):
            print(f"Mensagem: {message.text} | Enviada por: {message.sender_id} | Data: {message.date}")
    
    except Exception as e:
        print(f"Erro ao acessar o grupo: {e}")

# ================================================
#        Função principal
# ================================================
async def executar_cliente(api_id, api_hash, phone_number, session_name):
    # Iniciar sessão
    client = await iniciar_sessao(api_id, api_hash, phone_number, session_name)
    
    if client:
        # Acessar o grupo após a autenticação
        await acessar_grupo(client)
        
        # Desconectar o cliente
        await client.disconnect()

# Executar o script
if __name__ == "__main__":
    import_telegram()
"""

# ================================================
#        Importar pacotes
# ================================================
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import os
from dotenv import load_dotenv

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
#        Função principal
# ================================================

async def main():
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
            messages = await client.get_messages(group_entity, limit=100)  # Limitar a 100 mensagens
            
            for message in messages:
                print(f"Mensagem: {message.message} | Enviada por: {message.sender_id} | Data: {message.date}")
        
        except Exception as e:
            print(f"Erro ao acessar o grupo: {e}")
    
    finally:
        # Desconectar o cliente
        await client.disconnect()


# Executar o script
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())