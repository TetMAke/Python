num_int = 5
num_dec = 7.3
val_str = "Cualquier texto"

print("El valor es:", num_int)
print("El valor es: %i" %num_int)
print("El valor es: " + str(num_int)) #cast o conversion de tipo de una variable.

"""
%f-> Marcador de punto flotante.

Se puede controlar la precision del punto flotante usando
%.#f donde el # representa la cantidad de numeros despues
del punto decimal.

"""
print("Concatenando decimal:", num_dec)
print("Concatenando decimal: %.10f" %num_dec)
print("Concatenando decimal: " + str(num_dec))

print("Cocatenando strings", val_str)
print("Cocatenando strings %s" %val_str)
print("Cocatenando strings " + val_str)