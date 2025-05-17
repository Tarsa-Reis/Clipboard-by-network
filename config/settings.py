import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do servidor
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
# No Render, a porta é definida pela variável PORT
SERVER_PORT = int(os.getenv('PORT', 10000))

# Configurações do cliente
SERVER_URL = os.getenv('SERVER_URL', 'https://clipboard-by-network.onrender.com')