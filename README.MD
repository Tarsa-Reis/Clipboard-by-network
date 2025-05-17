# Clipboard Share

Sistema de compartilhamento de clipboard entre computadores na mesma rede.

## Instalação

1. Clone o repositório:
    bash git clone [https://seu-repositorio/clipboard_share.git](https://seu-repositorio/clipboard_share.git) cd clipboard_share

2. Instale as dependências:
    bash pip install -r requirements.txt


## Uso

### Servidor

Para iniciar o servidor:

bash python -m src.server.app


### Cliente

Para iniciar o cliente:

bash python -m src.client.clipboard_monitor


## Configuração

Crie um arquivo `.env` na raiz do projeto:

env SERVER_HOST=0.0.0.0 SERVER_PORT=5000 SERVER_URL=[http://192.168.1.100:5000](http://192.168.1.100:5000)


## Segurança

Este é um projeto básico. Para uso em produção, considere:
- Adicionar autenticação
- Implementar criptografia
- Configurar HTTPS
- Limitar IPs permitidos

