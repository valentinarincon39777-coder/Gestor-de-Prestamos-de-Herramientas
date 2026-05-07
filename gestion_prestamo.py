
from datetime import date,timedelta, datetime

from validaciones import validar_menu, validar_numero
from gestion_json import *
from gestion_herramienta import listar_herramienta, validar_herramienta, listar_cantidades, cantidad_stock, ajustar_stock
from gestion_usuario import listar_usuario, validar_usuario
from logs import registrar_logs



NOMBRE_ARCHIVO='prestamos.json'


def menu_prestamos(nombre_usuario):

    while(True):
        print('-'*30)
        op_prestamo=validar_menu('''
                                    ---MENU PRESTAMO---
                                    1)Registrar préstamo
                                    2)Listar préstamos 
                                    3)Buscar préstamos
                                    4)Eliminar préstamo
                                    5)Salir del menú préstamo
                                    : ''',1,5)
        
        match op_prestamo: 
            
            case 1:
                registrar(nombre_usuario)
            
            case 2: 
                listar()
            case 3: 
                buscar()
            case 4: 
                eliminar()
               
            case 5: 

                break
                
            

         



def registrar(nombre_usuario): 
    registros=cargar(NOMBRE_ARCHIVO)

    prestamo={}


    prestamo['id']=generar_id(registros)
    prestamo['estado']='Activo'

    listar_usuario()
    id_usuario=validar_numero('Ingrese el ID del usuario al que se le prestará la herramienta: ')
    while(validar_usuario(id_usuario)==False): 
        id_usuario=validar_numero('EL ID NO HA SIDO ENCONTRADO. Intente nuevamente: ')

    prestamo['usuario']=validar_usuario(id_usuario)
    prestamo['id_usuario']=id_usuario
    





   



    listar_herramienta()
    id_herramienta=validar_numero('Ingrese el ID de la herramienta que se prestará: ')
    while(validar_herramienta(id_herramienta)==False): 
        id_herramienta=validar_numero(f'EL ID NO HA SIDO ENCONTRADO. Intente nuevamnete: ')
    prestamo['herramienta']=validar_herramienta(id_herramienta)
    prestamo['id_herramienta']=id_herramienta





    listar_cantidades(id_herramienta)
    prestamo['cantidad'] = cantidad_stock(id_herramienta, nombre_usuario)

        




    prestamo['fecha_prestamo']=str(date.today())

    prestamo['fecha_vencimiento']=str(fecha())




    prestamo['condicion']=condicion_herramienta()

    registro_herramienta=cargar('herramientas.json')
    for elemento in registro_herramienta:
        if elemento.get('id', 'ERROR')==id_herramienta:
            valor=elemento.get('valor')
    
    prestamo['valor_daño']=valor 


    prestamo['observaciones']=input('Observaciones adicionales: ')

    

    registros.append(prestamo)
    print(F'PRESTAMO PARA {prestamo['usuario']} INGRESADO CORRECTAMETE ')
    print(f'La fecha de máxima de entrega es: {prestamo['fecha_vencimiento']} ')

    registrar_logs(F'Al usuario {prestamo['usuario']} se le ha prestado la herramienta {prestamo.get('herramienta')}')

    

    guardar(NOMBRE_ARCHIVO, registros)












def fecha(): 

    print('El máximo de días para el préstamo de una herramienta es de 5 días')
    dias_prestamo=validar_numero('Ingrese la cantidad de días que necesita la herramienta: ')


    while dias_prestamo > 5: 
        dias_prestamo=validar_numero('No se le puede prestar más de 5 días. Ingrese una cantidad menor: ')



    fecha_vencimiento=date.today()+timedelta(days=dias_prestamo)

    return fecha_vencimiento





def condicion_herramienta():
   

        op_condicion=validar_menu('''
                               Ingrese el estado/condición en el cual se le entrega la herramienta al usuario: 
                               1)Nueva 
                               2)Excelente condición
                               3)Buena condición
                               4)Regular
                               ''',1,4)
        match op_condicion:
            case 1: 
                e='Nueva'
                
            case 2: 
                e='Excelente estado'
            case 3: 
                e='Buen estado'
            case 4: 
                e='Regular'

        return e



def listar(): 
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN PRESTAMO PARA LISTAR')
    else: 

        for elemento in registros: 
            print('-'*30)
            print(f'''   
                  ID del prestamo: {elemento.get('id', 'ERROR')}
                  Estado:{elemento.get('estado', 'ERROR')}
                  Usuario: {elemento.get('usuario', 'ERROR')}
                  Herramienta: {elemento.get('herramienta', 'ERROR')}
                  Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                  Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                  Condicion herramienta: {elemento.get('condicion', 'ERROR')}
                  Observaciones: {elemento.get('observaciones', 'ERROR')}''')




