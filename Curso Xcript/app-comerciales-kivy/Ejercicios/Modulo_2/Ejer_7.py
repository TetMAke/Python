"""Realice un algoritmo que pida un número al usuario y verifique si el mismo es par o impar."""

num = int(input("Usuario un numero: "))

if num % 2 == 0:
    print("El numero %i es par." % num)
else:
    print("El numero %i es impar." % num)