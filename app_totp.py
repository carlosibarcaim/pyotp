import os
from flask import Flask, request, jsonify
import pyotp
import base64

app = Flask(__name__)

# Función para convertir de hexadecimal a Base32
def hex_to_base32(hex_string):
    # Convertir el valor hexadecimal en bytes
    raw_data = bytes.fromhex(hex_string)
    # Codificar los bytes en Base32
    base32_encoded = base64.b32encode(raw_data).decode('utf-8')
    return base32_encoded

@app.route('/', methods=['GET'])
def home():
    return "Bienvenidos a la API de TOTP"

@app.route('/validar_totp', methods=['POST'])
def validar_totp():
    # Obtener el secreto y el código proporcionado desde el cuerpo de la solicitud
    data = request.get_json()
    secreto = data.get('secreto')
    codigo = data.get('codigo')

    if not secreto or not codigo:
        return jsonify({"error": "Faltan parámetros"}), 400

    # Convertir el secreto hexadecimal a Base32
    secreto_base32 = hex_to_base32(secreto)

    # Validar el código TOTP
    totp = pyotp.TOTP(secreto_base32)
    if totp.verify(codigo):
        return jsonify({"valid": True}), 200
    else:
        return jsonify({"valid": False}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('port', 5000)), debug=True)



