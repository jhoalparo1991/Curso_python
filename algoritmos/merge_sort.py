import random
import sys

sys.setrecursionlimit(10000000)


def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    
    left = arr[:middle]
    right = arr[middle:] 
    
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)

def merge(left, right):
    
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):

        print(f'Arr -> [{left[i]}, {right[j]}]')
        if left[i] < right[j] :
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
            
    while i < len(left):
        result.append(left[i])
        i +=1
    
    while j < len(right):
        result.append(right[j])
        j +=1    
    return result

if __name__ == '__main__':
    
    size = int(input('Tamaño de la lista = '))
    
    my_list = [random.randint(0,100) for i in range(size)]    
    print(my_list)
    
    list_sort = merge_sort(my_list)
    print(list_sort)