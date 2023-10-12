import math
'''1.	Escribir una función que, dado un número de DNI, retorne True si 
el número es válido y False si no lo es. Para que un número de DNI sea 
válido debe tener entre 7 y 8 dígitos.'''

def dni_valido(dni):
    if (len(dni) >= 7 and len(dni) <= 8):
        return True
    else:
        return False

'''2.	Escribir una función que, dado un string, retorne la longitud de 
la última palabra. Se considera que las palabras están separadas por uno 
o más espacios. También podría haber espacios al principio o al final 
del string pasado por parámetro.'''

def calculate_lenght(string):
    final_word = ""
    for i in range(len(string) - 1,-1,-1):
        if (string[i] == " " and i != len(string) - 1):
            for j in range(i + 1,len(string)):
                final_word += string[j]
            break
        else:
            pass
    if (string[len(string) - 1] == " "):
        return len(final_word) - 1
    else:
        return len(final_word)

'''3.	Escribir un programa que permita al usuario obtener un 
identificador para cada uno de los socios de un club. Para eso 
ingresará nombre completo y número de DNI de cada socio, 
indicando que finalizará el procesamiento mediante el ingreso 
de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre 
apellido. Podría ingresarse más de un nombre, en cuyo caso será: 
nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, 
el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso 
contrario, el programa debe dejar al usuario en un bucle hasta que 
ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará 
formado por: el primer nombre, la cantidad de letras del apellido y los 
3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254'''
def identifier(name, dni):
    identifier = ""
    last_name = ""
    words = name.split()
    for i in name:
        if (i == " "):
            break
        else:
            identifier += i
    identifier += str(len(words[-1]))
    for i in range(3):
        identifier += dni[i]
    return identifier

'''4.	Crea un programa que pida dos número enteros al usuario y diga si 
alguno de ellos es múltiplo del otro. Crea una función que reciba los dos 
números, y devuelve si el primero es múltiplo del segundo.'''

def multiples(number1, number2):
    if (number1 % number2 == 0):
        return True
    else:
        return False

'''5.	Crear una función que calcule la temperatura media de un día a 
partir de la temperatura máxima y mínima. Crear un programa principal, 
que utilizando la función anterior, vaya pidiendo la temperatura máxima 
y mínima de cada día y vaya mostrando la media. El programa pedirá el 
número de días que se van a introducir.'''

def half_temp(max_temp, min_temp):
    half_temperature = (max_temp + min_temp) / 2
    return half_temperature

'''6.	Crea una función que reciba como parámetro un texto y devuelve una 
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” 
devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha 
función.'''
def space_text(text):
    new_text = ""
    alphabet = "abcdefghijqlmnñopqrstuvwxyz"
    for i in range(len(text)):
        if (text[i].lower() in alphabet):
            new_text += text[i]
            new_text += " "
        else:
            new_text += text[i]
    return new_text

'''7.	Crea una función que recibe una lista con valores numéricos y 
devuelve el valor máximo y el mínimo. Crea un programa que pida números 
por teclado y muestre el máximo y el mínimo, utilizando la función 
anterior.'''

def max_min(number_list):
    max_number = number_list[0]
    min_number = number_list[0]
    for i in number_list:
        if (i > max_number):
            max_number = i
        else:
            pass
        if (i < min_number):
            min_number = i
        else:
            pass
    return max_number, min_number

'''8.	Diseñar una función que calcule el área y el perímetro de una 
circunferencia. Utiliza dicha función en un programa principal que lea 
el radio de una circunferencia y muestre su área y perímetro.'''

def area_perimeter(radio):
    area = round(math.pi * (radio ** 2),2)
    perimeter = round(2 * math.pi * radio,2)
    return area, perimeter

'''9.	Crear una subrutina llamada “login”, que recibe un nombre de 
usuario y una contraseña y te devuelve Verdadero si el nombre de usuario 
es “usuario1” y la contraseña es “asdasd”. Además recibe el número de 
intentos que se ha intentado hacer login y si no se ha podido hacer login 
incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una 
contraseña y se intente hacer login, solamente tenemos tres oportunidades 
para intentarlo.'''

def login(user_name, password, attempts):
    attempts += 1
    if (user_name == "usuario1" and password == "asdasd"):
        return True, attempts
    else:
        return False, attempts

'''10.	Escribir una función que aplique un descuento a un precio. Esta 
función tiene que recibir un diccionario con los precios y porcentajes 
del carrito de compra, aplicar los descuentos a los productos del carrito
y devolver el precio final de la compra.'''

def discount(prize, discountt):
    final_prize = prize * (1 - discountt / 100)
    return final_prize

'''11.	Escribir una función que reciba otra función y una lista, y 
devuelva otra lista con el resultado de aplicar la función dada a cada 
uno de los elementos de la lista.'''

def modified_list(listt):
    for i in range(len(listt)):
        listt[i] += 1

def list_new(listtt):
    modified_list(listtt)
    return listtt

'''12.	Escribir una función que reciba una frase y devuelva un diccionario
con las palabras que contiene y su longitud.'''

def lenght_dictionarie(phrase):
    phrase = phrase.split()
    words_dictionarie = {}
    for i in phrase:
        words_dictionarie[i] = len(i)

    return words_dictionarie

'''13.	Escribir una función que calcule el módulo de un vector.'''
def module(vector):
    mod = math.sqrt((vector.real ** 2) + (vector.imag ** 2)) 
    return mod

'''14.	Requerir al usuario que ingrese un número entero e informar si es 
primo o no, utilizando una función booleana que lo decida.'''

def prime_number(number):
    divisors = 0
    for i in range(1,number + 1):
        if (number % i == 0):
            divisors += 1
        else:
            pass
    if (divisors == 2):
        return True
    else:
        return False

'''15.	Escribir un programa que pida números al usuario, motrar el 
factorial de cada uno y, al finalizar, la cantidad total de números 
leídos en total. Utilizar una o más funciones, según sea necesario.'''

def function_go_on(go_on):
    if (go_on == "0"):
        return True
    else:
        return False

def function_total_numbers(total_numbers):
    total_numbers += 1
    return total_numbers

def factorial_function(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial

'''16.	Solicitar al usuario un número entero y luego un dígito. Informar 
la cantidad de ocurrencias del dígito en el número, utilizando para ello 
una función que calcule la frecuencia.'''

def function_occurrences(int_number,digit):
    occurrences = 0
    int_number = str(int_number)
    digit = str(digit)
    for i in int_number:
        if (i == digit):
            occurrences += 1
        else:
            pass
    return occurrences

'''17.	Solicitar al usuario el ingreso de números primos. La lectura 
finalizará cuando ingrese un número que no sea primo. Por cada número, 
mostrar la suma de sus dígitos. También solicitar al usuario un dígito 
e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.'''

def function_prime_number(number):
    divisors = 0
    for i in range(1,number + 1):
        if (number % i == 0):
            divisors += 1
        else:
            pass
    if (divisors == 2):
        return True
    else:
        return False

def function_digit_addition(number):
    number = str(number)
    addition = 0
    for i in number:
        addition += int(i)
    return addition

def digit_in_number(digit, number):
    number = str(number)
    digit = str(digit)
    occurrences = 0
    for i in number:
        if (digit == i):
            occurrences += 1
        else:
            pass
    return occurrences

def function_big_factorial(big_number):
    factorial = 1
    for i in range(big_number, 0, -1):
        factorial *= i
    return factorial




        
