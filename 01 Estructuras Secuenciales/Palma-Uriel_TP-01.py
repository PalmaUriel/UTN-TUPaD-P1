# Actividades TP 1 Secuenciales. Uriel Palma Comision 8
# 1
print("Hola Mundo")
# 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
# 3
name = input("Ingrese su nombre: ")
lastName = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
country = input("Ingrese su pais de residencia: ")
print(f"Soy {name} {lastName}, tengo {age} años y vivo en {country}.")
# 4
radio = float(input("Ingrese el radio de un círculo: "))
pi = 3.14
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"El area del circulo es: {area} y el perimetro es {perimetro}.")
# 5
segundos = int(input("Ingrese un valor en segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivales a {horas} horas")
# 6
numero = int(input("Ingrese el número del cual desea saber la tabla: "))
print(f"Tabla de multiplicar del {numero}: ")
for i in range(1, 11):
    tabla = numero * i
    print(f"{numero} x {i} = {tabla}")
# 7
numero1 = int(input("Ingrese un número entero distinto de 0: "))
numero2 = int(input("Ingrese otro número entero distinto de 0: "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicación = numero1 * numero2
print(f"los resultados de las operación de ambos numeros son.... suma: {suma}. resta: {resta}. división: {division}. multiplicación: {multiplicación}.")
# 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso en KG: "))
masaCorporal = peso / (altura ** 2)
print(f"Su indice de Masa Corporal es: {masaCorporal}")
# 9
temperaturaCelsius = float(input("Ingrese una temperatura en grados Celsius: "))
tempFahrenheit = (9/5) * temperaturaCelsius + 32
print(f"{temperaturaCelsius} grados Celsius corresponden a {tempFahrenheit} grados Fahrenheit.")
# 10
number1 = float(input("Ingrese un número: "))
number2 = float(input("Ingrese otro número: "))
number3 = float(input("Ingrese otro número: "))
promedio = round((number1 + number2 + number3) / 3)
print(f"El primedio entre {number1}, {number2} y {number3} es {promedio}.")