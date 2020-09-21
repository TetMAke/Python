"""
Realice un algoritmo que solicite al usuario informar una
cantidad de días, horas, minutos y segundos. Seguidamente,
convierta todo a segundos.
"""

h = input("Horas:")
m = input("Minutos:")
s = input("Segundos:")

h1 = int(h) * 3600
h2 = int(m) * 60
seg = h1 + h2 + int(s)

print("Segundos son:", seg)