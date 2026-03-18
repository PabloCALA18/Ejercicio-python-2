""""3.Escribe un programa que muestra la primer,
última u otra letra de una cadena de carcateres,
inclusive una rebanada.
"""
#cadena[inicio:fin]

palabra = input("Ingresa una palabra: ")

print("Selecciona lo que querés hacer \n 1.Si queres la primera letra \n 2.Si querés la última letra \n 3.Si queres la palbra rebanada \n 4.Si querés desde un número")
n = int(input("Ingresa el número: "))

if n == 1:
    print(palabra[0])
if n == 2:
    print(palabra[-1])
if n == 3:
    inicio = int(input("Inicio del corte: "))
    fin = int(input("Fin del corte: "))
    print(palabra[inicio:fin])
if n == 4:
    inicio = int(input("Ingresa el número de inicio: "))
    print(palabra[inicio:])
