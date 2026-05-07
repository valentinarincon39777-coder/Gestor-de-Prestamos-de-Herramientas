
from validaciones import validar_menu, validar_numero
from menus import menu_admin, menu_residente
from logs_examen import registrar_error_logs
from gestion_usuario import registrar
from gestion_json import *


print('-'*60)



def usuario():
    registros=cargar('usuarios.json')
    if not registros: 
        print('NO HAY REGISTROS DE USUARIOS')
    else:  
        encontrado=False 

        usuario=input(' Ingrese su nombre de usuario, por favor: ')

        for elemento in registros: 
            if usuario==elemento.get('nombre_usuario', 'ERROR'): 
                encontrado=True
                print(f'BIENVENIDO {elemento.get('nombre', 'ERROR')} ')

        if not encontrado: 
            print('NOMBRE DE USUARIO NO ENCONTRADO. Ingréselo correctamente o en caso de no estar registrado, acuda al administrador para generar su nombre de usuario')
            return None
            
    return usuario








def main(nombre_usuario): 

    while (True):

            op_inicio = validar_menu('''
                                Ingrese su rol: 
                                1)Administrador 
                                2)Residente
                                3)Salir
                                : ''', 1, 3)
            match op_inicio:
                case 1:
                    contraseña = 123
                    contraseña_dada = validar_numero(
                        'Ingrese la contraseña de administrador: ')
                    if contraseña == contraseña_dada:
                        print('Contraseña correcta')
                        menu_admin(nombre_usuario)
                    else:
                        print(
                            'Contraseña incorrecta. Si usted no es administrador no puede ingresar.')

                        registrar_error_logs(
                            'Se intentó fallidamente entrar al sistema de administrador', nombre_usuario)
                        print('Evento de intento inválido ha sido registrado')

                case 2:
                    menu_residente()

                case 3:
                    break






while True: 
    op_inicio_sesion=validar_menu('''CONTROL DE PRESTAMOS DE HERRAMIENTAS PARA VECINOS DEL BARRIO SANTA ANA
                                  1)Ingresar nombre de usuario
                                  2.Salir
                                  >> ''', 1,2)
    match op_inicio_sesion: 
        case 1: 
            
            nombre_usuario=usuario()

            if nombre_usuario != None:
                main(nombre_usuario)


        case 2: 
            break 

