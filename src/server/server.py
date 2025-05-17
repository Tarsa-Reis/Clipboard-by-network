from src.server.app import run_server
from config.settings import SERVER_HOST, SERVER_PORT

# Roda o servidor Flask
run_server(host=SERVER_HOST, port=SERVER_PORT)