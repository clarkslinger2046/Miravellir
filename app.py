from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "app": "Miravellir Backend",
        "version": "1.0",
        "status": "running",
        "time": datetime.now().isoformat(),
        "message": "¡Bienvenido a Miravellir! 🚀"
    })

@app.route('/api/status')
def status():
    return jsonify({
        "battery_example": 42,
        "device": "Samsung Galaxy S25 Ultra",
        "imei": "351234567890123",
        "server": "online",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/recargar', methods=['POST'])
def recargar():
    data = request.json
    monto = data.get('monto')
    return jsonify({
        "success": True,
        "monto": monto,
        "mensaje": f"Recarga de Bs {monto} procesada correctamente"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)