def suma (numero_1, numero_2):
    return numero_1 + numero_2

def resta (numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion (numero_1, numero_2):
    return numero_1 * numero_2
    
def division (numero_1, numero_2):
    return numero_1 / numero_2

def calculadora(numero_1, numero_2, operacion): 
    if operacion == 'suma':
       return suma(numero_1,numero_2)

    if operacion == 'resta':
       return resta(numero_1,numero_2)

    if operacion == 'multiplicacion':
       return multiplicacion(numero_1,numero_2)

    if operacion == 'division':
       return division(numero_1,numero_2)

numero_1 = 10
numero_2 = 20

operacion_suma = calculadora(numero_1,numero_2,'suma')
operacion_resta = calculadora(numero_1,numero_2,'resta')
operacion_multiplicacion = calculadora(numero_1,numero_2,'multiplicacion')
operacion_division = calculadora(numero_1,numero_2,'division')

print("La suma de ",numero_1,"con",numero_2,"es",operacion_suma)
print("La resta de ",numero_1,"con",numero_2,"es",operacion_resta)
print("La multiplicacion de ",numero_1,"con",numero_2,"es",operacion_multiplicacion)
print("La division de ",numero_1,"con",numero_2,"es",operacion_division)