
def saludar(name:str ='juan'):
    print(f"¡Hola, {name}!");
# lambda
sumar=lambda x, y: x + y
# print(saludar())    

# si queremos que una funcion acepte # un numero variable de argumentos
def sumar_varios(*args):
    return sum(args)  
# print(sumar_varios(1, 2, 3, 4, 5))  # Imprime: 15

def mostrar_info(**persona):
  return persona['ciudad']
  
    # for clave, valor in persona.items():
    #     print(f"{clave}: {valor}")

# result = mostrar_info(nombre="Ana", edad=30, ciudad="Barcelona", profesion="Ingeniera", pais="España", telefono="123456789")
# print(result)  # Imprime: Barcelona
# saludar = 'Hola, juan!'
def test():
  saludar = 'Hola, pablo!'

def test():
  saludar = 'Hola, daniel!'
  
print(saludar)  # Imprime: Hola, mundo!  

  



