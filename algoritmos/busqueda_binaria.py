import random


def busqueda_binaria(lista, inicio, final, objetivo):

    if inicio > final:
        return False

    medio = (inicio + final) // 2
    print(medio)
    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        busqueda_binaria(lista, inicio, medio - 1, objetivo)


if __name__ == '__main__':

    tamanio_lista = int(input('De que tamano deseas la lista? = '))
    objetivo = int(input('Qué número buscas? = '))

    lista = sorted([random.randint(0, 10000)
                   for i in range(tamanio_lista)])

    encontrado = busqueda_binaria(lista, 0, tamanio_lista, objetivo)

    print(
        f'El elemento {objetivo} {"está" if encontrado else "no esta"} en la lista')

    print(lista)
