def run():
    # Se acceden a los elementos atraves de llaves
    mi_diccionario = {
        'llave_1': 1,
        'llave_2': 2,
        'llave_3': 3,
    }
    print(mi_diccionario['llave_1'])
    
    problacion_paises = {
        # Para visualizar mejor las cantidades se pueden coloar underscores
        'Brasil': 210_147_125,
        'Argentina': 44_938_712,
        'Mexico': 126_000_000,
    }
    for pais in problacion_paises.keys():
        print(pais)

    for pais in problacion_paises.values():
        print(pais)

    for pais, poblacion in problacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes.')


    print(f'Eliminar un elemento: {problacion_paises.pop("Mexico")}')
    print(f'Eliminar todo el diccionario: {problacion_paises.clear()}')


if __name__ == "__main__":
    run()