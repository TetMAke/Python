
"""
Realice un algoritmo que solicite las notas de las 4 pruebas
semestrales al usuario. Seguidamente, calcule la media y
envíe el valor resultante a la salida estándar:
"""

num1 = input("Nota 1:")
num2 = input("Nota 2:")
num3 = input("Nota 3:")
num4 = input("Nota 4:")

average = (int(num1)+int(num2)+int(num3)+int(num4))/4

print(average)