formato = 'xx/xx/xxxx'

fecha = input("Digite la fecha con el formato correcto: ")

if len(fecha) == len(formato):
    print("Fecha es valida")
else:
    print("Fecha No es valida")