from flask import Flask, jsonify, request
from src.server.clipboard_manager import ClipboardManager

app = Flask(__name__)
clipboard_manager = ClipboardManager()

@app.route('/get_clipboard', methods=['GET'])
def get_clipboard():
    return jsonify({'content': clipboard_manager.get_content()})

@app.route('/set_clipboard', methods=['POST'])
def set_clipboard():
    data = request.json
    content = data.get('content', '')
    clipboard_manager.set_content(content)
    return jsonify({'status': 'success'})

def run_server(host='0.0.0.0', port=5000):
    app.run(host=host, port=port)

if __name__ == '__main__':
    run_server()