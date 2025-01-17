import os
from flask import Flask, request, jsonify
import pyotp
from conversiones import hex_to_base32

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Bienvenidos a la API de TOTP"

@app.route('/validar_totp', methods=['POST'])
def validar_totp():
    try:
        # Obtener el secreto y el código proporcionado desde el cuerpo de la solicitud
        data = request.get_json()
        secreto = data.get('secreto')
        codigo = data.get('codigo')

        if not secreto or not codigo:
            return jsonify({"error": "Faltan parámetros"}), 400

        secreto_base32 = hex_to_base32(secreto)

        # Validar el código TOTP
        totp = pyotp.TOTP(secreto)
        if totp.verify(codigo):
            return jsonify({"valid": True}), 200
        else:
            return jsonify({"valid": False}), 200
    
    except Exception as e:
        # Manejo de errores
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('port', 5000)), debug=True)


