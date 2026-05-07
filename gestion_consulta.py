

from validaciones import validar_menu
from gestion_json import *
from datetime import datetime, date
from gestion_usuario import listar_usuario



def menu_consultas():
    while (True):
        print('-'*30)
        op_consulta = validar_menu('''
                                    ---MENU REPORTES Y CONSULTAS---
                                    1)Herramientas con stock bajo
                                    2)Préstamos activo 
                                    3)Prestamos vencidos
                                    4)Historial de préstamo de usuario
                                    5)Herramientas más solicitadas
                                    6)Usuarios que más herramientas solicitan
                                    7)Registro de eventos del día 
                                    8)Registro de intentos inválidos del día
                                    9)Salir del menú reportes y consultas
                                    : ''', 1, 9)

        match op_consulta:

            case 1:
                stock_bajo()

            case 2:
                prestamos_activos()

            case 3:
                prestamos_vencidos()

            case 4:
                historial_usuario()

            case 5:
                herramientas_solicitadas()

            case 6:
                usuarios_solicitantes()

            case 7: 
                logs()
            
            case 8:
                logs_errores()

            case 9:

                break


def stock_bajo():
    registros = cargar('herramientas.json')
    if not registros:
        print('NO HAY NINGUNA HERRAMIENTA PARA BUSCAR')

    else:
            encontrado=False

            for elemento in registros:
                if elemento.get('cantidad') < 3:
                    encontrado=True
                    print(f'''
                    ID de la herramienta: {elemento.get('id', 'ERROR')}
                    Nombre: {elemento.get('nombre', 'ERROR')}
                    Categoría: {elemento.get('categoria', 'ERROR')}
                    Cantidad: {elemento.get('cantidad', 'ERROR')}
                    Estado: {elemento.get('estado', 'ERROR')}
                    Valor: ${elemento.get('valor', 'ERROR')}''')
                    
            if not encontrado: 
                print('No hay herramientas con stock bajo(<3)')
                


def prestamos_activos():
    registros = cargar('prestamos.json')
    if not registros:
        print('NO HAY NINGUN PRESTAMO PARA BUSCAR')

    else:

        encontrado = False

        for elemento in registros:
            if elemento.get('estado', 'ERROR') == 'Activo':

                encontrado = True

                print('-'*30)
                print(f'''
                        
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Estado herramienta: {elemento.get('valor_daño', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')

        if not encontrado:
            print('No hay préstamos activos')

            


def prestamos_vencidos():
    registros = cargar('prestamos.json')
    if not registros:
        print('NO HAY NINGUN PRESTAMO PARA BUSCAR')

    else:

        encontrado = False

        for elemento in registros:
            fecha = datetime.strptime(elemento.get(
                'fecha_vencimiento'), "%Y-%m-%d").date()

            if fecha < date.today() and elemento.get('estado', 'ERROR')=='Activo': 
                encontrado = True
                print('-'*30)
                print(f'''
                        
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Estado herramienta: {elemento.get('valor_daño', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')

        if not encontrado:
            print('No hay préstamos vencidos')


def historial_usuario():
    registros = cargar('prestamos.json')
    if not registros:
        print('NO HAY NINGUN PRESTAMO PARA BUSCAR')

    else:

        listar_usuario()
        id_usuario = int(
            input('Ingrese el ID del usuario del cuál desea su historial: '))

        encontrado = False

        for elemento in registros:

            if elemento.get('id_usuario', 'ERROR') == id_usuario:

                if not encontrado:

                    print(
                        f'HISTORIAL DEL USUARIO: {elemento.get('usuario', 'ERROR')} A CONTINUACION')

                encontrado = True

                print('-'*30)
                print(f'''
                        
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Estado:{elemento.get('estado', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Estado herramienta: {elemento.get('valor_daño', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')

        if not encontrado:
            print(f'EL ID {id_usuario} NO HA SIDO ENCONTRADO')




def herramientas_solicitadas():
    registros = cargar('prestamos.json')
    if not registros:
        print('NO HAY NINGUNA HERRAMIENTA PARA LISTAR')

    else:
        encontrado = False

        conteo_herramientas = {}

        for elemento in registros:

            herramienta = elemento.get('herramienta', 'ERROR')

            if herramienta in conteo_herramientas:

                conteo_herramientas[herramienta] += 1

            else:
                conteo_herramientas[herramienta] = 1

        for herramienta, cantidad in conteo_herramientas.items():
            if cantidad >= 5:
                encontrado = True
                print(f'''
                      Nombre de la herramienta: {herramienta}
                      Cantidad de veces solicitada: {cantidad}''')
        if not encontrado:
            print('No hay ninguna herramienta demasiado solicitada(más de 5 veces)')





def usuarios_solicitantes():
    registros = cargar('prestamos.json')
    if not registros:
        print('NO HAY PRESTAMOS PARA LISTAR')

    else:
        encontrado = False

        conteo_usuarios = {}

        for elemento in registros:

            usuario = elemento.get('usuario', 'ERROR')

            if usuario in conteo_usuarios:

                conteo_usuarios[usuario] += 1

            else:
                conteo_usuarios[usuario] = 1

        for usuario, cantidad in conteo_usuarios.items():

            if cantidad >= 5:

                encontrado = True

                print(f'''
                  Nombre del usuario: {usuario}
                  Cantidad de préstamos solicitados: {cantidad}''')

        if not encontrado:
            print(
                'No hay ningún usuario con demasiados préstamos solicitados(más de 5 préstamos)')



def logs():
    registros=cargar('logs.json')
    if not registros: 
        print('NO HAY REGISTROS HASTA EL MOMENTO')

    else: 
        encontrado=False 

        for elemento in registros: 
            fecha_log=datetime.strptime(elemento.get('hora'), '%Y-%m-%d %H:%M:%S').date()

            if fecha_log == date.today(): 
                encontrado=True
                print('-'*30)
                print(f'''
                      Descripción: {elemento.get('descripcion')}
                      Momento exacto del evento: {elemento.get('hora')}
'''
                      )
        
        if not encontrado:
            print('No hay registro de eventos el día de hoy')




def logs_errores():
    registros=cargar('logs_error.json')
    if not registros: 
        print('NO HAY REGISTROS DE EVENTOS DE INTENTOS INVALIDOS HASTA EL MOMENTO')

    else: 
        encontrado=False 

        for elemento in registros: 
            fecha_log=datetime.strptime(elemento.get('hora'), '%Y-%m-%d %H:%M:%S').date()

            if fecha_log == date.today(): 
                encontrado=True
                print('-'*30)
                print(f'''
                      Descripción: {elemento.get('descripcion')}
                      Momento exacto del evento: {elemento.get('hora')}
                      Usuario responsable del intento inválido: {elemento.get('usuario')}
'''
                      )
        
        if not encontrado:
            print('No hay registro de eventos de intentos inválidos el día de hoy')











