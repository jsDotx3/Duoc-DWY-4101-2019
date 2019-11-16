numeros_array = range(1,11)

for valor in numeros_array:
    pass
    # print(valor)

for indice, value in enumerate(numeros_array):
    print("En el indice ",indice,"tiene el valor", value)



diccionario = {'a': 10, 'b': 20,'c':300}

for key, value in diccionario.items():
    print(key,value)