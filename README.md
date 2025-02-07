# Elevador Info

![Python](https://img.shields.io/badge/Python-3.12-red) ![Telegram](https://img.shields.io/badge/Telegram-API-red)

Este projeto tem como objetivo extrair dados de mensagens no Telegram que informam o andar em que o elevador do meu condomínio se encontra ao chegar em casa. Os dados são processados e armazenados em uma base de dados para posterior análise e visualização.

---

## 📌 Índice

1. [Descrição do Projeto](#-descrição-do-projeto)
2. [Dados Coletados](#-dados-coletados)
3. [Pré-requisitos](#-pré-requisitos)
4. [Instalação](#-instalação)
5. [Como Usar](#-como-usar)
6. [Estrutura do Projeto](#-estrutura-do-projeto)

---


## 📝 Descrição do Projeto

O projeto captura mensagens enviadas no Telegram com informações sobre o andar do elevador (de 0 a 11). Essas mensagens incluem:
- O número do andar.
- A data da mensagem (dia do mês, dia da semana).
- A hora e os minutos da mensagem.

Os dados são coletados diariamente, armazenados em uma base de dados e posteriormente tratados para análise e visualização.

---

## 📊 Dados Coletados

As seguintes informações são extraídas das mensagens:

| Campo            | Descrição                              | Variável |
|------------------|----------------------------------------|----------|
| Andar            | Número do andar do elevador (0 a 11)  | `n_andar`   |
| Dia do Mês       | Dia do mês da mensagem                | `dia_mes`   |
| Dia da Semana    | Dia da semana da mensagem             | `dia_semana`|
| Hora             | Hora da mensagem                      | `hora`      | 
| Minuto           | Minuto da mensagem                    | `minuto`    |

Esses dados são armazenados em uma base de dados para facilitar consultas e análises.

---

## 🔧 Pré-requisitos

Para executar este projeto, você precisará dos seguintes itens instalados:

- Python 3.12 ou superior
- Bibliotecas Python:
  - `Telethon` (para interagir com a API do Telegram)
  - 
- Credenciais da API do Telegram (`API ID` e `API Hash`), obtidas em [my.telegram.org](https://my.telegram.org/).

---

## 💻 Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/elevador_info.git
   cd elevador_info
   ```
2. Instale as dependências necessárias:
    ```bash
    pip instal telethon
    ```
3. Condigure suas credenciais do Telegram:
    - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
    ```
    API_ID=seu_api_id
    API_HASH=seu_api_hash
    PHONE_NUMBER=seu_numero_telegram
    ```

## 🚀 Como Usar
1. Execute o script principal para coletar os dados:
    ```bash
    python elevador_info.py
    ```
2. O script irá:
    - Conectar-se ao Telegram usando suas credenciais.
    - Extrair as mensagens relevantes do chat especificado.
    - Salvar os dados em uma base de dados.
3. Após a coleta, você pode tratar e visualizar os dados conforme necessário

## 📂 Estrutura do Projeto
```
    elevador_info/
    ├── 
    ├── 
    ├── 
    ├──      
    └── README.md             # Este arquivo
```
Por segurança o arquivo `.env` esta em uma pasta fora do repositório