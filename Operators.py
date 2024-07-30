#los operadores de comparasion se utilizan para comparar valores.
x = 2
y = 4

#print(x == y)
#print(x != y)
#print(x <= y)
#print(x >= y)

#los operadores logicos
#print(x < 3 and x <5)
#print( y > 1 or y < 3)
#print(not(x < 3 and x < 9))

#operadores d identidad
lista1 = ["manzana", "cereza"]
lista2 = ["manzana", "cereza"]
lista3 = lista2
#print(lista1 is lista2)
#print( lista2 is lista3)

#membership operator
#print("cereza" in lista1)
#print("mango" in lista1)
#print("mango" not in lista1)

#condicional if
numero1 = input("Introduce un número")
numero2 = input("Introduce otro número")

if numero1 < numero2:
    print("y es menor que x ")
elif numero1 > numero2:
    print("y es mayor que x")
print("Completado")