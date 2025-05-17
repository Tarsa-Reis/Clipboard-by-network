from src.server.app import run_server
from src.client.clipboard_monitor import ClipboardMonitor

#iniciar servidor

server_url = "http://192.168.254.224:5000"
monitor = ClipboardMonitor(server_url)
monitor.start()

#Roda o servidor Flask (colocar o seu IP local)

run_server(host='192.168.254.224', port=5000)
