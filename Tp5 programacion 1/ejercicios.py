import funciones

'''1.	Escribir una función que, dado un número de DNI, retorne True 
si el número es válido y False si no lo es. Para que un número de DNI 
sea válido debe tener entre 7 y 8 dígitos.'''

dni = input("Ingrese un dni: ")
validate_dni = funciones.dni_valido(dni)
if (validate_dni == True):
    print("Dni valido")
else:
    print("Dni no valido")

'''2.	Escribir una función que, dado un string, retorne la longitud de 
la última palabra. Se considera que las palabras están separadas por uno 
o más espacios. También podría haber espacios al principio o al final 
del string pasado por parámetro.'''

string = input("Ingrese una frase: ")
lenght_string = funciones.calculate_lenght(string)
print(f"La longitud de la ultima palabra del string es {lenght_string}")

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
ID -> Maria7254
'''

while True:
    dni = input("Introduzca el numero de dni: ")
    while funciones.dni_valido(dni) == False:
        dni = input("Introduzca el numero de dni: ")
    name = input("Ingrese el nombre completo o teclee enter para finalizar : ")
    if (name == ""):
        break
    id = funciones.identifier(name, dni)
    print(f"Su identificador es {id}")

'''4.	Crea un programa que pida dos número enteros al usuario y diga si 
alguno de ellos es múltiplo del otro. Crea una función que reciba los dos
números, y devuelve si el primero es múltiplo del segundo.'''

number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))
if (funciones.multiples(number1, number2)):
    print(f"El numero {number1} es multiplo de {number2}")
else:
    print(f"El numero {number1} no es multiplo de {number2}")

'''5.	Crear una función que calcule la temperatura media de un día a 
partir de la temperatura máxima y mínima. Crear un programa principal, 
que utilizando la función anterior, vaya pidiendo la temperatura máxima 
y mínima de cada día y vaya mostrando la media. El programa pedirá el 
número de días que se van a introducir.'''

days_number = int(input("Introduce el numero de dias que quieras saber la temperatura media: "))
for i in range(days_number):
    max_temperature = float(input(f"Ingrese la temperatura maxima del dia {i + 1}: "))
    min_temperature = float(input(f"Ingrese la temperatura minima del dia {i + 1}: "))
    half_temperature = funciones.half_temp(max_temperature, min_temperature)
    print(f"La temperatura media del dia {i + 1} fue de {half_temperature}")

'''6.	Crea una función que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” 
devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha
función.'''

text = input("Introduzca un texto: ")
text_with_spaces = funciones.space_text(text)
print(text_with_spaces)

'''7.	Crea una función que recibe una lista con valores numéricos y 
devuelve el valor máximo y el mínimo. Crea un programa que pida números 
por teclado y muestre el máximo y el mínimo, utilizando la función 
anterior.'''


numbers_list = []
for i in range(5):
    number = int(input("Introduzca un numero: "))
    numbers_list.append(number)
max_number, min_number = funciones.max_min(numbers_list)
print(f"El mayor numero de los ingresados fue {max_number} y el menor {min_number}")

'''8.	Diseñar una función que calcule el área y el perímetro de una 
circunferencia. Utiliza dicha función en un programa principal que lea 
el radio de una circunferencia y muestre su área y perímetro.'''

radio = float(input("Ingrese el radio de la circunferencia: "))
area, perimeter = funciones.area_perimeter(radio)
print(f"area = {area}")
print(f"perimetro = {perimeter}")

'''9.	Crear una subrutina llamada “login”, que recibe un nombre de 
usuario y una contraseña y te devuelve Verdadero si el nombre de usuario 
es “usuario1” y la contraseña es “asdasd”. Además recibe el número de 
intentos que se ha intentado hacer login y si no se ha podido hacer login 
incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una 
contraseña y se intente hacer login, solamente tenemos tres oportunidades 
para intentarlo.
'''
attemps = 0
success = 0
while True:
    user_name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    success, attemps = funciones.login(user_name, password, attemps)
    if (attemps == 3 and (user_name != "usuario1" or password != "asdasd")):
        print("Se le acabaron los intentos")
        break
    elif (user_name != "usuario1" or password != "asdasd"):
        print(f"Vuelva a intentar le quedan {3 - attemps} intentos")
    else:
        print("Ingreso exitoso!")
        break

'''10.	Escribir una función que aplique un descuento a un precio. Esta 
función tiene que recibir un diccionario con los precios y porcentajes 
del carrito de compra, aplicar los descuentos a los productos del carrito
y devolver el precio final de la compra.'''

products_dictionarie = {560:50,458:48,230:10.3}
i = 0
for key, value in products_dictionarie.items():
    i += 1
    final_prize = funciones.discount(key,value)
    print(f"Precio producto {i}: ${key}")
    print(f"Descuento producto {i}: %{value}")
    print(f"Precio final del producto {i}: ${final_prize}")

'''11.	Escribir una función que reciba otra función y una lista, y 
devuelva otra lista con el resultado de aplicar la función dada a cada 
uno de los elementos de la lista.'''

listt = [1,2,3,4,5,6]
new_listt = funciones.list_new(listt)
print(new_listt)

'''12.	Escribir una función que reciba una frase y devuelva un diccionario
con las palabras que contiene y su longitud.'''

phrase = input("Ingrese una frase: ")
word_dictionarie = funciones.lenght_dictionarie(phrase)
print(word_dictionarie)

'''13.	Escribir una función que calcule el módulo de un vector.'''

real_part = float(input("Ingresa la componente x  del vector: "))
imaginary_part = float(input("Ingresa la componente y del vector: "))
vector = complex(real_part,imaginary_part)
module_vector = funciones.module(vector)
print(f"El modulo del vector es {module_vector}")

'''14.	Requerir al usuario que ingrese un número entero e informar si es 
primo o no, utilizando una función booleana que lo decida.'''

number = int(input("Ingrese un numero para saber si es primo o no: "))
if (funciones.prime_number(number)):
    print(f"El numero {number} es primo")
else:
    print(f"El numero {number} no es primo")

'''15.	Escribir un programa que pida números al usuario, motrar el 
factorial de cada uno y, al finalizar, la cantidad total de números 
leídos en total. Utilizar una o más funciones, según sea necesario.'''

total_numbers = 0
while True:
    go_on = input("Ingrese 0 si quiere finalizar o cualquier otra tecla para continuar: ")
    if (funciones.function_go_on(go_on)):
        break
    else:
        number = int(input("Ingrese un numero para calcular su factorial: "))
        total_numbers = funciones.function_total_numbers(total_numbers)
        factorial = funciones.factorial_function(number)
        print(f"El factorial del numero {number} es {factorial}!")
print(f"La cantidad de numeros ingresados fue {total_numbers}")

'''16.	Solicitar al usuario un número entero y luego un dígito. Informar 
la cantidad de ocurrencias del dígito en el número, utilizando para ello 
una función que calcule la frecuencia.'''

int_number = int(input("Ingrese un numero entero: "))
digit = int(input("Ingrese un digito para contar las ocurrencias en el entero: "))
occurrences = funciones.function_occurrences(int_number,digit)
print(f"La cantidad de ocurrencias del digito {digit} en el numero {int_number} es {occurrences}")

'''17.	Solicitar al usuario el ingreso de números primos. La lectura 
finalizará cuando ingrese un número que no sea primo. Por cada número, 
mostrar la suma de sus dígitos. También solicitar al usuario un dígito 
e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.'''

big_number = 0
while True:
    number = int(input("Ingrese un numero primo o uno no primo para finalizar: "))
    if (funciones.function_prime_number(number)):
        if (number > big_number):
            big_number = number
        digit_addition = funciones.function_digit_addition(number)
        print(f"La suma de los digitos del numero {number} es {digit_addition}")
        digit = int(input("Ingrese un digito para saber cuantas veces aparece en el numero: "))
        total_occurrences = funciones.digit_in_number(digit, number)
        print(f"La cantidad de veces que aparece {digit} en {number} es {total_occurrences}")
    else:
        break
factorial_big_number = funciones.function_big_factorial(big_number)
print(f"El mayor numero ingresado primo fue {big_number} y su factorial es {factorial_big_number}!")

