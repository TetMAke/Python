# condicional if y operadores lógicos (And, Or y Not)

"""
Aspectos por mejorar:

1) Leve descripción teórica o al menos refencias  sobre operadores lógicos
2) Teoría sobre  el condicional if
3) Cambio de variables por nombres menos personales
    -Modificar el nombre de gabriel por una variable - Listo
4) Descripción de los códigos presentes en este archivo
"""
"""
El condicional if (si) es una  forma de hacer control a las instrucciones del progromama. Por medio de de la sentencia if es posible decidir
cuáles instrucciones y cuales no dependiendo de una o varias condiciones. El siguiente programa sirve para elaborar un bot simple con el que
puedes dialogar dependiendo de lo que respondas. En este código no sólo se muestra cómo usar el condicional if sino como  pedir datos y 
guardarlos en variables. 

Operadores lógicos

Un aspecto a tener en cuenta antes de empezar con el código, es un concepto conocido como los operadores lógicos. Ellos no son más que palabras
que usamos en nuestro día a día para conectar ideas y en la programación los podemos usar para hacer condiciones más específicas. Los operado-
res más comunes son los siguientes:

Operador Lógico   Python
Y                 And
O                 Or
No                Not

No siendo más, comencemos.

"""

#Bot Simple

#Este bot fue creado por Carlos, así que puede identificarlo a través de algunas preguntas, pero también puede comunicarse con otros usuarios.
#Este bot es un poco culto, así que le gusta hacer algunas preguntas sobre música y escritura.
 

año = int(input("¿En qué año estamos? ")) #Pedir entrada y tratar el dato como valor entéro
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
    nombre = input("¿Cuál  es tu nombre? ") #Python reconoce caractéres de otros idiomas en su texto como lo son las tíldes 
    año_nacimiento = int(input("¿En qué año naciste? "))
    edad_usuario = año - año_nacimiento
    if not edad == edad_usuario: # operador lógico Not. La condición se cumple si la edad no es igual a la edad calculada 
          print("mmmm...algo extraño pasa. Vamos a confirmar")
          edad = int(input("ingresa tu edad: "))
    if nombre == "Carlos" or nombre == "carlos" and año_nacimiento == 1990 and edad == edad_usuario: # operador lógico Or y operador lógico And
        print("Bienvenido Carlos, programador de este código")
        print("Ahora debes responder una pregunta de autenticación")
        respuesta = input("¿Cuál fue el primer sobrenombre que te pusiste? " )
        if respuesta == "Gohan" or respuesta == "gohan": 
            print("¡perfecto¡ Definitvamente eres Carlos")
        else:
            print("Confirmación reprobada.")
    else:
       print("Bienvenido usuario")     
else: # la declaración if y su declaración else deben tener la mísma sangría(indentation) para que la sintaxis sea correcta
        print("eres menor de edad.\nTe faltan "+ str(18-edad) + " años para llegar a los 18.")
        gusto = input("¿te gusta la música instrumental? ")
        if gusto == "Sí":
         print("¡que buen gusto tienes!")
         #la delcaración elif es la forma que se usa en Python para escribir "Else If"
         # no es necesario usarlo, ya que bien puedes colocar en una línea la delcaración Else y en la siguente el condicional If
        elif gusto == "sí": 
            print("¡que buen gusto tienes!")
        elif gusto == "si":
            print("¡que buen gusto tienes, pero no olvides la tilde diacrítica!")
        elif gusto == "Si":
             print("¡que buen gusto tienes, pero no olvides la tilde diacrítica!")
        elif gusto == "No":
             print("lástima :(")
        elif gusto == "no":
            print("lástima")

"""Incluir referencias sobre operadores lógicos en español"""
