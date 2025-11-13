import os 
os.system('cls')

lista = [1,2,3,4]

lista.append(1) #Agregar elementos al final

lista.append('a')

lista.insert(0,1.1) #inserta un elemento en una posicion especifica

lista.extend([1,1,1,1,'a'])# agregar varios elementos al final de la lista

# Eliminar elementos de una lista

lista.remove('a') #Eliminar la primera coincidencia por valor no por indice

lista.pop() #Sin parametros o con -1 siempre elimina el ultimo valor, pero se puede pasar cualquier indice 
lista.pop(0) 
# lista.clear() #limpiar todo
print(lista)
# ordenar listas
lista.sort() #Solo funciona con enteros y modifica la lista original
print(lista)

listaLetras = ['Y','A','z','a','b','c','d','a']
print(listaLetras)
listaLetras.sort()
print(listaLetras)

nuevaLista = sorted(listaLetras)
nuevaLista.sort(key=str.lower,reverse=True)

print(nuevaLista)
print(len(nuevaLista))
print(nuevaLista.count('q'))
print('q' in nuevaLista)