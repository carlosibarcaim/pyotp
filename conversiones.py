# conversiones.py
import base64

def hex_to_base32(hex_string):
    """
    Convierte una cadena en base32 a un formato adecuado.
    """
    # Convierte la cadena hexadecimal a bytes (solo si la entrada es en hexadecimal)
    try:
        bytes_data = bytes.fromhex(hex_string)  # Solo si la entrada es hexadecimal
    except ValueError:
        bytes_data = base64.b32decode(hex_string)  # Si no, la entrada es base32 y se decodifica directamente

    # Convierte los bytes a base32
    base32_data = base64.b32encode(bytes_data).decode('utf-8')
    
    return base32_data

