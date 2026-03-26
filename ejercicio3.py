""""2.1. Escribe un programa que solicita al usuario
que ingrese números enteros positivos y muestre
la suma de esos números. La entrada de números
continuará hasta que el usuario ingrese un 
número negativo, momento en el que el programa 
mostrará la suma total."""

print("BIENVENIO \n Ingrese números enteros positivos. Para finalizar, ingrese un número negativo.")
num = int(input("Ingrese un numero: "))
acum = num
while num > 0:
   num = int(input("Ingrese un numero: "))
   acum += num
   # Si el número ingresado es negativo, se resta del acumulador para no incluirlo en la suma.
acum -= num
print(f"La suma de todos esos números es {acum}")

