import funciones
'''1.	Escribir una función que reciba un número positivo n y devuelva 
la cantidad de dígitos que tiene.'''
number = int(input("Ingrese un numero positivo para saber cuantos digitos tiene: "))
digitss = 0
digits = funciones.count_digits(number,digitss)
print(f"El numero tiene {digits} digitos")

'''2.	Escribir una función que reciba 2 enteros n y b y devuelva True 
si n es potencia de b.'''
n = int(input("Ingrese un entero n: "))
b = int(input("Ingrese un entero b"))
if (funciones.pow(n,b)):
    print(f"{n} es potencia de {b}")
else:
    print(f"{n} no es potencia de {b}")

'''3.	Escribir una funcion recursiva que reciba como parámetros dos 
strings a y b, y devuelva una lista con las posiciones en donde se 
encuentra b dentro de a.'''
a = input("Ingrese un string a: ")
b = input("Ingrese un string b: ")
empty_positions = []
positions = funciones.function_positions(a,b,empty_positions)
print("Las posiciones donde se b de dentro de a son:")
for i in range(len(positions)):
    if (i == len(positions) - 1):
        print(positions[i])
    else:
        print(f"{positions[i]},", end = " ")

'''4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) 
que determinen la paridad del numero natural dado, conociendo solo 
que:
•	1 es impar.
•	Si un número es impar, su antecesor es par; y viceversa.
'''
number = int(input("Ingrese un numero para saber si es par o impar: "))
odd_even = funciones.function_even(number)
if (odd_even):
    print(f"El numero {number} es par")
else:
    print(f"El numero {number} es impar")

'''5.	Escribir una función recursiva que encuentre el mayor elemento de 
una lista.'''
greater_list = [1,2,5,9,3,6]
i = 0
greater_num = 0
greater_number = funciones.greater_function(greater_list,i,greater_num)
print(f"El mayor elemento de la lista es {greater_number}")

'''6.	Escribir una función recursiva para replicar los elementos de una 
lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) 
= ([1, 1, 3, 3, 3, 3, 7, 7])'''
n = int(input("Ingresa la cantidad de veces que quieras replicar los elementos de la lista: "))
replicate_list = [1, 3, 3, 7]
list_new = []
i = 0
new_list = funciones.function_replicate_list(replicate_list,n,list_new,i)
print("La lista replicada queda:")
print(new_list)

'''7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
● El programa debe pedir al usuario que ingrese un número n, y un número d,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)'''
n = int(input("Ingrese un numero n: "))
p = int(input("Ingrese un numero p: "))
result_k = funciones.K(n,p)
print(f"El valor de K(n,p) = {result_k}")



#8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

line = int(input("Ingrese el numero de fila: "))  
column = int(input("Ingrese el numero de columna: "))

result = funciones.pascal(line, column)
print(f"El valor en la fila {line} y columna {column} del Triángulo de Pascal es: {result}")

#9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).

caracters = ['a', 'b', 'c', 'd', 'e']
k = int(input("Ingrese k: "))
result = []
funciones.combinations(caracters, k, "", result)

for cadena in result:
    print(cadena)

#10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.

#Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.

sheet_number = int(input("Ingrese un numnero para calcular el ancho de la hoja A(n): "))  

width, length = funciones.sheet_measure(sheet_number)

print(f"Las medidas de la hoja A({sheet_number}) son: Ancho = {width} mm, Largo = {length} mm")