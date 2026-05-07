from gestion_json import *
from datetime import datetime


def registrar_logs(descripcion): 
    registro=cargar('logs.json')
    evento={}
    evento['descripcion']=descripcion
    evento['hora']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro.append(evento)

    guardar('logs.json', registro)
