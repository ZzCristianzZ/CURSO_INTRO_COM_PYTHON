# Lista
nombres =["Juan", "Ana", "Elena"]
print ("El tipo de nombre es ", type(nombres))
for nombre in nombres:
    print("Buenos dias ", nombre)

# Tuple
nombres =("Juan", "Ana", "Elena")
print ("El tipo de nombre es ", type(nombres))
for nombre in nombres:
    print("Buenos dias ", nombre)


# Set, el orden de los elementos no se mantiene
nombres ={"Juan", "Ana", "Elena"}
print ("El tipo de nombre es ", type(nombres))
for nombre in nombres:
    print("Buenos dias ", nombre)

# Diccionario

nombres ={"Juan":1, "Ana":2,"Elena":3}
print ("El tipo de nombre es ", type(nombres))
for nombre, valor in nombres.items():
    print("Buenos dias ", nombre, valor)

print("ITERAR CON NUMEROS, SOLO CON UN ARGUMENTO")

# para iterar con numeros con <range>
# Este significa que iteramos desde cero hasta el numero 10 sin incluir el 10 

for i in range(10):
    print(i)

# imprime los numeros del 0 al 9 

print("ITERAR CON DOS ARGUMENTOS DE UN NUMERO A OTRO NUMERO FINAL SIN INCLUIRLO")

#Para ejecutarlo con numero incial y un numero final

for x in range(3,11):
    print(x)

# Imprime desde el numero 3 hasta el numero 10

print("ITERAR CON TRES ARGUMENTOS ESTABLECIENDO EL PASO COSECUTIVO, EN ESTE CASO DE 2 EN 2")

# Para ejecutarlo con un paso consecutivo diferente (Ejemplo de 2 en 2)

for y in range(3,11,2):
    print(y)



