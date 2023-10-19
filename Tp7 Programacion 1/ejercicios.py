'''1.	Escribe un programa que tome una lista de números como entrada y 
la ordene en orden ascendente utilizando el método de ordenamiento de 
burbuja.'''

bubble_list = []
number_elements = int(input("Ingresa el numero de elementos que vas a ingresar a la lista: "))
for i in range(number_elements):
    number = int(input("Ingresa un numero: "))
    bubble_list.append(number)

print("La lista antes de ordenarla:")

for i in range(len(bubble_list)):
    if (i == len(bubble_list) - 1):
        print(bubble_list[i])
    else:
        print(f"{bubble_list[i]},", end = " ")

length = len(bubble_list) - 1

for i in range(len(bubble_list) - 1):
    for j in range(length):
        if (bubble_list[j] > bubble_list[j + 1]):
            auxiliar_variable = bubble_list[j]
            bubble_list[j] = bubble_list[j + 1]
            bubble_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

print("Los elementos de la lista ordenados de forma ascendente quedan:")

for i in range(len(bubble_list)):
    if (i == len(bubble_list) - 1):
        print(bubble_list[i])
    else:
        print(f"{bubble_list[i]},", end = " ")

'''2.	Crea un programa que tome una lista de palabras como entrada y las 
ordene alfabéticamente en orden ascendente utilizando el método de 
ordenamiento de selección.'''

selection_list = []
number_elements = int(input("Ingresa el numero de elementos que vas a ingresar a la lista: "))
for i in range(number_elements):
    number = int(input("Ingresa un numero: "))
    selection_list.append(number)

print("La lista antes de ordenarla:")

for i in range(len(selection_list)):
    if (i == len(selection_list) - 1):
        print(selection_list[i])
    else:
        print(f"{selection_list[i]},", end = " ")
    
min_value = selection_list[0]
min_index = 0
start = 1
length = len(selection_list) - 1

for i in range(length):
    change = False
    min_index = i
    min_value = selection_list[min_index]
    for j in range(i,length):
        if (min_value > selection_list[j + 1]):
            min_value = selection_list[j + 1]
            min_index = j + 1
            change = True
        else:
            pass
    if (change):
        auxiliar_variable = selection_list[i]
        selection_list[i] = selection_list[min_index]
        selection_list[min_index] = auxiliar_variable
    else:
        pass

print("Los elementos de la lista ordenados de forma ascendente quedan:")

for i in range(len(selection_list)):
    if (i == len(selection_list) - 1):
        print(selection_list[i])
    else:
        print(f"{selection_list[i]},", end = " ")

'''3.	Crea una lista de diccionarios, donde cada diccionario contiene 
información sobre un libro (título, autor, año de publicación, etc.). 
Luego, escribe un programa que ordene la lista de libros en función de 
un campo específico, como el año de publicación o el autor.'''

book_list = []
book_dict = {}
number_of_books = int(input("Ingrese el numero de libro sobre los cual va a ingresar informacion: "))
for i in range(number_of_books):
    print(f"Ingresara informacion sobre el libro {i + 1}")
    title = input("Ingresa el titulo del libro: ")
    book_dict["titulo"] = title
    author = input("Ingrese el autor del libro: ")
    book_dict["autor"] = author
    year_publication = int(input("Ingrese el año de publicacion: "))
    book_dict["año de publicacion"] = year_publication
    book_list.append(book_dict)
    book_dict = {}

print("La lista antes de ordenarla:")

for i in range(len(book_list)):
    if (i == len(book_list) - 1):
        print(book_list[i])
    else:
        print(f"{book_list[i]},", end = " ")

print("Ordenaremos por año de publicacion de mas viejos a mas nuevos")

length = len(book_list) - 1

for i in range(len(book_list) - 1):
    for j in range(length):
        first_dictionary = book_list[j]
        second_dictionary = book_list[j + 1]
        if (first_dictionary["año de publicacion"] > second_dictionary["año de publicacion"]):
            auxiliar_variable = book_list[j]
            book_list[j] = book_list[j + 1]
            book_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1
        

print("La lista ordenada:")

