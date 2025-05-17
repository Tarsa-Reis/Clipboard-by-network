from src.client.clipboard_monitor import ClipboardMonitor
import time

print("Iniciando cliente de clipboard...")

# substituir pelo ip do servidor
server_url = "http://192.168.254.224:5000"
print(f"Conectando ao servidor: {server_url}")

monitor = ClipboardMonitor(server_url)
monitor.start()

print("\nCliente rodando! Para parar, pressione Ctrl+C")
print("----------------------------------------")
print("Aguardando alterações no clipboard...")

# Mantém o programa rodando
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrando cliente...")
    monitor.stop()
    print("Cliente encerrado!")