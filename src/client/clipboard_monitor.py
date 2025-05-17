import time
import pyperclip
import requests
from threading import Thread


class ClipboardMonitor:
    def __init__(self, server_url):
        self.server_url = server_url
        self.is_running = False
        self.last_content = ""

    def start(self):
        self.is_running = True
        self.monitor_thread = Thread(target=self._monitor_clipboard)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop(self):
        self.is_running = False

    def _monitor_clipboard(self):
        while self.is_running:
            try:
                current_content = pyperclip.paste()
                if current_content != self.last_content:
                    self._send_to_server(current_content)
                    self.last_content = current_content

                self._check_server_updates()
            except Exception as e:
                print(f"Erro: {e}")
            time.sleep(1)

    def _send_to_server(self, content):
        try:
            requests.post(f"{self.server_url}/set_clipboard",
                          json={'content': content})
        except Exception as e:
            print(f"Erro ao enviar para servidor: {e}")

    def _check_server_updates(self):
        try:
            response = requests.get(f"{self.server_url}/get_clipboard")
            server_content = response.json()['content']
            if server_content != self.last_content:
                pyperclip.copy(server_content)
                self.last_content = server_content
        except Exception as e:
            print(f"Erro ao verificar servidor: {e}")