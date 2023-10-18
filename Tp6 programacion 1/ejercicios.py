'''1.	Solicitar al usuario que ingrese números, estos deben guardarse en 
una lista. Para finalizar el usuario debe ingresar 0, el cual no debe 
guardarse.'''

number_list = []
number = 3
print("Ingresaras numeros a una lista:")
while number != 0:
    number = float(input("Ingrese cualquier numero o 0 para finalizar: "))
    if (number != 0):
        number_list.append(number)
    else:
        pass
print(number_list)

''''2.	A continuación, solicitar al usuario que ingrese un número y, si 
el número está en la lista, eliminar su primera ocurrencia. Mostrar un 
mensaje si no es posible eliminar.'''

number = float(input("Ingrese un numero que quiera eliminar su primera ocurrencia: "))
if (number not in number_list):
    print(f"El numero {number} no puede ser eliminado")
else:
    for i in range(len(number_list)):
        if (number_list[i] == number):
            del number_list[i]
            break
        else:
            pass
print(number_list)

'''3.	Imprimir la sumatoria de todos los números de la lista.'''
addition_list = 0
for i in number_list:
    addition_list += i

print(f"La sumatoria de todos los elementos de la lista es {addition_list}")

'''4.	Solicitar al usuario otro número y crear una lista con los 
elementos de la lista original, que sean menores que el número dado. 
Imprimir esta nueva lista, iterando por ella.'''

minor_numbers_list = []
print("Ingresaras un numero para crear una lista con los elementos menores a ese numero de la otra lista:")
number = float(input("Ingrese el numero: "))
for i in number_list:
    if (i < number):
        minor_numbers_list.append(i)
    else:
        pass

print("Elementos de la lista generada:")
for i in minor_numbers_list:
    print(i)

'''5.	Generar e imprimir una nueva lista que contenga como elementos a 
tuplas, cada una compuesta por un número de la lista original y la 
cantidad de veces que aparece en ella. Por ejemplo, si la lista 
original es [5,16,2,5,57,5,2], la nueva lista contendrá: 
[(5,3),(16,1),(2,2),(57,1)]'''

tuple_list = []
appear_numbers = []
for i in number_list:
    if i not in appear_numbers:
        appear_numbers.append(i)
        tuple_list.append((i,number_list.count(i)))
    else:
        pass

print(tuple_list)

'''6.	Solicitar al usuario que ingrese los nombres de pila de los 
alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. 
A continuación, solicitar que ingrese los nombres de los alumnos de 
nivel secundario, finalizando al ingresar ‘x’.
a.	Informar los nombres de todos los alumnos de nivel primario y de 
los de nivel secundario, sin repeticiones.
b.	Informar qué nombres se repiten entre los alumnos de nivel primario y 
secundario.
c.	Informar qué nombres de nivel primario no se repiten en los de nivel 
secundario.
'''

primary_list = []
secundary_list = []
primary_student = "h"
secundary_student = "g"
while primary_student != "x":
    primary_student = input("Ingrese el nombre de pila de un alumno de nivel primario o x para terminar de ingresar: ")
    primary_student = primary_student.lower()
    if (primary_student != "x"):
        primary_list.append(primary_student)
    else:
        pass

while secundary_student != "x":
    secundary_student = input("Ingrese el nombre de pila de un alumno de nivel secundario o x para terminar de ingresar: ")
    secundary_student = secundary_student.lower()
    if (secundary_student != "x"):
        secundary_list.append(secundary_student)
    else:
        pass

print("Alumnos de nivel primario: ")
primary_appear = []
secundary_appear = []
for i in primary_list:
    if (i not in primary_appear):
        primary_appear.append(i)
        print(i)
    else:
        pass

print("Alumnos de nivel secundario:")

for i in secundary_list:
    if (i not in secundary_appear):
        secundary_appear.append(i)
        print(i)
    else:
        pass

print("Los nombres de alumnos que se repiten entre nivel primario y secundario son: ")

for i in primary_list:
    if i in secundary_list:
        print(i)

