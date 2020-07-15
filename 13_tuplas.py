def run():
    # las tuplas son inmutables
    # Funcionan más rapido que una lista y es recomentable para loops
    tupla = (1, 2, 3, 4, 5)
    
    for numero in tupla:
        print(numero)


if __name__ == "__main__":
    run()