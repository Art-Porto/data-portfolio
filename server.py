"""
Simple Flask server for data portfolio
"""
from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='ScrubsByAna/graficos')

@app.route('/')
def index():
    return jsonify({
        'message': 'Data Portfolio API',
        'endpoints': {
            '/': 'This info',
            '/health': 'Health check',
            '/files': 'List available files'
        }
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/files')
def files():
    """List files in the workspace"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    folders = ['alura', 'fiap', 'google-data-analytics', 'ScrubsByAna']
    return jsonify({'folders': folders})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)