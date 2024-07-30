#El ciclo while se utiliza para repetir un bloque de codigo basado en una expresion de texto

x = 1
while x < 10:
    x = x + 1
    if x==3:
        continue
    elif x==6:
        break
    print(x)

#El ciclo for se utiliza para iterar una secuencia de elementos
frutas = ["Manzana", "Pera", "Cereza"]
for item in frutas:
    print(frutas)

fruta = "Manzana"
for x in fruta:
    if x == "n":
        continue
    print(x)

#Rango con for
for x in range(7):
    print(x)

for x in range(3, 10):
    print(x)

for x in range(1, 17, 2):
    print(x)