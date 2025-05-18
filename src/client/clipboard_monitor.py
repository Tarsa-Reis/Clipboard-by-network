import time
import pyperclip
import requests
from threading import Thread

class ClipboardMonitor:
    def __init__(self, server_url):
        self.server_url = server_url
        self.is_running = False
        self.ultimo_conteudo = ""
        print(f"Monitor iniciado - Conectando ao servidor: {server_url}")

    def start(self):
        self.is_running = True
        print("Iniciando monitoramento do clipboard...")
        self.monitor = Thread(target=self._monitor_clipboard)
        self.monitor.daemon = True
        self.monitor.start()
        print("Monitoramento ativo!")

    def _monitor_clipboard(self):
        print("Thread de monitoramento iniciada")
        while self.is_running:
            try:
                current_content = pyperclip.paste()
                if current_content != self.ultimo_conteudo:
                    print(f"Novo conteúdo detectado: '{current_content[:30]}...'")
                    self._send_to_server(current_content)
                    self.ultimo_conteudo = current_content

                self._check_server_updates()
            except Exception as e:
                print(f"Erro no monitoramento: {e}")
            time.sleep(1)

    def _send_to_server(self, content):
        try:
            print(f"Enviando para servidor: '{content[:50]}'")
            response = requests.post(f"{self.server_url}/set_clipboard",
                                  json={'content': content})
            print(f"Resposta do servidor: {response.status_code}")
        except Exception as e:
            print(f"Erro ao enviar para servidor: {e}")

    def _check_server_updates(self):
        try:
            response = requests.get(f"{self.server_url}/get_clipboard")
            server_content = response.json()['content']
            if server_content != self.ultimo_conteudo:
                print(f"Novo conteúdo do servidor: '{server_content[:50]}'")
                pyperclip.copy(server_content)
                self.ultimo_conteudo = server_content
        except Exception as e:
            print(f"Erro ao verificar servidor: {e}")