import random

def search_lineal(objective,my_list):
    
    match = False
    
    if len(my_list) <= 0:
        return False        
    for i in range(len(my_list)):
        if my_list[i] == objective:
            match = True
            break
    return match



if __name__ == '__main__':
    
    objective  = int(input('Cual es el tamaño de la lista? '))
    
    my_list = [random.randint(1,100) for i in range(objective) ]
    
    my_number_is  = int(input('Que numero deseas buscar? '))
    
    searched = search_lineal(my_number_is,my_list)
    
    print(f'El numero {my_number_is} { " esta" if searched else "no esta" } en la lista')
    print(my_list)
    



