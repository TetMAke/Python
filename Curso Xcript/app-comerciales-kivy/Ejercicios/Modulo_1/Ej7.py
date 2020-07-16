"""
Realice un algoritmo que solicite al usuario informar 2
números. Seguidamente, sume los valores y envíe a la salida
estándar la siguiente frase: "La suma entre <X> e <Y>
es igual a <total>"
"""

num = input("Dígite un numero: ")
num1 = input("Dígite otro número: ")
sum = int(num) + int(num1)
print("La suma entre %s e %s es igual a %i" % (num, num1, sum))
