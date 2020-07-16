"""Realice un algoritmo que solicite al usuario informar 3
números. Seguidamente, sume los valores y envíe a la salida
estándar la siguiente frase "La suma total es:  "."""

num1 = input("Digite un numero: ")
num2 = input("Digite un 2do numero: ")
num3 = input("Digite un 3er numero: ")
sum = int(num1) + int(num2) + int(num3)
print("La suma total es: %i" % sum)
