import random
import time


def lista_ordenada(lista):

    tamanio = len(lista)

    for indice in range(1, tamanio):

        posicion_lista = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > posicion_lista:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = posicion_lista

    return lista


if __name__ == '__main__':

    print(' Ordenamiento por insercion '.center(100, '*'))
    size_list = int(input('Tamaño de la lista '))

    my_list = [random.randint(0, 10000) for i in range(size_list)]

    print(my_list)

    inicio = time.time()
    my_list_sort = lista_ordenada(my_list)
    final = time.time()
    print(my_list_sort)
    print(f'Ordenado en { (final - inicio) } segundos')
