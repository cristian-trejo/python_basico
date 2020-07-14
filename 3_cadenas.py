nombre = print('Escribe tu nombre: ')
# Estos metodos son especiales para objetos de tipo string
nombre_correcto = nombre.capitalize()
nombre_mayusculas = nombre.uppper()
nombre_minusculas = nombre.lower()
nombre_sin_espacios = nombre.strip()
nombre_remplazando = nombre.replace('a', 'o')
# Indices
letra = nombre[2]
longitud_nombre = len(nombre)
# Slices
nombre_slice_inicial = nombre[:3]
nombre_slice_final = nombre[3:]
nombre_slice_medio = nombre[2:5]
nombre_slice_saltos = nombre[1:7:2]
nombre_inverso = nombre[::-1]