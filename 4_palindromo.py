def palindromo(palabra):
    # Eliminamos los espacios en blanco
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


# equivale a main
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print('Es palíndromo.')
    else:
        print('No es palíndromo.')


# Es el punto de entrada de un programa de Python
if __name__ == '__main__':
    run()