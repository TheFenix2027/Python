#Listas. Las listas son modificables y estan ordenadas.
numeros= [1, 2, 3, 4, 5]
#Tuplas. Las tuplas son inmodificables y estan ordenas.
colores= ("Rojo", "Amarillo", "Azul")
#Sets. Los sets son inmodificables y estan desordenados.
nombres= {"David", "Juan", "Python"}
print(numeros[2])
print(colores[1])
print(nombres)

numeros[4]= 6
print(numeros)
numeros[0:3]= 7, 8, 9
print(numeros)
numeros.insert(1, 8)
print(numeros)
#Diccionarios. Los diccionarios son modificables y estan desordenados
nombres.add("Felipe")
print(nombres)
nombres.remove("Python")
print(nombres)