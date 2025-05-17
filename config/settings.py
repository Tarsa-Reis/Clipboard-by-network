
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do servidor
SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')  # 0.0.0.0 permite conexões de qualquer IP
SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))

# Configurações do cliente
SERVER_URL = os.getenv('SERVER_URL', 'http://localhost:5000')