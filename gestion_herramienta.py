

from validaciones import validar_menu, validar_numero
from gestion_json import *
from logs import registrar_logs
from logs_examen import registrar_error_logs





NOMBRE_ARCHIVO='herramientas.json'


def menu_herramientas():

    while(True):
        print('-'*30)
        op_herramienta=validar_menu('''
                                    ---MENU HERRAMIENTAS---
                                    1)Registrar herramienta
                                    2)Listar herramientas 
                                    3)Buscar herramientas
                                    4)Actualizar herramienta
                                    5)Eliminar o incativar herramienta
                                    6)Salir del menú herramientas
                                    : ''',1,6)
        
        match op_herramienta: 
            
            case 1:
                registrar()
            case 2:
                listar()
            case 3:
                buscar()
            case 4:
                actualizar()

            case 5: 
                eliminar()
            
                


            case 6: 
                break 


def registrar(): 
    registros=cargar(NOMBRE_ARCHIVO)
    herramienta={}

    herramienta['id']=generar_id(registros)
    herramienta['nombre']=input('Ingrese el nombre de la herramienta: ')
    herramienta['categoria']=categoria_herramienta()
    herramienta['cantidad']=validar_numero('Ingrese la cantidad de herramientas: ')
    herramienta['estado']=estado_herramienta()
    herramienta['valor']=validar_numero('Ingrese el valor estimado a pagar en caso de pérdida o daño de la herramieta: ')

    registros.append(herramienta)
    guardar(NOMBRE_ARCHIVO, registros)
    print(F'HERRAMIENTA {herramienta['nombre']} INGRESADA CORRECTAMETE ')
    registrar_logs(F'La herramienta {herramienta['nombre']} ha sido registrada')




def categoria_herramienta(): 
    op_categoria=validar_menu('''
    Ingrese el número al cual pertenece la categoría de la herramienta:
                              1)Herramientas básicas
                              2)Herramientas eléctricas
                              3)Herramientas de jardinería
                              4)Herramientas de medición
                              5)Herramientas grandes 
                              6)Otros
                              : ''',1,6)
    match op_categoria: 
        case 1: 
            h='Herramientas básicas'
        case 2: 
            h='Herramientas eléctricas'
        case 3: 
            h='Herramientas de jardinería'
        case 4: 
            h='Herramientas de medición'
        case 5: 
            h='Herramientas grande'
            
        case 6: 
            h='Otros'

    return h 






def estado_herramienta(): 
    op_estado=validar_menu('''
    Ingrese el número al cual pertenece el estado de la herramienta:
                              1)Activa
                              2)En reparación
                              3)Fuera de servicio
                              
                              : ''',1,3)
    match op_estado: 
        case 1: 
            h='Activa'
        case 2: 
            h='En reparación'
        case 3: 
            h='Fuera de servicio'
        
    return h    
       




def listar(): 
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA LISTAR')
    else: 

        for elemento in registros: 
            print('-'*30)
            print(f'''
                       
                  ID de la herramienta: {elemento.get('id', 'ERROR')}
                  Nombre: {elemento.get('nombre', 'ERROR')}
                  Categoria: {elemento.get('categoria', 'ERROR')}
                  Cantidad: {elemento.get('cantidad', 'ERROR')}
                  Estado: {elemento.get('estado', 'ERROR')}
                  Valor: ${elemento.get('valor', 'ERROR')}''')



def buscar(): 
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA BUSCAR')
    
    
    else: 
        while(True):
            id=validar_numero('Ingrese el ID de la herramienta a buscar: ')
            
            for elemento in registros: 
                if elemento.get('id', 'ERROR')==id: 

                    print(f'''
                    ID de la herramienta: {elemento.get('id', 'ERROR')}
                    Nombre: {elemento.get('nombre', 'ERROR')}
                    Categoria: {elemento.get('categoria', 'ERROR')}
                    Cantidad: {elemento.get('cantidad', 'ERROR')}
                    Estado: {elemento.get('estado', 'ERROR')}
                    Valor: ${elemento.get('valor', 'ERROR')}''')
                    return 
            
            print(f'EL ID {id} NO HA SIDO ENCONTRADO')




