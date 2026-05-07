

def validar_numero(mensaje): 
    
    while(True):
        try:
            numero=int(input(mensaje))
            while numero < 0 or numero >  99999999 : 
                print('ERROR, SOLO SE ADMITEN NUMEROS POSITIVOS DE HASTA DE 8 DÍGITOS')
                numero=int(input(mensaje))
            return numero
        except Exception: 
            print('ERROR, SOLO SE ADMITEN NUMEROS')





def validar_menu(mensaje, min,max):
    op=validar_numero(mensaje)
    while op<min or op>max:
        print('ERROR OPCION NO VALIDA, INTENTE NUEVAMNETE')
        op=validar_numero(mensaje)
    return op
