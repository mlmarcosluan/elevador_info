# ================================================
#        Importar pacotes
# ================================================
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import os
from dotenv import load_dotenv
import asyncio

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
#        Função gerais
# ================================================    

# Detecta o sistema operacional e executa o comando adequado
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# ================================================
#        Função principal
# ================================================

async def main():

    while True:

        try:
            escolha = menu_principal()

        except ValueError:
            print ("Valor incorreto")
            input("Aperte enter para continuar...")
            continue
        if escolha == 1: # Foi escolhido pesquisar novas mensagens

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
                        print(f"Mensagem: {message.message} | Data: {message.date}")

                    input("Aperte enter para coninuar")
                except Exception as e:
                    print(f"Erro ao acessar o grupo: {e}")
            
            finally:
                # Desconectar o cliente
                await client.disconnect()
        elif escolha == 0:
            print("Encerrando programa.")
            break

# Executar o script
if __name__ == "__main__":
    asyncio.run(main())