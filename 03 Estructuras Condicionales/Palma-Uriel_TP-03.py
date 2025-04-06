# Actividades TP 3 Estructuras Condicionales
# Uriel Palma Comisión 8
############## 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No cumple con la mayoria de edad")
############## 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
############## 3
num = int(input("Ingrese un número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")
############## 4
age = int(input("Ingrese su edad: "))
if age < 12:
    print("Usted es un niño")
elif age >= 12 and age < 18:
    print("Usted es un adolescente")
elif age >= 18 and age < 30:
    print("Usted es un adulto/a joven")
else:
    print("Usted es un adulto/a")
############## 5
password = input("Ingrese una contraseña con contenga entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresardo una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
############## 6
import random
numeros_aleatorios = [random.randint(1,100) for i in range (50)]

from statistics import multimode, median, mean
modas = multimode(numeros_aleatorios)
moda = modas[0]
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No corresponde")

############## 7
frase = input("Ingrese una frase o palabra: ")
if frase [-1] in ("AEIOUaeiou"):
    print(f"{frase}!")
else:
    print(frase)

############## 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Eliga la opción deseada: " \
"1. Si desea su nombre en mayúsculas " \
"2. Si desea su nombre en minúsculas " \
"3. Si desea su nombre con la primera letra mayúscula. "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Debe elegir una de las 3 opciones")

############## 9
magnitud = int(input("Ingrese la magnitud de un terremoto para conocer su categoria segun la escala de Richter: "))
if magnitud < 3:
    print("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado(Sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte(Puede carsar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte(Puede causar daños significativos)")
else:
    print("Extremo(Puede causar graves daños a gran escala)")

############## 10
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
hemisferio = hemisferio.lower()
dia = int(input("Ingrese el número del día: "))
mes = int(input("Ingrese el número del mes: " \
"1. Enero " \
"2. Febrero " \
"3. Marzo " \
"4. Abril " \
"5. Mayo " \
"6. Junio " \
"7. Julio " \
"8. Agosto " \
"9. Septiembre " \
"10. Octubre " \
"11. Noviembre " \
"12. Diciembre. " \
""))


if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    if hemisferio == "s":
            print("Verano")
    elif hemisferio == "n":
            print("Invierno")
elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    if hemisferio == "s":
            print("Otoño")
    elif hemisferio == "n":
            print("Primavera")
elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    if hemisferio == "s":
            print("Invierno")
    elif hemisferio == "n":
            print("Verano")
elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    if hemisferio == "s":
            print("Primavera")
    elif hemisferio == "n":
            print("Otoño")
else:
        print("Ingrese un valor valido")
        


