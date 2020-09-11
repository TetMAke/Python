import random # Módulo para funciones aleatorias

# Definición de función de búsqueda binaria en uan lista.

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
    # Dado que se trata de una función recursiva,
    # Si esta condición se cumple sin que se haya encontrado el número,
    # es por que ya no se puede dividir más la lista y por ende no 
    # se encontró el número. Este es el primer caso base para la función recursiva    
        return False

    # Creación de punto medio que parte la lista en dos.
    # Se asegura que la división de un número entero.
    medio = (comienzo + final) // 2

    # Caso en el que el número a buscar está en la mistad de la lista. Segundo caso base
    if lista[medio] == objetivo:
        return True
    # Caso en el que el número a buscar es mayor que el número que se encuentra en la mitad de la lista 
    elif lista[medio] < objetivo:
        # repetir búsqueda binaria pero desde la mitad superior de la listsa 
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    # Caso en que el número a buscar es menor que el número que está en la mitad de la lista
    else:
        # repetir la búsqueda binaria pero desde la mitad inferior de la lista
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)

#Inicio de ejecución de código de Python
if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)]) # Seguir por aquí  

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')