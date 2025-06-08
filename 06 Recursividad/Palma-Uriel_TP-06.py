# Actividades TP 6 Recursividad
# Uriel Palma Comisión 8

#### 1

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

numero = int(input("Ingrese un número: "))
for i in range(1, numero + 1):    
    print(f"El factorial de {i} es {factorial(i)}")

### 2

def serie_fibbo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return serie_fibbo(num -1) + serie_fibbo(num - 2)

numfibbo = int(input("Ingrese un número: "))

for i in range(1, numfibbo + 1):
    print(f"la serie fibbonacci hasta {numfibbo} es {serie_fibbo(i)}")

### 3

def potencia(num,exponente):
    if exponente == 0:
        return 1
    else:
        return num * potencia(num, exponente - 1)
    
numPote = int(input("Ingrese un número para obtener la potencia: "))
exponent = int(input("Ingrese el exponente para la potencia del número: "))
result = potencia(numPote,exponent)
print(f"El resultado de {numPote} elevado al exponente {exponent} es {result}")

### 4

def a_binario(num):
    return "" if num == 0 else a_binario(num // 2) + str((num % 2))
        
num = int(input("Ingrese un número decimal: "))

if num == 0:
    print("0")
elif num < 0:
    print("Ingrese un número positivo")
else:
    resultado = a_binario(num)
    print(resultado)

### 5

def es_palindromo(palabra):
    if len(palabra) < 2:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print(es_palindromo(palabra))

### 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los digitos de {n} es: {suma_digitos(n)}")

### 7

def contar_bloques(n):
    if n == 1:
        return 1 
    else:
            return n + contar_bloques(n - 1)

bloque = int(input("Ingrese un número: "))
print(f"Los bloques necesarios para construir la piramide son: {contar_bloques(bloque)}")

### 8

def contar_digito(numero, digito):
    if digito < 0 or digito > 9:
        return 0
    if numero < 10:
        return int(numero == digito)
    else:
        return int(numero % 10 == digito) + contar_digito(numero // 10, digito)

number = int(input("Ingrese un número: "))
digit =  int(input("Ingrese un digito entre 0 y 9: "))
resultadoFinal = contar_digito(number, digit)
print(f"El número {number} contiene {resultadoFinal} veces el digito {digit}")