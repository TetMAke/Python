"""Realice un algoritmo que pida dos números. Primero, imprima al mayor de ellos y, seguidamente imprima al
menor de ellos."""

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 > num2:
    nuM = num1
    numm = num2
else:
    numm = num1
    nuM = num2

print("El numero mayor es %i" %nuM)
print("El numero menor es %i" %numm)
