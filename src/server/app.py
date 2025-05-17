from flask import Flask, jsonify, request
from src.server.clipboard_manager import ClipboardManager

app = Flask(__name__)
clipboard_manager = ClipboardManager()


@app.route('/get_clipboard', methods=['GET'])
def get_clipboard():
    try:
        content = clipboard_manager.get_content()
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/set_clipboard', methods=['POST'])
def set_clipboard():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Nenhum dado recebido'}), 400

        clipboard_manager.set_content(data.get('content', ''))
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})