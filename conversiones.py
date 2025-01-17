# conversiones.py

import base64

def hex_to_base32(hex_string):
    """
    Convierte una cadena hexadecimal en base32.
    """
    # Convierte la cadena hexadecimal a bytes
    bytes_data = bytes.fromhex(hex_string)
    
    # Convierte los bytes a base32
    base32_data = base64.b32encode(bytes_data).decode('utf-8')
    
    return base32_data
