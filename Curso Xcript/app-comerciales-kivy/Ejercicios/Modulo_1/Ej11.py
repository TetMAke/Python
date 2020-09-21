"""
Realice un algoritmo que solicite al usuario que escriba 2
números. Seguidamente, imprima el total de la división en
números  decimales y el total de la división en números
enteros ( es decir, sin casillas decimales).
"""
num = input("Numero 1:")
num1 = input("Numero 2:")

div = int(num)/int(num1)

print("Entero: %i y Decimales: %.1f" %(div, div))