import sys
from os import system

clients = ['Ana', 'Carlos','Patricia','Marlon']


def get_all_clients():
    print('Our list clients: ')
    print('*' * 50)
    for client in clients:
        print(client)
    print('*' * 50)
    print()    
        
def create_client(name):
    
    if name is clients:
        print(f'This client name {name} already exist in the list')
    else:

        clients.append(name)


def update_client(name_search, new_name):

    if name_search is clients:    

        print(f'Client {name_search} not found in the list')

    else:
        for index, client in clients:
        
            if clients[index] == name_search:
            
                clients[index] = new_name
                

def _name_clients():
    return input('What is the name client? => ')


def _menu():
    print("Welcome to platzi SALE".center(50," "))
    print('-' * 50 )
    print('What do you like to make?')
    print('[C]reate')
    print('[R]ead')
    print('[U]pdate')
    print('[D]elete')
    

if __name__ == '__main__':
    
    system('cls')   
    
    while True:
        
        
        _menu()
    
        command = input('Select option => ').lower()
        
        if command is None:
            sys.exit()
                   
        elif command == 'c':   
        
            name = _name_clients()

            if name is None or name == 'exit':
                sys.exit()
            
            create_client(name)
        
        elif command == 'r':
        
            get_all_clients()
           
        elif command == 'u':
            
            name_search = _name_clients() 
            
            new_name = input('What is the new name of client? => ')
            
            update_client(name_search, new_name)                
