
seguir = 'si'

def opciones():
    
    while seguir == 'si':

        print(f'Opciones para hallar raiz cuadrada \n (1)Enumeracion Exhaustiva \n (2) aproximacion de soluciones \n (3) Busqueda Binaria')
        
        
        opcion = int(input('Elija una opcion: '))
        numero = int(input('Elija un numero: '))

        if opcion == 1:
             Enumeracion(numero)
        elif opcion == 2:
            Aproximacion(numero)
        elif opcion == 3:
             Busquedabinaria(numero)
        else:
            print('Elija 1, 2 o 3')
    

def Enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
            print(respuesta)
            respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        seguir =input('Desea probar otro numero o metodo ? Digite si para continuar, No para salir: ')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')
        seguir =input('Desea probar otro numero o metodo ? Digite si para continuar, No para salir: ')
        
    


def Aproximacion(objetivo):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs (respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso 
    
    if abs(respuesta**2 - objetivo) >= epsilon:
        print (f'No se encontro la raiz cuadrada {objetivo}')
        seguir =input('Desea probar otro numero o metodo ? Digite si para continuar, No para salir: ')
    else:
        print (f'La raiz cuadrada de {objetivo} es aproximadamente {respuesta}')
        seguir =input('Desea probar otro numero o metodo ? Digite si para continuar, No para salir: ')

def Busquedabinaria(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs (respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')

        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo)/2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    seguir =input('Desea probar otro numero o metodo ? Digite si para continuar, No para salir: ')

  

    

opciones()




    



