import random


def run():
    vidas = 5
    numero_aleatorio = random.randint(1, 100)    
    numero_elegido = int(input(f'Elige un numero del 1 al 100, tienes {vidas} intentos: '))
    

    while numero_elegido != numero_aleatorio:
               
        if numero_elegido < numero_aleatorio:
            vidas -= 1            
            print('Busca un número más grande: ')
        elif numero_elegido > numero_aleatorio:
            vidas -= 1            
            print('Busca un número más pequeño: ')                
        
        if vidas == 0:
            print('Game Over')
            break
        print(f'Te quedan {vidas} intentos.')
        numero_elegido = int(input('Elige otro número: '))

    if numero_aleatorio == numero_elegido:    
        print('¡Ganaste!')
    

if __name__ == "__main__":
    run()