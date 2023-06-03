import random

def option_player():
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    option = int(input('Cual eliges? => '))
    while option <= 0 or option > 3:
        option = int(input('Cual eliges? => '))
    return option

def exec_game():
    
    
    point_player = 0
    point_machine = 0
    counter = 0
    while(True):
            
        player = option_player()
        machine = random.randint(0,2) 
        options = ['Piedra','Papel','Tijera']
        
        print(f'Player => {options[player-1]}')
        print(f'Machine => {options[machine]}')
        
        win = winner(options[player-1],options[machine])
        
        if win == 'player' :
            point_player += 1
        elif win == 'machine':
            point_machine += 1
        print('-' * 50)
        counter += 1
        if point_player == 3 or point_machine == 3:
            break
        
        
    print(f'Player {point_player}')    
    print(f'Machine {point_machine}')    
    print(f'Rounds {counter}')
    
    if point_player > point_machine :
        print('!FELICITACIONES, has ganado la partida¡')
    else:
        print('!UPS, has perdio la partida,TE GANÓ UNA MAQUINA ¡')
                
def winner(player, machine) :

    message = ''
    if player == machine :
        return -1  
    elif player == 'Piedra' and machine == 'Tijera' or  player == 'Tijera' and machine == 'Papel' or player == 'Papel' and machine =='Piedra':
        message = 'player'
    else:
        message = 'machine'
    
    return message  
            
if __name__ == '__main__':

    exec_game()
    
        
    
    