#guia 01 de programacion3

def piramide():
    # usuario ingresa total de bloques y se crea piramide con esos bloques
    blocks = int(input("ingrese numero de bloques: "))
    # height es la altura de la piramide
    height = 0
    # suma es una variable que se ocupa para comparar
    suma = 0

    # ocupamos el while para sacar la altura que tendra nuestra piramide
    while suma <= blocks:
        height += 1
        suma += height

    i = 1
    altura = int(height)
    usados = 0
    j = 0
    #se imprime la piramide
    while i < int(altura):
        print(" " * (altura - i), "* " * i)
        usados = usados + (1 * i)
        i += 1
#se determina cuantos bloques han sobrado
    sobrantes = blocks - usados
    print('Bloques sobrantes', sobrantes)

#piramide()
def primo():
    #se le pide un numero entero al usuario
    numero = int(input("Ingrese numero entero: "))
    x = 1
    contador = 0
    # el numero 1 por definicion no es primo
    if (numero == 1):
        print('El numero',numero,'no es primo')
    else:
#se determina cuantas veces se obtiene residuo cero al dividir entre todos los numeros menores al numero
        while x <= numero:
            if numero % x == 0:
                contador += 1
            x += 1
    #si se obtienen solo 2 veces residuo cero el numero es primo
        if contador == 2:
            print('El numero',numero,'es primo')
        else:
            print('El numero',numero,'no es primo')
#primo()