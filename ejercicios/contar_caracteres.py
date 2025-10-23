# Dado un string de n caracteres. Desarrolla una función que retorne su longitud de caracteres.

# La función debe cumplir con los siguientes requerimientos.

# La función tendrá por nombre longitud.
# La función recibirá como argumento el string del cual se desea conocer su longitud.
# La función retornará la cantidad de caracteres que posee el string.
# Ejemplo.





def longitud(texto:str)-> int:  
  return len(texto)
print(longitud("Hola mundo"))

def longitud(texto: str) -> int:
  i=0
  for _ in texto:
    i+= 1
    print(i)
  return i  

print(longitud("Hola mundo"))