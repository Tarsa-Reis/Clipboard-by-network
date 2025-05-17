from src.client.clipboard_monitor import ClipboardMonitor

#substituir pelo ip do servidor
server_url = "http://0.0.0.0:5000"
monitor = ClipboardMonitor(server_url)
monitor.start()

# Mantém o programa rodando
try:
    while True:
        pass
except KeyboardInterrupt:
    monitor.stop()