accion = int(input("Digite '1' para si y '2 para no: "))

if (accion == 1):
    print("Usted dijo que SI")
else:
    if (accion == 2):
        print("Usted dijo que NO")
    else:
        print("Digite un valor valido.")

"""Operadores relacionales"""
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))

if (num1 == num2):  # Operador de igualdad
    print("El numero %d es igual a %d" % (num1, num2))

if (num1 != num2):
    print("El numero %d es diferente a %d" % (num1, num2))

if (num1 < num2):
    print("El numero %d es menor a %d" % (num1, num2))

if (num1 > num2):
    print("El numero %d es mayor a %d" % (num1, num2))

if (num1 <= num2):
    print("El numero %d es menor igual que %d" % (num1, num2))

if (num1 >= num2):
    print("El numero %d es mayor igual que %d" % (num1, num2))

"""Operadores Logicos

Simplificar las condiciones, estos son:
and (y)
or (o)
not() (negación)
is (es)
is not (no es)
in  (contenido)
not in  (no contenido)
"""

"""Bloque de instruccion

Conjunto de lineas de codigo identadas en el mismo nivel.
Es un conjunto de instrucciones que se encuentran
en el mismo nível de identación, es decir en el mismo nivel jerárquico.
"""

num1 = int(input("Digite un numero: "))
if (num1 > 10):
    print("el valor es mayor que 10!")
    if(num1<=15):
        print("El valor es mayor que 10, pero menor que 15")
    else:
        if(num1<=50):
            print("El valor es mayor que 10, pero menor que 50!")
else:
    if (num1 > 5):
        print("numero es menor que 10 pero mayor que 5!")
        if (num1 == 7):
            print("Numero es igual a 7.")
        else:
            print("El valor es menor a 5.")
