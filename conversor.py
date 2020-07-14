def conversionMonedas(opcion, cantidad):
    if opcion == 1:
        conversion = round(cantidad / 22.73, 2)
        print(f'{cantidad} MXN equivalen a {conversion} USD.')
    elif opcion == 2:
        conversion = round(cantidad * 22.73, 2)        
        print(f'{cantidad} USD equivalen a {conversion} MXN.')
    else:
        print(f'Opción o cantidad no valida.')

opcionUsuario = int(input('Elije una opción: \n1- Convertir de MXN a USD. \n2- Convertir de USD a MXN.\n'))
cantidadUsuario = float(input('Ingresa la cantidad a convertir: '))
conversionMonedas(opcionUsuario, cantidadUsuario)