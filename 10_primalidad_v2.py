import math
import time

def es_primo(numero):
    if numero <= 1:
        return False

    maximo_divisor = math.floor(math.sqrt(numero))
    for contador in range(2, 1 + maximo_divisor):
        if contador % contador == 0:
            return False
    return True


def run():    
    # Inicio de computo
    tiempo_inicial = time.time()
    contador_primos = 0


    numero = int(input('Ingresa un numero: '))
    if es_primo(numero):
        print('Es primo.')
    else:
        print('No es primo.')


    for n in range(1, 100000):
        cantidad_primos = es_primo(n)
        contador_primos += cantidad_primos
    print(f'Total de numeros primero en el rango: {contador_primos}')


    tiempo_final = time.time()
    print(f'Tiempo requerido: {round(tiempo_final - tiempo_inicial, 2)} s.')


if __name__ == "__main__":
    run()    