def actualizar(): 

    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA ACTUALIZAR')
    
    
    else: 
        while(True):
            listar()
            id=validar_numero('Ingrese el ID de la herramienta a actualizar: ')

            op_actualizar=validar_menu('''¿Qué dato de la herramienta desea actualizar?
                                       1)Nombre 
                                       2)Categoría
                                       3)Cantidad
                                       4)Estado
                                       5)Valor
                                       6)Cancelar
                                       : ''', 1,6)
            
            for elemento in registros:
                if elemento.get('id', 'ERROR')==id: 

                    match op_actualizar: 
                        case 1: 
                            elemento['nombre']= input('Ingrese el nombre de la herramienta: ')
                            
                        case 2: 
                            elemento['categoria']= categoria_herramienta()
                            
                        case 3: 
                            elemento['cantidad']= validar_numero('Ingrese la cantidad de herramientas: ')
                            
                        case 4: 
                            elemento['estado']= estado_herramienta()
                            
                        case 5: 
                            elemento['valor']= validar_numero('Ingrese el valor estimado a pagar en caso de pérdida o daño de la herramieta: ')
                        
                        case 6: 
                            break 

                    guardar(NOMBRE_ARCHIVO, registros)
                    print(F'HERRAMIENTA {elemento.get('nombre', 'ERROR')} ACTUALIZADA CORRECTAMETE ')
                    registrar_logs(F'La herramienta {elemento['nombre']} ha sido actualizada')
                    return 

                        
            print(f'EL ID {id} NO HA SIDO ENCONTRADO')       



def eliminar(): 
    registros=cargar(NOMBRE_ARCHIVO)

    if not registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA ELIMINAR ')
    
    else: 
        listar()
        id=validar_numero('Ingrese el ID de la herramienta a eliminar: ')

        for elemento in registros: 
            if elemento.get('id', 'ERROR')==id: 
                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO, registros)
                print(F'HERRAMIENTA {elemento.get('nombre', 'ERROR')} ELIMINADA CORRECTAMETE ')
                registrar_logs(F'La herramienta {elemento['nombre']} ha sido eliminada')
                return 
            
        print(f'EL ID {id} NO HA SIDO ENCONTRADO')  
                
            


def listar_herramienta():
    registros=cargar(NOMBRE_ARCHIVO)
    if not  registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA LISTAR')
    else: 
        encontrado=False

        for elemento in registros: 
            if elemento.get('estado')=='Activa'and elemento.get('cantidad')>0:
                encontrado=True
                print('-'*30)
                print(f'''
                        
                    ID de la herramienta: {elemento.get('id', 'ERROR')}
                    Nombre: {elemento.get('nombre', 'ERROR')}''')
        if not encontrado: 
            print('No hay herramientas activas o disponibles por el momento')








def validar_herramienta(id_herramienta):
    registros=cargar(NOMBRE_ARCHIVO)
    if not  registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA VALIDAR')
    else: 

        for elemento in registros:
            if elemento.get('id', 'ERROR')==id_herramienta and elemento.get('estado')=='Activa'and elemento.get('cantidad')>0:
                return elemento.get('nombre', 'ERROR')
        return False 
        








def listar_cantidades(id_herramienta):
    registros=cargar(NOMBRE_ARCHIVO)
    if not  registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA LISTAR')
    else: 

        for elemento in registros: 
        
            if elemento.get('id', 'ERROR')==id_herramienta:
                print('-'*30)
                print(f'''
                    Herramienta: {elemento.get('nombre', 'ERROR')}
                    Cantidad disponible: {round(elemento.get('cantidad', 'ERROR'))}''')
                



def cantidad_stock(id_herramienta, nombre_usuario):
    registros=cargar(NOMBRE_ARCHIVO)

    if not  registros: 
        print('NO HAY NINGUNA HERRAMIENTA PARA LISTAR')
    
    else:

        while(True):

           

            for elemento in registros: 
                if elemento.get('id', 'ERROR')==id_herramienta: 

                    solicitud_cantidad=validar_numero('Ingrese la cantidad que desea de la herramienta considerando su disponibilidad: ')

                    while solicitud_cantidad>elemento.get('cantidad', 'ERROR'): 
                        registrar_error_logs(f'Se intentó prestar más herramientas de {elemento.get('nombre', 'ERROR')} que las disponibles', nombre_usuario)
                        print('No hay suficiente de la herramienta')
                        print('Evento de intento inválido ha sido registrado')
                        solicitud_cantidad=validar_numero('Ingrese la cantidad que desea de la herramienta considerando su disponibilidad: ')
                    while solicitud_cantidad==0: 
                        registrar_error_logs(f'Se intentó prestar más herramientas de {elemento.get('mombre', 'ERROR')} que las disponibles', nombre_usuario)
                        print('Evento de intento inválido ha sido registrado')
                        return False
                        


                    ajustar_stock(id_herramienta, solicitud_cantidad, 'prestar') 
                    return solicitud_cantidad



          
            
def ajustar_stock(id_herramienta, solicitud_cantidad, accion): 
     registros=cargar(NOMBRE_ARCHIVO)

     for elemento in registros: 
         if elemento.get('id', 'ERROR')==id_herramienta: 
            cantidad_stock=elemento.get('cantidad', 'ERROR')
            if accion=='prestar':
                nueva_cantidad_stock=cantidad_stock-solicitud_cantidad
            if accion=='devolver':
                nueva_cantidad_stock=cantidad_stock+solicitud_cantidad

            elemento['cantidad']=nueva_cantidad_stock

            guardar(NOMBRE_ARCHIVO,registros)



    


            

    
            
                      

                
            
            
            



                           