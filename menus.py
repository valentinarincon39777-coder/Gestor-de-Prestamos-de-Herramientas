from validaciones import validar_menu
from gestion_herramienta import menu_herramientas
from gestion_usuario import menu_usuarios
from gestion_prestamo import menu_prestamos,  devolucion
from gestion_consulta import menu_consultas
from gestion_residente import catalogo_herramientas, proxima_disponibilidad



def menu_admin(nombre_usuario):

    while (True):
        print('-'*30)
        op_admin = validar_menu('''
                                    ---MENU ADMINISTRADOR ---
                                    1)Gestionar herramientas
                                    2)Gestionar usuarios
                                    3)Gestionar préstamos
                                    4)Gestionar devolución
                                    5)Consultas y reportes
                                    6)Salir del menú administrador
                                    : ''', 1, 6)

        match op_admin:

            case 1:
                menu_herramientas()
            case 2:
                menu_usuarios()
            case 3:
                menu_prestamos(nombre_usuario)
            case 4:
                devolucion()
            case 5:
                menu_consultas()
            case 6:
                break




def menu_residente():

    while (True):
        print('-'*30)
        op_residente = validar_menu('''
                                    ---MENU RESIDENTE---
                                    1)Catálogo de herramientas activas y disponibles
                                    2)Conocer próxima disponibilidad de herramientas NO disponibles
                                    3)Salir del menú residente
                                    : ''', 1, 3)

        match op_residente:

            case 1:
                catalogo_herramientas()
            case 2:
                proxima_disponibilidad()
            case 3:
               break 
    
