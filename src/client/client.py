from src.client.clipboard_monitor import ClipboardMonitor
from config.settings import SERVER_URL
import time

monitor = ClipboardMonitor(SERVER_URL)
monitor.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nEncerrando cliente...")
    monitor.stop()
    print("Cliente encerrado!")