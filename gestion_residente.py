
from gestion_json import *





def catalogo_herramientas(): 

    registros=cargar('herramientas.json')

    if not registros:
        print('NO HAY ARCHIVOS DE HERRAMIENTAS')
    
    else: 
        encontrado=False 
        for elemento in registros: 
            if elemento.get('cantidad')>= 1 and elemento.get('estado')=='Activa': 
                encontrado=True 
                print('-'*30)
                print(f'''
                    Herramienta: {elemento.get('nombre', 'ERROR')}
                    Cantidad: {elemento.get('cantidad','ERROR')}
                      ''')
        if not encontrado: 
            print('No hay herramientas disponibles en estos momento. Una disculpa.')



def proxima_disponibilidad(): 
    #para aquellas herramientas con estado activa y cantidad igual que cero  de registros herramientas 
   

    registro_herramientas=cargar('herramientas.json')

    if not registro_herramientas: 
        print('NO HAY REGISTRO DE HERRAMIENTAS')
    
    else: 
        encontrado= False
        print('A continuacion, aquellas herramientas activas pero en cantidad NO disponible')

        for elemento in registro_herramientas: 
            if elemento.get('estado', 'ERROR')=='Activa' and elemento.get('cantidad')==0: 

                herramienta=elemento.get('nombre', 'ERROR')

                registro_prestamos=cargar('prestamos.json')
                if not registro_prestamos: 
                 print('NO HAY REGISTRO DE HERRAMIENTAS')
    
                else: 
                     for elemento in registro_prestamos: 
                        if elemento.get('herramienta')==herramienta: 
                            encontrado=True
                            print (f'''
                            Herramienta: {elemento.get('herramienta')}
                            Usuario que la posee: {elemento.get('usuario')}
                            Posible feha de disponibilidad de herramienta: {elemento.get('fecha_vencimiento')}
                                   ''')
                            
        if not encontrado: 
            print('Todas las herramientas están activas y disponibles')


           
                
                            

                        