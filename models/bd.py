import requests, os
from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("API_DATABASE")

def getDatabase(dato):
    if not dato:
        return False
    try:
        urlGet = "%s/%s.json" % (URL,dato)
        respuesta = requests.get(urlGet)

        if respuesta.status_code != 200:
            return False
    
        return respuesta
    except Exception as e:
        print(f"ocurrio un error(db-1): {e}")
        return False

def postDatabase():
    pass

def deletDatabase():
    pass

def updateDatabase():
    pass
