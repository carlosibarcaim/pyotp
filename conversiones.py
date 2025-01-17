# conversiones.py
import re
import base64

# Función para verificar si una cadena es hexadecimal
def is_hexadecimal(s):
    return bool(re.match('^[0-9A-Fa-f]+$', s))

def hex_to_base32(hex_string):
    """
    Convierte una cadena hexadecimal en base32.
    """
    try:
        # Convierte de hexadecimal a bytes
        bytes_data = bytes.fromhex(hex_string)
    except ValueError:
        return None  # Si no es hexadecimal, devolvemos None (esto indica que no es hex)

    # Convierte los bytes a base32
    base32_data = base64.b32encode(bytes_data).decode('utf-8')
    return base32_data

def process_secret(secret):
    """
    Procesa el secreto. Si es hexadecimal, lo convierte a base32.
    Si ya está en base32, lo deja tal cual.
    """
    if is_hexadecimal(secret):
        return hex_to_base32(secret)
    else:
        return secret  # Si no es hexadecimal, lo dejamos como base32


