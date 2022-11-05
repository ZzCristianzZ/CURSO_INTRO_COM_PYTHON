# Primer ejercicio

contador = 0 
while contador <=10:
    print(contador)
    contador +=1 # Contador = contador + 1

# Segundo ejercicio

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print(contador_externo, contador_interno)
        contador_interno += 1
    
    contador_externo += 1
    contador_interno = 0


# Ejemplos bucle for con iteraciones.

## Usando bucle for en diccionarios

estudiantes = { #diccionario estudiantes por que tiene llaves
'mexico': 10, #Mexico es la llave 0, y el numero 10 es us valor 
'colombia':15, #Colombia es la llave 1, y el numero 15 es su valor
'puerto_rico':4 #Puerto Rico es la llave 2 y el numero 4 es su valor.
}

for pais in estudiantes : # Este iter repite la expresion con cada llave o  en este caso pais.
    print(pais) # esta expresion imprime cada pais.
for pais in estudiantes.keys():#Este iter hace totalmente lo mismo que el anterior.
    print(pais)
for numero_de_estudiantes in estudiantes.values(): #Extrae cada valor del diccionario, el de la derecha de la llave, y repite la expresion con cada valor.
    print(pais)
for pais, numero_de_estudiantes in estudiantes.items(): # Usar la llave y el valor en la forma lejible de imprimir.
    print(f'en {pais} hay {numero_de_estudiantes} estudiantes activos')


# Reto 
# Persona, comida favorida

diccionario = {
    'Rubi' : 'Los Chitos',
    'Ismael': 'La Pizza',
    'Perla' : 'El Sancocho',
    'Migue':'El arroz Con Pollo',
    'Enrique':'El arroz con berenjena'
}
 # Imprimir una frase que incluya la llava y el valor 

for nombre, comida in diccionario.items():
    if comida[-1] == 's':
        singular_o_plural = 'Gustan'
    else:
        singular_o_plural = 'Gusta'
    print(f'A {nombre} le {singular_o_plural} {comida}.')