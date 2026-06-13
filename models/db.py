import requests, os
from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("API_DATABASE")


def getDatabase(clave):
    if not clave:
        return False
    try:
        get_url = f"{URL}/{clave}.json"
        respuesta = requests.get(get_url,timeout=5)
        if respuesta.status_code == 200:
            return respuesta.json()
        return False
    except Exception as e:
        print(f"ocurrio un error(db-1): {e}")
        return False

def postDatabase(clave, datos):
    if not datos or not clave:
        return False
    try:
        post_url = f"{URL}/{clave}.json"
        respuesta = requests.post(post_url,json=datos)
        return respuesta.status_code == 200
    except Exception as e:
        print(f"ocurrio un error(db-2): {e}")
        return False

def deleteDatabase(clave):
    if not clave:
        return False
    try:
        delete_url = f"{URL}/{clave}.json"
        respuesta = requests.delete(delete_url)
        return respuesta.status_code == 200
    except Exception as e:
        print(f"ocurrio un error(db-3): {e}")
        return False

def updateDatabase(clave,datos):
    if not clave or not datos:
        return False
    try:
        update_url = f"{URL}/{clave}.json"
        respuesta = requests.patch(update_url,json=datos)
        return respuesta == 200
    except Exception as e:
        print(f"ocurrio un error(db-4): {e}")
        return False
