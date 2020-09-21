"""
Realice un algoritmo que solicite al usuario informar el
valor de una compra. Seguidamente, aplique un 10% de
descuento e imprima en la pantalla tanto el valor total
como el valor con el descuento aplicado.
"""

value = input("Compra:")
desc = int(value) * 0.9

print("Valor: %s y Descontado: %i" %(value, desc))