def buscar(): 

    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN PRESTAMO PARA BUSCAR')
    
    
    else: 
        while(True):
            id=validar_numero('Ingrese el ID deL préstamo a buscar: ')
            
            for elemento in registros: 
                if elemento.get('id', 'ERROR')==id: 
                    print('-'*30)
                    print(f'''
                        
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Estado:{elemento.get('estado', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Condicion herramienta: {elemento.get('condicion', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')
                        
                    return
            
            print(f'EL ID {id} NO HA SIDO ENCONTRADO')







def eliminar(): 
#en caso de ingresar un prestamo incorrecto y querer cancelarlo(borra registro en su totalidad y actualiza el stock)

    registros=cargar(NOMBRE_ARCHIVO)

    if not registros: 
        print('NO HAY NINGUN PRESTAMO PARA ELIMINAR')
    
    else: 
        listar()
        id=validar_numero('Ingrese el ID deL préstamo a eliminar: ')

        for elemento in registros: 
            if elemento.get('id', 'ERROR')==id: 
                id_herramienta=elemento.get('id_herramienta', 'ERROR')
                solicitud_cantidad=elemento.get('cantidad', 'ERROR')

                ajustar_stock(id_herramienta, solicitud_cantidad, 'devolver')
                

                registros.remove(elemento)
                guardar(NOMBRE_ARCHIVO, registros)
                print(F'PRESTAMO PARA {elemento['usuario']} ELIMINADO CORRECTAMETE ')
                registrar_logs(F'El préstamo del usuario {elemento['usuario']} para la herramienta {elemento['herramienta']} ha sido eliminado')

                return 
            
        print(f'EL ID {id} NO HA SIDO ENCONTRADO')  



def devolucion():

    registros=cargar(NOMBRE_ARCHIVO)

    if not registros: 
        print('NO HAY NINGUN PRESTAMO')
    
    else: 
        listar_devolucion()
        id=validar_numero('Ingrese el ID deL préstamo: ')
        for elemento in registros: 
            if elemento.get('id', 'ERROR')==id: 

                print('-'*30)
                print(f'''
                        
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Estado:{elemento.get('estado', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Condicion herramienta: {elemento.get('condicion', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')
                        

                id_herramienta=elemento.get('id_herramienta', 'ERROR')
                solicitud_cantidad=elemento.get('cantidad', 'ERROR')

                ajustar_stock(id_herramienta, solicitud_cantidad, 'devolver')


                fecha_vencimiento= datetime.strptime(elemento.get('fecha_vencimiento'), "%Y-%m-%d").date()
                #datetime.strptime(texto, FORMATO)
                #convierte el texto (archivo json fecha_vencimiento se guardo como string) otra vez en una fecha real, del tipo <class 'datetime.date'>.
                #strp---string parse time
                '''
                    %Y  → año
                    %m  → mes
                    %d  → día

                    y podemos el .date() ya que strptime devuelve un datetime que incluye hora, pero aqui solo queremos la fecha
                '''

                if  date.today() <= fecha_vencimiento: 
                    # para date.today() Python usa el formato ISO 8601, que es el estándar internacional: YYYY-MM-DD
                    print('Usuario puntual.No se le aplicará multa. ')
                else: 

                    print('Usuario impuntual. Tiene una multa de $10.00')

                op_daños=validar_menu('''¿La herramienta es devuelta con daños graves o fue perdida?
                                        1)SI, HAY DAÑOS O PERDIDA 
                                        2)NO, NO HAY DAÑOS NI PERDIDA
                                        >Ingrese el número correspondiente:   ''',1,2)
                
                match op_daños: 
                    case 1: 
                         print(f'El precio a pagar por daños/pérdida de la herramienta {elemento.get('herramienta', 'ERROR')} es de ${elemento.get('valor_daño', 'ERROR')}')


                    case 2: 
                         print('No tiene recargos adicionales por pérdida o daño')

                 
                   
                elemento['estado']='Inactivo'
                guardar(NOMBRE_ARCHIVO, registros)
                print(F'EL USUARIO {elemento['usuario']} HA REALIZADO LA CORRECTA DEVOLUCION DE LA HERRAMIENTA  ')
                registrar_logs(F'El usuario {elemento['usuario']} hizo la correcta devolución de la herramienta {elemento['herramienta']}')
                return 
            
            
        print(f'EL ID {id} NO HA SIDO ENCONTRADO')  








def listar_devolucion(): 
    registros=cargar(NOMBRE_ARCHIVO)
    if not registros: 
        print('NO HAY NINGUN PRESTAMO PARA LISTAR')
    else: 

        encontrado=False

        for elemento in registros: 
            if elemento.get('estado')=='Activo':
                encontrado=True
                print('-'*30)
                print(f'''   
                    ID del prestamo: {elemento.get('id', 'ERROR')}
                    Estado:{elemento.get('estado', 'ERROR')}
                    Usuario: {elemento.get('usuario', 'ERROR')}
                    Herramienta: {elemento.get('herramienta', 'ERROR')}
                    Cantidad : {round(elemento.get('cantidad', 'ERROR'))}
                    Fecha de vencimiento: {elemento.get('fecha_vencimiento', 'ERROR')}
                    Condicion herramienta: {elemento.get('condicion', 'ERROR')}
                    Observaciones: {elemento.get('observaciones', 'ERROR')}''')
        if not encontrado: 
            print('No hay préstamos activos en este momento')
                




      














































    