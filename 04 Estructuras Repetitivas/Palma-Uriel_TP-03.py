# Actividades TP 4 Estructuras Repetitivas
# Uriel Palma Comisión 8
############## 1

#for i in range(1,101):
#    print(i)

############## 2

#num = str(input("Ingrese un número entero: "))
#print(len(num))

############## 3

#suma = 0
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingresa el segundo número: "))

#for i in range(num1 +1, num2):
#    suma += i
#print(f"el resultado de la suma de los números enteros entre {num1} y {num2} excluyendo ambos es: {suma}")

############## 4

#suma = 0
#num = 1
#while num != 0:
#    num = int(input("Ingrese un número entero (Ingrese 0 para terminar): "))
#    suma += num
#print(f"La suma total de sus números es {suma}")

############## 5

#import random

#numeroAleatorio = random.randint(0,9)
#num = -1
#intento = 0

#print("Adivina el número entre 0 y 9!")

#while num != numeroAleatorio:
#    num = int(input("Ingresa un número entre 0 y 9: "))
#    intento = intento + 1
#print(f"el número de intentos fue: {intento}")

############## 6

#for i in range(100, 0, -2):
#    print(i)
    

############## 7

#suma = 0
#num = int(input("Ingrese un número entero positivo: "))

#for i in range(0, num +1):
#    suma += i
#print(f"La suma de los números enteros positivos comprendidos entre 0 y {num} es {suma}")

############## 8

#pares = 0
#impares = 0
#positivos = 0
#negativos = 0

#for i in range(0,100):
#    num = int(input("Ingresa un número entero: "))
#    if num > 0:
#        positivos = positivos + 1
#    elif num < 0:
#        negativos = negativos + 1
#    if num % 2 == 0:
#        pares =  pares + 1
#    else:
#        impares = impares + 1
#print(f"Positivos: {positivos}. Negativos: {negativos}. Pares: {pares}. Impares: {impares}")

############## 9

#cantidad_numeros = 100
#acumulador = 0

#for i in range(cantidad_numeros):
#    numero = int(input("Ingrese un número entero: "))
#    acumulador += numero
#    media = acumulador / cantidad_numeros
#print(f"La media de los números es {media}")

############## 10

numero = int(input("Ingrese un número entero positivo: "))

numeroStr = str(numero)
numeroInvertidoStr = numeroStr[::-1]
numeroInvertido = int(numeroInvertidoStr)
print(numeroInvertido)