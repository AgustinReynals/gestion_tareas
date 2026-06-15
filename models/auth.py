import bcrypt
from flask import session
from models.db import *

def validarSesion(datos):
    if not datos:
        return False
    try:
        respuesta = getDatabaseUnico("usuarios","email",datos["email"])
        if respuesta:
            for key,valor in respuesta.items():
                if  bcrypt.checkpw(datos["contrasena"].encode(),valor["contrasena"].encode()):
                    session["usuario"] = {"id":key,
                                        "nombre":valor["nombre"]}
                    return True
        return False
    except Exception as e:
        print(f"ocurrio un error(auth-1): {e}")
        return False

def RegistrarUsuario(datos):
    if not datos:
        return False
    try:
        passwordHasheada = hashedPassword(datos["contrasena"])
        dato = {"nombre":datos["nombre"],
                "email":datos["email"],
                "contrasena":passwordHasheada}
        respuesta = postDatabase("usuarios",dato)
        return respuesta
    except Exception as e:
        print(f"ocurrio un error(auth-2): {e}")
        return False
    
def emailExistente(email):
    if not email:
        return False
    try:
        respuesta = getDatabaseUnico("usuarios","email",email)
        if respuesta or respuesta == False:
            return False
        return True
    except Exception as e:
        print(f"ocurrio un error(auth-3): {e}")
        return False

def hashedPassword(password):
    if not password:
        return False
    try: 
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')
    except Exception as e:
        print(f"ocurrio un error(auth-4): {e}")
        return False