print("Los nombres de nivel primario que no se repiten en los de nivel secundario son: ")

for i in primary_list:
    if i not in secundary_list:
        print(i)

'''7.	Escribir un programa que procese strings ingresados por el 
usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al 
finalizar, informar la cantidad total de ocurrencias de cada carácter, 
en todos los strings ingresados. Ejemplo:
‘r’:5
‘%’:3
‘a’:8
'''

string_list = []
string = input("Ingrese un string: ")
for i in range(49):
    string = input("Ingrese otro string: ")
    string_list.append(string)

appear_characters = []
characters_occurrences = []
occurrences = 0
for i in string_list:
    for j in i:
        if (j not in appear_characters):
            appear_characters.append(j)
            for h in string_list:
                list_string = list(h)
                occurrences += list_string.count(j)
            characters_occurrences.append((j,occurrences))
            occurrences = 0
    else:
        pass
print("Caracteres en los strings ingresados y sus ocurrencias: ")
for i in characters_occurrences:
    print(f"{i[0]}:{i[1]}")

'''
8.	Diez equipos de la liga inter-barrial identificados con los números 
1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad 
todos contra todos.
Los goles anotados en cada encuentro se registraron en el siguiente cuadro:
Escriba un programa que:
o	Lea el cuadro de goles en un arreglo de dos dimensiones.
o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
o	Determine la cantidad de puntos obtenidos por cada equipo.

'''
soccer_matrix = []
gol_list = []
for i in range(10):
    for j in range(10):
        gol = int(input(f"Ingrese los goles anotados por el equipo {i + 1} en el partido {j + 1}: "))
        gol_list.append(gol)
    soccer_matrix.append(gol_list)
    gol_list = []

print("Tabla de goles:")

for i in range(10):
    for j in range(10):
        if (j == 9):
            print(soccer_matrix[i][j])
        else:
            print(soccer_matrix[i][j], end = " ")

results_list = []
win_counter = 0
lose_counter = 0
tie_counter = 0
gol_scored = 0
gol_received = 0
print("Los triunfos entregan 2 puntos, los empates 1 y las derrotas 0")
points = 0
for i in range(10):
    for j in range(10):
        if (i != j):
            gol_scored += soccer_matrix[i][j]
            gol_received += soccer_matrix[j][i]
            if (soccer_matrix[i][j] > soccer_matrix[j][i]):
                points += 2
                win_counter += 1
            elif (soccer_matrix[i][j] < soccer_matrix[j][i]):
                lose_counter += 1
            else:
                points += 1
                tie_counter += 1
    print(f"El equipo {i + 1} tuvo los siguientes resultados:")
    print(f"Triunfos: {win_counter}")
    print(f"Derrotas: {lose_counter}")
    print(f"Empates: {tie_counter}")
    print(f"La diferencia entre goles marcados y recibidos fue de {gol_scored - gol_received}")
    print(f"Los puntos obtenidos por el equipo fueron {points}")
    gol_scored = 0
    gol_received = 0
    points = 0
    win_counter = 0
    lose_counter = 0
    tie_counter = 0

'''9.	Escribir un programa que simule el juego clásico de Memoria 
(Memotest) utilizando matrices. El juego consiste en un tablero de 
cartas boca abajo y el objetivo es encontrar todas las parejas de 
cartas iguales.'''
memotest = [[0,1,2,3,4],[5,6,3,7,4],[8,5,9,10,6],[11,12,8,13,9],[14,15,11,16,13]]
guess = 0
win = False
print("Tendras 15 intentos para adivinar todas las cartas iguales que hay")
for i in range(15):
    print("Tablero:")
    for j in range(5):
        for h in range(5):
            if (h == 4):
                print(memotest[j][h])
            else:
                print(memotest[j][h], end = " ")
    row_guess1 = int(input("Introduzca el numero de fila en donde vio la primera carta: "))
    column_guess1 = int(input("Introduzca el numero de columna donde vio la primera carta: "))
    row_guess2 = int(input("Introduzca el numero de fila en donde vio la segunda arta: "))
    column_guess2 = int(input("Introduzca el numero de columna donde vio la segunda carta: "))
    if (memotest[row_guess1][column_guess1] == memotest[row_guess2][column_guess2]):
        guess += 1
        success = True
    else:
        success = False
    if (success):
        print("Bien acertaste!")
    else:
        print("Que pena, no acertaste")
    if (guess == 8):
        win = True
        print("Muy bien ganaste, felicidades!")
        break
    else:
        print(f"Te quedan {15 - (i + 1)} intentos")

