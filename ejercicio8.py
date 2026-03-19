""""8. Integrador:
Escribe un programa que permita a un usuario crear
una lista de nombres. El programa continuará pidiendo
nombres hasta que el usuario ingrese "fin". Luego, 
el programa mostrará la lista de nombres en orden alfabético,
indicará cuántos nombres empiezan con la letra 'A' o 'E', 
y mostrará si un nombre específico está en la lista."""

print("Ingresa nombres, cuando termines escribi (fin):  ")
v = "inicio"
nombreBuscado = ""
acum = 0
nombres = []
nombresA = []
nombresE = []
while v == "inicio":
    nombre = input("Ingresa un nombre:  ")
    nombres.append(nombre)
    if nombre == "fin":
        v = "fin"

nombres.remove(nombres[-1])
nombres.sort()

for name in nombres:
    if name[0] == "A":
        nombresA.append(name)
for name in nombres:
    if name[0] == "E":
        nombresE.append(name)

verificar = input("Busca un nombre: ")
for name in nombres:
    if name == verificar:
        acum += 1
        nombreBuscado = name
        print(f"El nombre {nombreBuscado} está en la lista")

if acum == 0:
     print(f"El nombre {nombreBuscado} no está en la lista")

print(f"Los nombres que ingresaste son: {nombres} \n Los que empiezan con A : {nombresA} \n Los que empiezan con E : {nombresE} ")