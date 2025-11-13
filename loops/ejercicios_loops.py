import os 
os.system('cls')
###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
for i in range(2,21,2):
  print(i)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma=0
for i in numeros:  
  suma += i
media = suma / len(numeros)
print(media)
  
  

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [1,12,40,2,3,4,5,89,15, 5, 25, 10, 20]
numero_mayor= numeros[0]
for i in numeros:
  if i > numero_mayor:
    numero_mayor=i
print(numero_mayor)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabra_largas=[palabra for palabra in palabras if len(palabra) > 5]
print(palabra_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = 'a'
coincidencias= 0
for palabra in palabras:
  # if palabra[0] == letra:
  if palabra.lower().startswith(letra.lower()):
    coincidencias += 1
print(coincidencias)