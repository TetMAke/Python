"""Realice un algoritmo que lea un número y muestre si el mismo es positivo, negativo o cero."""

num=int(input("Digite un numero: "))

if num == 0:
    print("El numero %i es 0" %num)
elif num > 0:
    print("El numero %i es positivo" %num)
else:
    print("El numero %i es negativo" %num)