objetivo = int(input('Escoje un numero: '))
epsilon = 0.1
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(respuesta, abs(respuesta**2 - objetivo))
    respuesta += paso

if abs(respuesta**2 - objetivo)>= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

