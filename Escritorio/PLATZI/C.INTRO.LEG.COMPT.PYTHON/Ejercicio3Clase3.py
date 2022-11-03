print("Bienvenido al comparador de edades. ")
print("Ahora descubriremos juntos quie tiene mas edad entre dos personas.")
print("Para esto necesitare que me brindes informacion antes")

nombre_persona1 = input ("Necesito el nombre de la primera persona, por favor digitalo: ")
edad_persona1 = int (input ("Que edad tienes "))

nombre_persona2 = input("Necesito el nombre por favor de la segunda Persona. Digitalo por favor : ")
edad_persona2 = int(input("Que edad tienes "))

print("Despejare la incertidumbre...")

if edad_persona1 > edad_persona2:
    print(f"Claro como el agua, {nombre_persona1} es mayor que {nombre_persona2}.")
elif edad_persona1 < edad_persona2:
     print(f"!Elemental Watson!, {nombre_persona2} es mayor que {nombre_persona2}.")
else:
    print(f"Basta de Contiendas {nombre_persona1} y {nombre_persona2}, ambos tienen la misma edad!")

print("Gracias por usar este programa.!Nos vemos la proxima! creditos : ezequiel_pettinari Platzi")


