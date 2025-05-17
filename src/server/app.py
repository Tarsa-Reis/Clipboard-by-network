from flask import Flask, jsonify, request
from src.server.clipboard_manager import ClipboardManager
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
clipboard_manager = ClipboardManager()


@app.route('/get_clipboard', methods=['GET'])
def get_clipboard():
    try:
        content = clipboard_manager.get_content()
        logger.info(f"GET /get_clipboard - Retornando conteúdo: {content[:30]}...")
        return jsonify({'content': content})
    except Exception as e:
        logger.error(f"Erro em get_clipboard: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/set_clipboard', methods=['POST'])
def set_clipboard():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Nenhum dado recebido'}), 400

        content = data.get('content', '')
        logger.info(f"POST /set_clipboard - Recebido conteúdo: {content[:30]}...")

        clipboard_manager.set_content(content)
        return jsonify({'status': 'success'})
    except Exception as e:
        logger.error(f"Erro em set_clipboard: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)