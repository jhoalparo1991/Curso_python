import random
import time


def bubble_sort(my_list):

    size = len(my_list)

    for i in range(size):
        for j in range(0, size - i - 1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


if __name__ == '__main__':

    size_list = int(input('Tamaño de la lista '))

    my_list = [random.randint(0, 10000) for i in range(size_list)]

    print(my_list)

    inicio = time.time()
    my_list_sort = bubble_sort(my_list)
    final = time.time()
    print(my_list_sort)
    print(f'Ordenado en { (final - inicio) } segundos')
