edad = int(input('Escribre tu edad: '))

if edad > 17:
    print('Eres mayor de edad.')
else:
    print('Eres menor de edad.')

#--------------------------------------------#
numero = int(input('Escribre un número: '))

if numero > 5:
    print('Es mayor a 5.')
elif numero == 5:
    print('Es igual a 5.')
else:
    print('Es menor a 5.')

#--------------------------------------------#
def suma(a, b):
    print('Se suman dos numeros')
    resultado = a + b
    # Nos indica que al finalizar la funcion se va a devolver la variable resultado
    return resultado

# Guardamos el valor que devuelve la funcion y lo guardamos en la variable sumatoria
sumatoria = suma(1, 4)
print(sumatoria)