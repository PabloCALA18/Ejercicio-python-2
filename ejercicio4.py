""""3.Escribe un programa que muestra la primer,
última u otra letra de una cadena de carcateres,
inclusive una rebanada.
"""
#cadena[inicio:fin]

palabra = input("Ingresa una palabra: ")

print("\n \n Selecciona lo que querés hacer \n 1.Si queres la primera letra \n 2.Si querés la última letra \n 3.Si queres la palabra rebanada \n 4.Si querés desde un número \n 5.Si querés hasta un número \n 6.Si queres un intervalo \n 7.Si querés toda la palabra \n 8.Si queres una letra en específico \n 9.Si querés la palabra al revés \n")
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
if n == 5:
    fin = int(input("Ingresa el número de fin: "))
    print(palabra[:fin])
if n == 6:
    inicio = int(input("Ingresa el número de inicio: "))
    fin = int(input("Ingresa el número de fin: "))
    print(palabra[inicio:fin])
if n == 7:
    print(palabra)
if n == 8:
    pos = int(input("Ingresa el número de la letra que querés: "))
    print(palabra[pos])
if n == 9:
    print(palabra[::-1])
