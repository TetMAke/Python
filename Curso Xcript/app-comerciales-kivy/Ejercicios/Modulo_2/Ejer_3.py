"""Realice un algoritmo que lea a dos números e imprima al mayor de ellos."""

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if num1 < num2:
    print("El numero mayor es %i" %num2)
else:
    print("El numero mayor es %i" %num1)