def run():    
    for contador in range(22):
        if contador % 2 == 0:
            continue
        print(contador)
        if contador == 21:        
            print(f'En la serie aparecio el numero: {contador}')
            break
        

if __name__ == "__main__":
    #rango = print('Ingresa el numero limite para generar un rango: ')
    #rango = int(rango)
    run()