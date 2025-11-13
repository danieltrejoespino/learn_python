import os 
os.system('cls')
#* while
# contador = 0 
# while contador <= 5:
#   print(contador)
#   contador += 1
  
# while contador <= 5:
#   print(contador)
#   contador += 1
#   break


# def contar(id = 0):
#   contador=0
#   while contador <id:
#     print(contador)
#     contador += 1    
# contar(12)
#* for
lista = list(range(1,50))
# for i in lista:
#   if(i / 2 == 0):
#     print(i)
  
# for e in "hola mundo":
#   print(e)
  
# for index, i in enumerate("hola mundo"):
#   print(f'Indice {index} letra: {i}')
# for i  in range(100,1,-1):
#   print(i)


#! Esto es comprension de listas

# animales = ['perro', 'gato', 'tigre', 'leon']

# animales_mayusculas = [animal.upper() for animal in animales]
# print(animales_mayusculas)
  
pares = [par for par in range(100) if par % 2 == 0 ]

print(pares)