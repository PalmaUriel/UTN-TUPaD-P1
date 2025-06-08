# Actividades TP 5 Funciones
# Uriel Palma Comisión 8

import math

#Definir Funciones

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre = input("Ingrese su nombre para recibir un saludo! ")):
    print(f"Hola {nombre}!")

def informacion_personal():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su pais de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def validar_numero_entero(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"Error. {mensaje}: "))
    return n

def calcular_area_circulo(radio):
    return math.pi * radio ** 2
    

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
    
def segundos_a_horas(segundos):
    return segundos / 3600
    
def tabla_multiplicar(numero):
    resultado = 0
    print(f"Tabla de Multiplicar del número {numero}!!")
    for i in range(1,11):
        resultado = numero * i
        print (resultado)

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b
    tupla = (suma, resta, multi, div)
    print(f"Los resultados de las operaciones realizadas son {tupla}")
    
def calcular_imc(peso, altura): 
    imc = peso / (altura ** 2)
    print(f"Su Indice de Masa Corporas es : {imc:.2f}")

def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius} grados Celsius corresponden a {fahrenheit} grados Fahrenheit")

def calcular_promedio(n1, n2, n3):
    promedio = n1 + n2 + n3 / 3
    print(F"El promedio de los números ingresados es {promedio:.2f}")

##Programa Principal

#### 1

imprimir_hola_mundo()

#### 2

saludar_usuario()

#### 3

informacion_personal()

#### 4

radio = validar_numero_entero("Ingrese un radio en cm", 1)
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es {area} y el perimetro {perimetro}")

#### 5

segundos = validar_numero_entero("Ingrese un número de segundos", 1)
horas = segundos_a_horas(segundos)
print(f"El número de segundos {segundos} corresponde a {horas} horas")

#### 6

numero = validar_numero_entero("Ingrese un número: ", 1)
tabla_multiplicar(numero)

#### 7

a = validar_numero_entero("Ingrese un número", 1)
b = validar_numero_entero("Ingrese otro número", 1)
operaciones_basicas(a, b)

#### 8

peso = validar_numero_entero("Ingrese su peso en kg: ", 1)
altura = validar_numero_entero("Ingrese su altura en cm: ", 1)
calcular_imc(peso, altura / 100)

#### 9

celsius = validar_numero_entero("Ingrese un valor de grados celsius: ", 1)
celsius_a_fahrenheit(celsius)

#### 10

a = validar_numero_entero("Ingrese el primer número: ", 1)
b = validar_numero_entero("Ingrese el segundo número: ", 1)
c = validar_numero_entero("Ingrese el tercer número: ", 1)
calcular_promedio(a, b, c)
