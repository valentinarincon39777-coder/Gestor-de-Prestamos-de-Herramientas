
from validaciones import validar_menu, validar_numero
from gestion_json import *
from logs import registrar_logs


NOMBRE_ARCHIVO='usuarios.json'

def menu_usuarios():

    while(True):
        print('-'*30)
        op_usuarios=validar_menu('''
                                    ---MENU USUARIOS---
                                    1)Registrar usuarios
                                    2)Listar usuarios
                                    3)Buscar usuarios
                                    4)Actualizar usuarios
                                    5)Eliminar o incativar usuarios
                                    6)Salir del menú usuarios
                                    : ''',1,6)
        
        match op_usuarios: 
            
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
    usuario={}

    usuario['id']=generar_id(registros)
    usuario['nombre']=input('Ingrese el nombre del usuario: ')
    usuario['apellido']=input('Ingrese los apellidos del usuario: ')
    usuario['telefono']=validar_numero('Ingrese el teléfono del usuario: ')
    usuario['direccion']=validar_numero('Ingrese el número de la vivienda del usuario: ')
    usuario['nombre_usuario']=input('Ingrese el nombre de usuario del vecino: ')
    usuario['tipo']=tipo_usuario()

    registros.append(usuario)
    guardar(NOMBRE_ARCHIVO, registros)
    print(F'USUARIO {usuario['nombre']} INGRESADO CORRECTAMENTE ')
    registrar_logs(F'El usuario {usuario['nombre']} ha sido registrado')


def tipo_usuario(): 
    op_tipo=validar_menu('''
    Ingrese el número al cual pertenece el tipo de usuario:
                              1)Residente
                              2)Administrador
                              
                              : ''',1,2)
    match op_tipo: 
        case 1: 
            h='Residente'
        case 2: 
            h='Administrador'
 
    return h

def listar():
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN USUARIO PARA LISTAR')
    else: 

        for elemento in registros: 
            print('-'*30)
            print(f'''
                       
                  ID del usuario: {elemento.get('id', 'ERROR')}
                  Nombre: {elemento.get('nombre', 'ERROR')}
                  Apellidos: {elemento.get('apellido', 'ERROR')}
                  Teléfono: {round(elemento.get('telefono', 'ERROR'))}
                  Número de vivienda: {round(elemento.get('direccion', 'ERROR'))}
                  Nombre de usuario: {elemento.get('nombre_usuario', 'ERROR')}

                  Tipo: {elemento.get('tipo', 'ERROR')}''')
            




            
def buscar(): 
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN USUARIO PARA BUSCAR')
    
    
    else: 
        while(True):
            id=validar_numero('Ingrese el ID deL usuario a buscar: ')
            
            for elemento in registros: 
                if elemento.get('id', 'ERROR')==id: 
                    
                    print(f'''
                    ID del usuario: {elemento.get('id', 'ERROR')}
                    Nombre: {elemento.get('nombre', 'ERROR')}
                    Apellidos: {elemento.get('apellido', 'ERROR')}
                    Teléfono: {elemento.get('telefono', 'ERROR')}
                    Número de vivienda: {elemento.get('direccion', 'ERROR')}
                    Nombre de usuario: {elemento.get('nombre_usuario', 'ERROR')}
                    Tipo: {elemento.get('tipo', 'ERROR')}''')
                    return 
            
            print(f'EL ID {id} NO HA SIDO ENCONTRADO')





def actualizar(): 

    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN USUARIO PARA ACTUALIZAR')
    
    
    else: 
        while(True):
            listar()
            id=validar_numero('Ingrese el ID del usuario a actualizar: ')

            op_actualizar=validar_menu('''¿Qué dato del usuario desea actualizar?
                                       1)Nombre 
                                       2)Apellido
                                       3)Teléfono
                                       4)Direccion
                                       5)Tipo
                                       6)Nombre de usuario
                                       7)Cancelar
                                       : ''', 1,7)
            
            for elemento in registros:
                if elemento.get('id', 'ERROR')==id: 

                    match op_actualizar: 
                        case 1: 
                            elemento['nombre']= input('Ingrese el nombre del usuario: ')
                            
                        case 2: 
                            elemento['apellido']=input('Ingrese los apellidos del usuario: ')
                            
                        case 3: 
                            elemento['telefono']=validar_numero('Ingrese el teléfono del usuario: ')
                            
                        case 4: 
                            elemento['direccion']=validar_numero('Ingrese el número de la vivienda del usuario: ')
                            
                        case 5: 
                            elemento['tipo']= tipo_usuario()
                        
                        case 6: 
                            elemento['nombre_usuario']=input('Ingrese el nombre de usuario del vecino: ')
                        case 7: 
                            break 

                    guardar(NOMBRE_ARCHIVO, registros)
                    print(F'USUARIO {elemento.get('nombre', 'ERROR')} ACTUALIZADO CORRECTAMETE ')
                    registrar_logs(F'El usuario {elemento['nombre']} ha sido actualizado')



                    return 

                        
            print(f'EL ID {id} NO HA SIDO ENCONTRADO')  




def eliminar(): 
    registros=cargar(NOMBRE_ARCHIVO)

    if not registros: 
        print('NO HAY NINGUN USUARIO PARA ELIMINAR')
    
    else: 
        listar()
        id=validar_numero('Ingrese el ID deL usuario a eliminar: ')

        for elemento in registros: 
            if elemento.get('id', 'ERROR')==id: 
                registros.remove(elemento)
                

                guardar(NOMBRE_ARCHIVO, registros)
                print(F'USUARIO {elemento.get('nombre', 'ERROR')} ELIMINADO CORRECTAMETE ')
                registrar_logs(F'El usuario {elemento['nombre']} ha sido eliminado')
               
                return 
            
        print(f'EL ID {id} NO HA SIDO ENCONTRADO')   







       

def listar_usuario():
    registros=cargar(NOMBRE_ARCHIVO)
    if not  registros: 
        print('NO HAY NINGUN USUARIO PARA LISTAR')
    else: 

        for elemento in registros: 
            print('-'*30)
            print(f'''
                       
                  ID del usuario: {elemento.get('id', 'ERROR')}
                  Nombre: {elemento.get('nombre', 'ERROR')} {elemento.get('apellido', 'ERROR')} ''')





def validar_usuario(id_usuario):
    registros=cargar(NOMBRE_ARCHIVO)
    if not  registros: 
        print('NO HAY NINGUN USUARIO PARA VALIDAR')
        

    else: 
        for elemento in registros:
            if elemento.get('id', 'ERROR')==id_usuario:
              
                 
                 return (f'{elemento.get('nombre', 'ERROR')} {elemento.get('apellido', 'ERROR')}')
        return False 
            
        
