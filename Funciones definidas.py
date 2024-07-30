#definir una función
def operacion(x):
    resultado=x*x
    return resultado
print(operacion(5))

#llamar la funcion
print(operacion(6))
print(operacion(7))
print(operacion(3))

#Varios argumentos y varios valores
def multiplicacion(x, y):
    multi= x*y
    suma= x+y
    resta= x-y
    division= (int(x/y))
    return multi, suma, resta, division
print(multiplicacion(30, 5))