for i in range(len(book_list)):
    if (i == len(book_list) - 1):
        print(book_list[i])
    else:
        print(f"{book_list[i]},", end = " ")

'''4.	Escribe un programa que tome una lista de cadenas como entrada y 
las ordene en orden ascendente según su longitud. Puedes utilizar el 
método de ordenamiento de inserción.'''

string_list = []
string_number = int(input("Introduzca el numero de cadenas que va a ingresar: "))
for i in range(string_number):
    string = input("Ingrese la cadena: ")
    string_list.append(string)

length = len(string_list)

for i in range(1,length):
    insert_value = string_list[i]
    insert_index = i
    while insert_index > 0 and len(string_list[insert_index - 1]) > len(insert_value):
        string_list[insert_index] = string_list[insert_index - 1]
        insert_index -= 1
    
    string_list[insert_index] = insert_value

print("La lista ordenada:")

for i in range(len(string_list)):
    if (i == len(string_list) - 1):
        print(string_list[i])
    else:
        print(f"{string_list[i]},", end = " ")

'''5.	Modifica uno de los ejercicios anteriores para ordenar la lista 
de números en orden descendente en lugar de ascendente.'''

print("Ejercicio 1 modificado:")
bubble_list = []
number_elements = int(input("Ingresa el numero de elementos que vas a ingresar a la lista: "))
for i in range(number_elements):
    number = int(input("Ingresa un numero: "))
    bubble_list.append(number)

print("La lista antes de ordenarla:")

for i in range(len(bubble_list)):
    if (i == len(bubble_list) - 1):
        print(bubble_list[i])
    else:
        print(f"{bubble_list[i]},", end = " ")

length = len(bubble_list) - 1

for i in range(len(bubble_list) - 1):
    for j in range(length):
        if (bubble_list[j] < bubble_list[j + 1]):
            auxiliar_variable = bubble_list[j]
            bubble_list[j] = bubble_list[j + 1]
            bubble_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

print("Los elementos de la lista ordenados de forma descendente quedan:")

for i in range(len(bubble_list)):
    if (i == len(bubble_list) - 1):
        print(bubble_list[i])
    else:
        print(f"{bubble_list[i]},", end = " ")

'''6.	Escribe un programa que tome una lista de números enteros y ordene 
la lista utilizando el algoritmo de ordenamiento por conteo.'''

def counting_sort_with_min(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val + 1
    count = [0] * range_val
    
    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_val):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for num in reversed(arr):
        position = count[num - min_val] - 1
        output[position] = num
        count[num - min_val] -= 1

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort_with_min(arr)
print("Arreglo ordenado:", sorted_arr)

'''7.	Crea una lista que contenga tanto números como cadenas de 
caracteres. Escribe un programa que ordene esta lista de manera que 
primero estén los números ordenados de menor a mayor y luego las cadenas 
de caracteres ordenadas alfabéticamente.'''

mixed_list = [30,"cadena",56,"jorgito",20,"matias",89,"santiago"]
number_list = []
string_list = []
for i in mixed_list:
    if isinstance(i,int):
        number_list.append(i)
    else:
        string_list.append(i)

mixed_list_new = []

length = len(number_list) - 1

for i in range(len(number_list) - 1):
    for j in range(length):
        if (number_list[j] > number_list[j + 1]):
            auxiliar_variable = number_list[j]
            number_list[j] = number_list[j + 1]
            number_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

for i in number_list:
    mixed_list_new.append(i)


length = len(string_list) - 1

for i in range(len(string_list) - 1):
    for j in range(length):
        if (string_list[j][0] > string_list[j + 1][0]):
            auxiliar_variable = string_list[j]
            string_list[j] = string_list[j + 1]
            string_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

print("Los elementos de la lista ordenados de forma ascendente quedan:")

for i in range(len(number_list)):
    if (i == len(number_list) - 1):
        print(number_list[i])
    else:
        print(f"{number_list[i]},", end = " ")

for i in range(len(string_list)):
    if (i == len(string_list) - 1):
        print(string_list[i])
    else:
        print(f"{string_list[i]},", end = " ")


'''8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para 
ordenar una lista de números.'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

array = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array)
print("Arreglo ordenado:", array)