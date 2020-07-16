import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f']
    simbolos = ['!', '#', '$', '%', '&', '/', '(', ')', '=']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        # choise es un metodo de ramdom para seleccionar un caracter aleatorio de la lista
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    # Generamos un string de la lista
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contraseña es: {contrasena}')


if __name__ == "__main__":
    run()    