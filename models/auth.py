from flask import session
# from bcrypt import *
from models.db import *

def validarSesion(datos):
    if not datos:
        return False
    try:
        respuesta = getDatabase("usuarios")
        if respuesta == False:
            return False
        for key,valor in respuesta.items():
            if valor["email"] == datos["email"] and valor["contrasena"] == datos["contrasena"]:
                session["usuario"] = {"id":key,
                                    "nombre":valor["nombre"]}
                return True
        return False
    except Exception as e:
        print(f"ocurrio un error(auth-1): {e}")
        return False
