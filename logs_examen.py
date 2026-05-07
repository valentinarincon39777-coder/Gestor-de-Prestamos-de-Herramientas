from gestion_json import *
from datetime import datetime


def registrar_error_logs(descripcion, usuario): 
    registro=cargar('logs_error.json')
    evento={}
    evento['descripcion']=descripcion
    evento['hora']=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    evento['usuario']=usuario
    registro.append(evento)

    guardar('logs_error.json', registro)