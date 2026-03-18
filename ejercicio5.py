"""5. Escribe un programa que recorra una lista de 
frutas y muestre cada fruta."""

"""""5.1 Agregar otras frutas a la lista."""

"""""5.2 Escribe un programa verifique si una fruta 
específica está en una lista de frutas y muestra
un mensaje correspondiente."""

frutas = [
    "Manzana", "Banana", "Naranja", "Pera", "Uva",
    "Mango", "Ananá", "Frutilla", "Durazno", "Cereza",
    "Kiwi", "Sandía", "Melón", "Limón", "Mandarina"
]
print(f"Las frutas son {frutas}")
ask = ""
i = 0
print("Selecciona lo que querés hacer \n 1.Si queres la primera fruta \n 2.Si querés la última fruta \n 3.Si queres las frutas rebanadas \n 4.Si querés desde un fruta \n 5.Si queres agregar una fruta \n 6.Verificar si hay una fruta")
n = int(input("Ingresa el número: "))

if n == 1:
    print(frutas[0])
if n == 2:
    print(frutas[-1])
if n == 3:
    inicio = int(input("Inicio del corte: "))
    fin = int(input("Fin del corte: "))
    print(frutas[inicio:fin])
if n == 4:
    inicio = int(input("Inicio del corte: "))
    print(frutas[inicio:])
if n == 5:
    nueva = input("Ingresa una nueva fruta: ")
    frutas.append(nueva)
    print(frutas)
if n == 6:
    ask = input("Pregunta que fruta hay: ")
    for fruta in frutas:
        if ask == fruta:
            print(f"La fruta {ask} está en el arreglo")
            i += 1
    if i == 0:
            print(f"La fruta {ask} no está en el arreglo")

