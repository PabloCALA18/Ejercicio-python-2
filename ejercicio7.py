"""""Escribe un programa que recorra una cadena de 
texto y cuente cuántas veces aparece la letra 'a' en la cadena."""

acum = 0

palabra = input("Ingresa una palabra: ")
x = input("Ingresa una letra, para ver cuántas veces se repite: ")

for i in palabra:
    if i == x:
        acum+=1

if acum == 0:
    print(f"La letra {x} no se está en la palabra")
elif acum == 1:
    print(f"La letra {x} está 1 vez en la palabra")
elif acum > 1:
    print(f"La letra {x} se repite {acum} veces en la palabra")