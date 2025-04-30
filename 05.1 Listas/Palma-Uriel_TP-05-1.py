# Actividades TP 5.1 Listas
# Uriel Palma Comisión 8

######## Actividad 1
multiplos_cuatro = list(range(4,101,4))
print(multiplos_cuatro)

######## Actividad 2
elementos = ["Lunes", "Martes", "Miercoles","Jueves","Viernes"]
print(elementos[3])

######## Actividad 3
list_vacia = []
list_vacia.append("Primera")
list_vacia.append("Segunda")
list_vacia.append("Tercera")
print(list_vacia)

######## Actividad 4
animales = ["Perro", "Gato", "Conejo", "Pez"]
animales[-1] = "Oso"
animales[-3] = "Loro"
print(animales)

######## Actividad 5

#El programa crea una lista llamada numeros que contiene 5 numeros
#Luego, se utiliza un remove para borrar un número el cual se obtiene de la funcion max() que llama al número de mayor valor en la lista
#Para finalizar se imprime la lista numeros con la modificación

######## Actividad 6
number = list(range(10,31,5))
print(number[0:2])

######## Actividad 7
autos = ["Sedan", "Polo", "Suran", "Gol"]
autos[-2] = "Passat"
autos[-3] = "Civic"
print(autos)

######## Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

######## Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][-2] = "tallarines"
compras[0].remove("pan")
print(compras)

######## Actividad 10
lista_anidada = [[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)