if (win == False):
    print("Perdiste")
else:
    pass



            

'''
10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo 
siguiente:
a.	la diagonal principal.
b.	la diagonal inversa.
'''

rows = int(input("Ingrese la cantidad de filas a la matriz cuadrada: "))
columns = int(input("Ingrese la cantidad de columnas a la matriz cuadrada: "))
matrix = []
single_row = []
for i in range(rows):
    for j in range(columns):
        number = float(input("Ingrese un elemento a la matriz: "))
        single_row.append(number)
    matrix.append(single_row)
    single_row = []

print("Matriz: ")
for i in range(rows):
    for j in range(columns):
        if (j == columns - 1):
            print(matrix[i][j])
        else:
            print(matrix[i][j], end = " ")

print("Elementos de la diagonal principal:")
for i in range(rows):
    for j in range(columns):
        if (i == j == columns - 1):
            print(matrix[i][j])
        elif (i == j):
            print(matrix[i][j], end = " ")
        else:
            pass

print("Elementos de la diagonal inversa:")
row_reverse = 0
column_reverse = columns - 1
for i in range(rows):
    for j in range(columns):
        if (i == rows - 1 and j == 0):
            print(matrix[i][j])
        elif (i == row_reverse and j == column_reverse):
            print(matrix[i][j], end = " ")
            row_reverse += 1
            column_reverse -= 1
        else:
            pass

'''11.	Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el 
diccionario.'''

badge_dictionarie = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
badge_user = input("Ingrese una divisa para ver si se encuentra en el diccionario: ")
badge_user = badge_user.lower()
found = False
for i in badge_dictionarie.keys():
    if (i.lower() == badge_user):
        found = True
        badge_found = i
        break
    else:
        pass

if (found):
    print(f"El simbolo de la divisa es {badge_dictionarie[badge_found]}")
else:
    print("La divisa no se encuentra en el diccionario")


'''12.	Escribir un programa que pregunte al usuario su nombre, edad, 
dirección y teléfono y lo guarde en un diccionario. Después debe mostrar 
por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> 
y su número de teléfono es <teléfono>’.'''

data_person_dictionary = {}
name = input("Ingrese su nombre: ")
data_person_dictionary["Nombre"] = name
age = int(input("Ingrese su edad: "))
data_person_dictionary["Edad"] = age
address = input("Ingrese su direccion: ")
data_person_dictionary["Direccion"] = address
phone_number = int(input("Ingrese su numero de telefono: "))
data_person_dictionary["Telefono"] = phone_number
print(f"{data_person_dictionary['Nombre']} tiene {data_person_dictionary['Edad']}, vive en {data_person_dictionary['Direccion']} y su numero de telefono es {data_person_dictionary['Telefono']}")

'''13.	Escribir un programa que guarde en un diccionario los precios de 
las frutas de la tabla, pregunte al usuario por una fruta, un número de 
kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando 
de ello.'''

fruit_dictionary = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
fruit_user = input("Ingrese una fruta: ")
fruit_user = fruit_user.lower()
kg = float(input("Ingrese el numero de kilos de la fruta: "))
found = False
for i in fruit_dictionary.keys():
    if (i.lower() == fruit_user):
        found = True
        fruit_user_dictionary = i
        break
    else:
        pass
if (found):
    print(f"El precio a pagar es de ${fruit_dictionary[fruit_user_dictionary] * kg}")
else:
    print(f"La fruta no se encuentra en el catalogo")
    
