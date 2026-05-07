import os 
import json 



def cargar(nombre_archivo): 
    try: 
        if os.path.exists(nombre_archivo): 
            with open(nombre_archivo) as archivo:
                return json.load(archivo)
        else: 
            return []
    
    except json.JSONDecodeError as ex:
        print(ex)
    


        
def guardar(nombre_archivo, registros): 
    try: 
        with open(nombre_archivo, 'w') as archivo:

            json.dump(registros, archivo, indent=4 )
    
    except json.JSONDecodeError as ex:
        print(ex)





def generar_id(registros):
    if not registros: 
        return 1 
    
    else: 
        return registros[-1].get('id', 'error')+1






