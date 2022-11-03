# Conceptos de String en Python
'123' * 3
# Esta es la multipliccion de la cadena Strin '' tres veces, no siendo una operacion matematica
'123' + '456'
# Esta siendo la Concatenacion de las dos cadenas de String
('Hip' * 3) + '' + 'Hurra'
# Esta Linea, siendo el conjunto del ejemplo de las dos anteriores con un espacio en blanco '', y la formacion de la frase conocida Hip Hip Hip Hurra, como resultado 
f'{"Hip " *3} Hurra'
# Esta como la manera simplificada dentro del lenguaje de Python para ejecutar la frase anteriormente dicha 

# Otros ejemplos y el uso de len, al igual que la division por caracteres

my_str = 'Platzi'

len(my_str)

# El comando len utilizado para mostrar el numero de cracteres contiene la palabra Platzi
my_str[0]
# Este comando nos muestra el caracter en la posicion 0, comenzando de izq a der, y commenzando desde 0,1,2 ...
my_str[1]
my_str[2:]
# La estructura del comando significa my_str[comienzo:fin:pasos], siendo el del anterior desde el caracter en la posicion 2 hasta el final de la misma la que muestra.
my_str[::2]
# Por ejemplo este muestra cada 2 pocisiones el caracter que se encuentra en el mismo.

nombre = input ('Cual es tu Nombre: ')
# La creciacion de variables por ingreso de datos tipo strong
nombre
print(nombre)
# imprimme en pantalla el valor de la variable ingresada por el usuario asignada a nombre
print('Tu nombre es ', nombre)

print (f'Tu nombre es {nombre}')

# Si ejecutamos este input sin clasificar el tipo de dato a ingresar, este se tomara uniicamente como STRONG, por lo que si necesitamos otro tipo de dato cambia su sintaxis

numeroStrong = input('Esribe un numero: ')
#suma = numeroStrong + 5 
#print(suma)
# Este dara como resultado el error de sintaxis

numeroint = int(input('Escribe un numero: '))

suma1 = numeroint + 5
print(suma1)






