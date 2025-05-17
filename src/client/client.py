from src.client.clipboard_monitor import ClipboardMonitor
from config.settings import SERVER_URL
import time

print("Iniciando cliente de clipboard...")
print(f"Conectando ao servidor: {SERVER_URL}")

monitor = ClipboardMonitor(SERVER_URL)
monitor.start()

print("\nCliente rodando! Para parar, pressione Ctrl+C")
print("----------------------------------------")
print("Aguardando alterações no clipboard...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrando cliente...")
    monitor.stop()
    print("Cliente encerrado!")