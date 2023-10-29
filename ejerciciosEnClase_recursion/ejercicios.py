import random
#Escribir una función que simule el siguiente experimento: Se tiene una 
# rata en una jaula con 3 caminos, entre los cuales elige al azar (cada 
# uno tiene la misma probabilidad), si elige el 1 luego de 3 minutos 
# vuelve a la jaula, si elige el 2 luego de 5 minutos vuelve a la jaula, 
# en el caso de elegir el 3 luego de 7 minutos sale de la jaula. La rata 
# no aprende, siempre elige entre los 3 caminos con la misma probabilidad, 
# pero quiere su libertad, por lo que recorrerá los caminos hasta salir de 
# la jaula. La función debe devolver el tiempo que tarda la rata en salir 
# de la jaula.

def path_choice(o,c):
    o = random.randint(1,3)
    if o==1:
        c = c + 3
        return (path_choice(o,c))
    elif o==2:
        c = c +5
        return (path_choice(o,c))
    else:
        c=c + 7
        return c

cronometer = 0
option = 0
print("La rata en la jaula")
print(f"La rata se demoro {path_choice(option,cronometer)} minutos en salir de la jaula")


# Escribir una consigna apropiada para la siguiente funcion
# Escriba una funcion que retorne el numero ingresado dado vuelta

def f (n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

n = int(input("Ingrese un numero entero: "))

print (f"{f(n)}")