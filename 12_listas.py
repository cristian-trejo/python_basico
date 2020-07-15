def run():    
    a = [1, 2]
    b = [3, 4]
    print(f'Concatenación: {a + b}')
    # Repite la lista
    print(f'Multiplicacion: {a * 2}')
    # Eliminar elemnto dado el indice
    print(f'Eliminar elemento: {a.pop(1)}, lista {a}')
    # Ordernar lista de menor a mayor
    a = [3, 1, 7, 4]
    print(f'Lista ordenada de menor a mayor: {a.sort()}')
    # Ordernar lista de mayor a menor
    print(f'Lista ordenada de mayor a menor: {sorted(a)}')
    # Eliminar elemento dado su valor
    print(f'Eliminar elemento: {a.remove(7)}')
    # Lista con rango
    c = (list(range(0, 10, 2)))
    print(f'Lista con rango: {c}')
    # Tamaño de lista
    print(f'Tamaño de lista: {len(a)}')


if __name__ == "__main__":
    run()
