import re
import hashlib

def validarSenha(senha):
    if not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8}$", senha):
        return False
    return True

def hashSenha(senha, salt):
    return hashlib.pbkdf2_hmac(
        'sha256',
        senha.encode('utf-8'),
        salt,
        600000
    )