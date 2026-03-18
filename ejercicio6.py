n = int(input("Ingresa cuantos números querés agregar a una lista: "))
array = []
lista = []
tipo = ""

for i in range(n):
    number = int(input("Ingresa un numero: "))
    array.append(number)

print("Queres los numeros: \n 1.Impares \n 2.Pares")
x = int(input("Ingresa tu opción: "))

if x == 1:
    tipo = "impares"
    for num in array:
        if num % 2 != 0:
            lista.append(num)
else:
    tipo = "pares"
    for num in array:
        if num % 2 == 0:
            lista.append(num)

lista.sort(reverse=False)
print(f"Los números {tipo} que ingresaste son: {lista}")

