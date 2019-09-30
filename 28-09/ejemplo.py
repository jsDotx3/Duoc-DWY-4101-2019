nombre = "pEdRo"
numero_1 = 10
numero_2 = 10.3
valor_verdadero = True
valor_Falso = False
valor_array = ["Hola", 1, 1.3, "Ejemplo"]
valor_tuplas = ("Prueba", 1, 1.4, False, "Hola")

lower = nombre.lower()
upper = nombre.upper()
title = nombre.title()

number_one = 20
number_two = 30

suma = number_one + number_two
resta = number_one - number_two
multiplicacion = number_one * number_two
division = number_one / number_two # 0.5
division_entera = number_one // number_two # 0
resto_divison = number_one % number_two
potencia = number_one ** number_two # 20 elevado a 30
redondeo = round(division,1)  # Segundo argumento es la cantidad de decimales para redondear

print(suma,resta,multiplicacion,division,division_entera,resto_divison,potencia,redondeo)

print(lower,upper,title, nombre)

array_numeros = [1,300,45,3,4556,0]
array_numeros.sort() # Orden ascendente
array_numeros.sort(reverse=True) # Orden descendente
print(array_numeros)



valor_array.append('Texto de Prueba') # Insertar un valor al final de larray
valor_array.insert(5, 'Valor del array indice 5') # Insertar un valor en el indice 5

print("El valor del indice -1 original es: ", valor_array[-1])

valor_array.remove("Ejemplo") # Eliminando del array por valor
print("El valor del indice -1 después de eliminar Ejemplo es: ", valor_array[-1])

del valor_array[2] # Eliminando del array por indice.
print("El valor del indice -1 después de eliminar el array con indice 2 es: ", valor_array[-1])

print("El valor de la variable nombre es: "+ nombre)

# Esto es un comentario